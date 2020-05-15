import json
import networkx as nx
import ndlib.models.epidemics as ep
import ndlib.models.ModelConfig as mc


class ProfileThresholdHate():
    def __init__(self):
        with open("data/actual/twitter_following_385.json", "r") as f:
            data = json.load(f)
        assert len(data.keys()) == 385
        self.g = nx.DiGraph()
        for each_user in data:
            followers = data[each_user]
            if len(followers) == 0:
                self.g.add_node(each_user)
            else:
                for each_follower in followers:
                    self.g.add_edge(each_user, each_follower)
        assert self.g.number_of_nodes() == 385
        self.model=None

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
            self.config.add_node_configuration("threshold", i, self.threshold)
            self.config.add_node_configuration("profile", i, self.profile)
        self.model.set_initial_status(self.config)

    def run_model(self, infected_nodes):
        self.config_new_model(infected_nodes)
        iterations = self.model.iteration_bunch(2)
        print(set(iterations[1]['status'].keys()))
        return set(iterations[1]['status'].keys())


    def run_model_timewise(self, infected_nodes, max_iterations=50):
    infected_updated=set()
    for each_infected in infected_nodes:
        infected_updated.add(each_infected)
        for each_follower in self.g[each_infected]:
            infected_updated.add(each_follower)
    infected_nodes = list(infected_updated)
    self.config_new_model(infected_nodes)
    iterations = self.model.iteration_bunch(max_iterations)
    return iterations