from bots.base import BaseBot, Move
import random

class Mia(BaseBot):
    def __init__(self):
        super().__init__()
        self.count = 0
        #self.forgiveness_rate = 0.2
        self.coop_rate = 0.9
        self.defect_rate = 0.2333

    def get_move(self, game_state):
        self.count += 1

        if not game_state.opponent_history: # First round, no history yet
            return Move.COOPERATE
        else:
            opponent_last_move = game_state.last_opponent_move()

            if (opponent_last_move == Move.COOPERATE):
                if random.random() < self.coop_rate:
                    return Move.COOPERATE
                else:
                    return Move.DEFECT
            else:
                if random.random() < self.defect_rate:
                    return Move.COOPERATE
                else:
                    return Move.DEFECT