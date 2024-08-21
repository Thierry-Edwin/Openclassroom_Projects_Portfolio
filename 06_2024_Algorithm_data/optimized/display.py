import questionary


class Display:
    def __init__(self):
        pass

    def path_choice(self):
        """Permet le choix du data_path et du budget_max"""

        print("----ALGORITHME OPTIMISE----")
        data_path = questionary.path("Choose the path of data (CSV)").ask()
        return data_path

    def max_budget_choice(self):
        while True:
            max_budget = questionary.text("What's your maximum budget?").ask()
            try:
                max_budget = int(max_budget)
                break
            except ValueError:
                print("Please enter a valid integer for the budget.")
        return max_budget

    def score_choice(self):
        """Permet de choisir un score pour affiner l'algo"""
        while True:
            score_user = questionary.text(
                "which score would you like to choose ? ( 1 -> 100 )"
            ).ask()
            try:
                score_user = int(score_user)
                break
            except ValueError:
                print("Please enter a valid score. Between 1 and 100")
        return score_user

    def display_result(self, selected_actions, infos, timer):
        """Affiche les informations dans la console"""

        percentage_profit, total_benef, total_cost = infos
        percentage_profit = round(percentage_profit, 2)
        print(f"Total profit : {total_benef} $")
        print(f"For a total cost : {total_cost} $")
        print(f"Profit : {percentage_profit} %")
        print("-Name---------Cost---Profit--Score")
        for action in selected_actions:
            print(action)
        print(f"Time : {timer}s")
        print(len(selected_actions))
