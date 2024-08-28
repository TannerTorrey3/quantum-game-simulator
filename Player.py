import numpy as np
from more_itertools import locate
class Player:
    def __init__(self,payoff_matrix:list[list[float]]):
        self.payoff_matrix = payoff_matrix
        self.max_indices = []
        self.normalized_indices = []
        self.decision_data = []
        self.num_decisions = len(payoff_matrix)
        self.neg:int
        
    
    def normalize_decision(self,decision,max_value):
        return list(map(lambda x, y: 0.0 if np.isclose(x,0.0) else x/y, decision, max_value))
    
    def normalize_payoff(self):
        self.max_payoff = np.max(self.payoff_matrix)
        self.payoff_matrix = [self.normalize_decision(decision,self.max_payoff) for decision in self.payoff_matrix]

    def minimize_list(self):
        self.payoff_matrix = list(map(lambda x: 1.0-x,self.payoff_matrix))

    def find_indices(self, decision, max):
        return locate(decision, lambda x: x == max)
    
    def locate_maximums(self):
        self.max_indices = [self.find_indices(decision, np.max(decision)) for decision in self.payoff_matrix]
    
    def normalize_indices(self):
        self.normalize_indices = list(map(lambda x: x//2, self.max_indices))

    def calculate_decisions(self):
        '''Calculates theta'''
        modified = [None]*self.num_decisions
        for i, col_row in enumerate(self.payoff_matrix):
            self.decision_data.append(self.map_choice(col_row, i))
            theta = self.decision_data[i][0][0] * np.pi/2 
            indexes = self.decision_data[i][0][1]
            if(self.decision_data[i][0][2] == 0):
                theta *= 1.0
                if(self.decision_data[i][0][2] > 1):
                    indexes = list(range(self.decision_data[i][0][1][0]+1))
            
            modified[i] = (theta, indexes, self.decision_data[i][0][2])
        self.modified_payoff_matrix = modified
        self.calculate_negatives()

    def map_choice(self,decision_row,row_index):
        for i, _ in  enumerate(decision_row):
            if i not in self.max_indices[row_index]:
                decision_row[i] = 0.0
        choice  = list(zip(filter(lambda x: np.not_equal(x,0.0), choice),self.normalized_indices, self.max_indices[row_index]))
        return choice
    
    def calculate_negatives(self):
        self.neg = len(list(filter(lambda x: x[0] < 0.0)))