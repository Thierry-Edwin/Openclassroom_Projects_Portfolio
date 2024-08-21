"""

Algorithme de calcul de score sur un ensemble de données.
Données : Tableau d'actions boursière [Name, Cost, Profit]

"""


class Optimized:
    def __init__(self):
        pass

    def calculate_benef_data(self, data):
        """
        Calcule le benefice en Euro

        Args:
            data (list) : Lisste des actions (nom de l'action, prix, profit$,  % de benefice)

        Return:
            list : Même liste d'actions (nom de l'action, prix, benefice en euro)
        """
        result = []
        for row in data[1:]:  # Commencer à l'index 1 pour exclure l'en-tête
            prix = float(row[1])
            pourcentage = float(row[2])
            profit = (prix * pourcentage) / 100
            profit = round(profit, 2)
            result.append((row[0], prix, profit, pourcentage))
        result = sorted(result, key=lambda x: x[1], reverse=True)
        return result

    def calculate_score(self, actions, max_budget, score_user):
        """
        Octroie un score à chaques actions en calculant le ratio (Benefice  / cout )

        Args:
            actions (list): liste des actions
            max_budget (int): Le budget maximum d'investissement

        Returns:
            action_scores (list): liste des actions (nom de l'action, prix, benef, score)
        """
        action_scores = []
        max_score = max(action[3] for action in actions)
        for action in actions:

            if action[1] <= 0:
                """signaler erreur"""
                continue
            else:
                if action[1] > max_budget:
                    score = 1
                else:
                    score = (action[3] / max_score) * 99 + 1
                    score = round(score, 2)

                if score > score_user:
                    action_scores.append((action[0], action[1], action[2], score))
        action_scores = sorted(action_scores, key=lambda x: x[3], reverse=True)
        return action_scores

    def best_action(self, actions, max_budget):
        """
        Selectionne les meilleurs actions, en fonction de leurs score et du budget max

        Args:
            actions (list): liste des actions contenant le score ratio
            max_budget (int): Max budget

        Returns:
            selected_actions (list) : Liste des actions selectionnées en fonction du budget
            infos (list): liste de tuples contenant le pourcentage de profit,
                            le benefice en euro, et le cout total
        """

        selected_actions = []
        total_cost = 0
        total_benef = 0
        for action, cost, benefit, score in actions:
            if total_cost + cost <= max_budget and action not in [
                a[0] for a in selected_actions
            ]:
                selected_actions.append((action, cost, benefit, score))
                total_cost += cost
                total_benef += benefit
                total_cost = round(total_cost, 2)
                total_benef = round(total_benef, 2)
        percentage_profit = (total_benef / total_cost) * 100
        infos = (percentage_profit, total_benef, total_cost)
        return selected_actions, infos
