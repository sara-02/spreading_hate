import json
from copy import deepcopy


class FormOutput():
    def __init__(self):
        # with open("data/actual/twitter_following_385.json", "r") as f:
        #     data = json.load(f)
        # assert len(data.keys()) == 385
        # self.g = nx.DiGraph()
        # for each_user in data:
        #     followers = data[each_user]
        #     if len(followers) == 0:
        #         self.g.add_node(int(each_user))
        #     else:
        #         for each_follower in followers:
        #             self.g.add_edge(int(each_user), int(each_follower))
        with open("data/actual/twitter_profile_385.json", "r") as f:
            self.user_data = json.load(f)

    def update_iter_1_scores(self, update_nodes):
        return_scores = deepcopy(self.user_data)
        for each_user in return_scores:
            if each_user in update_nodes:
                return_scores[each_user]['score'] = 1
            else:
                return_scores[each_user]['score'] = 0
        return return_scores