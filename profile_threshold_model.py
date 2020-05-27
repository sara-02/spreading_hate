import json
import networkx as nx
import ndlib.models.epidemics as ep
import ndlib.models.ModelConfig as mc


class ProfileThresholdHate():
    def __init__(self):
        with open("data/actual/twitter_following_385.json", "r") as f:
            data = json.load(f)
        assert len(data.keys()) == 385
        with open("data/results/adoptor_user385.json", "r") as f:
            self.adoptor_score = json.load(f)
        with open("data/results/profile_user385.json", "r") as f:
            self.threshold_score = json.load(f)
        self.g = nx.DiGraph()
        for each_user in data:
            followers = data[each_user]
            if len(followers) == 0:
                self.g.add_node(each_user)
            else:
                for each_follower in followers:
                    self.g.add_edge(each_user, each_follower)
        assert self.g.number_of_nodes() == 385
        self.model = None

    def config_new_model(self, infected_nodes):
        self.model = ep.ProfileThresholdModel(self.g)
        self.config = mc.Configuration()
        self.config.add_model_parameter('blocked', 0)
        self.config.add_model_parameter('adopter_rate', 0)
        if not infected_nodes:
            infected_nodes = ["94152234"]
        self.config.add_model_initial_configuration("Infected", infected_nodes)
        self.threshold = 0.075
        self.profile = 0.085
        for i in self.g.nodes():
            if i in self.threshold_score:
                threshold = self.threshold_score[i]
            else:
                threshold = self.threshold
            if i in self.adoptor_score:
                profile = self.adoptor_score[i]
            else:
                profile = self.profile
            self.config.add_node_configuration("threshold", i, threshold)
            self.config.add_node_configuration("profile", i, profile)
        self.model.set_initial_status(self.config)

    def run_model(self, infected_nodes, max_iter=2):
        if not infected_nodes:
            infected_nodes = ["94152234"]
        self.config_new_model(infected_nodes)
        iterations = self.model.iteration_bunch(max_iter)
        return iterations