from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, validates
from sqlalchemy import event
from datetime import datetime, timezone
import re
from crm_project.project.config import Base
from crm_project.models.mixin_model import BaseModelMixin


# Modèle Customer
class Customer(Base, BaseModelMixin):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True, index=True)
    email = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(15), nullable=True, unique=True)
    company_name = Column(String(100), nullable=True)
    creation_date = Column(
        DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    last_update = Column(
        DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    commercial_contact_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relation vers User
    commercial_contact = relationship("User")
    # Relation vers ses contrats
    contracts = relationship(
        "Contract", back_populates="customer", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Customer(name={self.name}, id={self.id}>"

    @validates("email")
    def validate_email(self, key, email):
        # Regex pour valider le format de l'email
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_regex, email):
            raise ValueError("Invalid email format")
        return email

    @validates("phone_number")
    def validate_phone_number(self, key, phone_number):
        if phone_number and not phone_number.isdigit():
            raise ValueError("Invalid phone number format")
        if len(phone_number) < 8 or len(phone_number) > 15:
            raise ValueError("Phone number must be between 8 and 15 digits")
        return phone_number


# Événements SQLAlchemy pour mettre à jour automatiquement les dates
@event.listens_for(Customer, "before_insert")
def set_creation_date(mapper, connection, target):
    target.creation_date = datetime.now(timezone.utc)
    target.last_update = datetime.now(timezone.utc)


@event.listens_for(Customer, "before_update")
def set_last_update(mapper, connection, target):
    target.last_update = datetime.now(timezone.utc)
