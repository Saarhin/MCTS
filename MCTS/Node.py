import numpy as np

class Node:
    def __init__(self, prior, to_play):
        self.prior = prior            # the probability of selecting this node from its parent
        self.to_play = to_play        # whose turn is it to play (1 or -1)
        self.children = {}
        self.visit_count = 0
        self.value_sum = 0
        self.state = None


    def value(self):
        return self.value_sum / self.visit_count
    
    def expanded(self):
        return len(self.children) > 0
    
    def select_action(self, temperature):
        visit_counts = np.array([child.visit_count for child in self.children.values()])
        actions = [action for action in self.children.keys()]

        if temperature == 0 :
            action = actions[np.argmax(visit_counts)]
        elif temperature == float("inf"):
            action = np.random.choice(actions)
        else:
            visit_count_distribution = visit_counts ** (1 / temperature)
            visit_count_distribution = visit_count_distribution / sum(visit_count_distribution)
            action = np.random.choice(actions, p=visit_count_distribution)

        return action
    
    
