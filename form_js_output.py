import json
from copy import deepcopy


class FormOutput():
    def __init__(self):
        with open("data/actual/twitter_profile_385.json", "r") as f:
            self.user_data = json.load(f)

    def update_output_scores(self, iteration_results):
        format_final = []
        tobe_hate_update = set()
        for each_result in iteration_results:
            return_scores = deepcopy(self.user_data)
            status = each_result.get('status', {})
            for each_user in return_scores:
                if each_user in status and status[each_user]==1:
                    print(each_user, each_result['iteration'])
                    return_scores[each_user]['score'] = 1
                    tobe_hate_update.add(each_user)
                else:
                    return_scores[each_user]['score'] = 0
            format_final.append(return_scores)
        return format_final