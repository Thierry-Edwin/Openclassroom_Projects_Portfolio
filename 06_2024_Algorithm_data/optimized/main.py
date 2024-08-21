import csv
import time

from display import Display
from optimized import Optimized
from tool import Tool


display = Display()
algo = Optimized()
tool = Tool()


def run():
    """Lance le programme"""

    data_file = display.path_choice()
    max_budget = display.max_budget_choice() 
    score_user = display.score_choice()
    start = time.time()
    data = tool.read_data(data_file)
    action = algo.calculate_benef_data(data)
    scored_action = algo.calculate_score(action, max_budget, score_user)
    selected_actions, infos = algo.best_action(scored_action, max_budget)
    end = time.time()
    timer = end - start
    display.display_result(selected_actions, infos, timer)
    data_file = display.path_choice()
    tool.write_data(data_file, selected_actions, infos)


run()