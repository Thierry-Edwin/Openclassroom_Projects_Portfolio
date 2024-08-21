# Algorithme Brute-force. Il créer toutes les combinaisons possible provenant d'un fichier CSV

import csv
import itertools
import time


"""Chaque action ne peut être achetée qu'une seule fois.

Nous ne pouvons pas acheter une fraction d'action.

Nous pouvons dépenser au maximum 500 euros par client."""


def read_data(file):
    """Lit le fichier CSV. Retourne une liste de tuple"""

    data = []
    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(tuple(row))
        return data


def format_data(data):
    """Formate les données"""

    formatted_data = []
    for row in data[1:]:
        cost = float(row[1].strip())
        benef = (float(row[2].strip()) * cost) / 100
        formatted_data.append((row[0], cost, benef))
    return formatted_data


def generate_combinations(actions):
    """
    Génère toutes les combinaisons possibles d'actions.
    """
    all_combinations = []
    for i in range(1, len(actions) + 1):
        all_combinations.extend(itertools.combinations(actions, i))
        # print(all_combinations)
    # print(len(all_combinations))
    return all_combinations


def brute_force(actions, max_budget):
    """
    Recherche de manière brute force toutes les combinaisons d'actions possibles
    et retourne la combinaison qui maximise le bénéfice total tout en respectant le budget maximal.
    """
    all_combinations = generate_combinations(actions)
    best_combination = None
    max_total_benefit = 0
    max_total_cost = 0

    for combination in all_combinations:
        total_cost = sum(action[1] for action in combination)
        total_benefit = sum(action[2] for action in combination)

        if total_cost <= max_budget and total_benefit > max_total_benefit:
            max_total_benefit = total_benefit = round(total_benefit, 2)
            best_combination = combination
            max_total_cost = total_cost
    best_combination = sorted(best_combination, key=lambda x: x[0], reverse=True)

    return best_combination, max_total_benefit, max_total_cost


def result_force(file, max_budget):
    start = time.time()
    data = read_data(file)
    actions = format_data(data)
    result, max_total_benefit, max_total_cost = brute_force(actions, max_budget)
    end = time.time()
    timer = end - start
    timer = round(timer, 2)
    print(f"Executé en {timer}s")
    return result, max_total_benefit, max_total_cost


file = "data/format_data.csv"
file1 = "../data/dataset1_Python+P7.csv"
file2 = "../data/dataset2_Python+P7.csv"
max_budget = 500


result, benef, cost = result_force(file, max_budget)
print(result)
percentage_profit = (benef / cost) * 100
percentage_profit = round(percentage_profit, 2)
print(f"Total profit : {benef}")
print(f"total cost : {cost}")
print(f"percentage profit : {percentage_profit}%")
