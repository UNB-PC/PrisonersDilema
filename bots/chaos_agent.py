from bots.base import BaseBot, Move
import random

class ChaosAgent(BaseBot):
    counter = 0

    def get_move(self, game_state):
        rounds = self.counter // 500
        limit = (rounds + 1)*449
        self.counter += 1
        rand = random.randint(1,100)

        if rand > 60 and self.counter < limit:
            result = Move.DEFECT
        else:
            result = Move.COOPERATE

        return result

        # if not game_state.opponent_history: # First round, no history yet
        #     return Move.COOPERATE
        # else:
        #     opponent_last_move = game_state.last_opponent_move()
        #     #......#
        # return Move.COOPERATE
