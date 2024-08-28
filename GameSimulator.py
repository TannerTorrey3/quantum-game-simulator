#619-484-7665
import numpy as np
# from classiq import *
from Player import Player

class GameSimulator:
    def __init__(self):
        self.players:list[Player]
        self.target = False
        self.num_players = 0


    def add_player(self,payoff:list[list[float]]):
        self.players.append(Player(payoff_matrix=payoff))
        self.num_players+=1
        
    def set_target(self,mode:bool):
        self.target = mode
    
    def normalize_players(self):
        for player in self.players:
            max_payoff = np.max(player.payoff_matrix)
            for decision in player.payoff_matrix:
                player.normalize_decision(decision,max_payoff) 
    
    def process_payoff(self,player:Player):
        '''Function that processes a payoff matrix for a single player
        :param player: A player object to process with.
        
        '''
        if self.target:
            player.minimize_list()

        player.locate_maximums()
        player.normalize_indices()
        player.calculate_decisions()

    def create_game_circ(self):
        #TODO use 
        #TODO Use numpy.transpose to convert Nd -> 2d payoff matrixes. Then all the player code will work with any dimensional game
        #TODO use utiility functions to generate payoff matrixes or feed in a payoff as the input of a Player
        #TODO create a Player class that holds player index, payoff matrix and utility functions, and all associated lists in the helper functions IE map_theta
        self.normalize_players()    
        for player in self.players:
            self.process_payoff(player)

        #TODO determine how to use Classiq SDK from this context
        #TODO continue the process from here... need to initialize a quantum program and use hadamards. 
        #TODO use decision_data for each player to apply ry
        



        
