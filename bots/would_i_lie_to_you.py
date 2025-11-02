from bots.base import BaseBot, Move

class WouldILieToYou(BaseBot):
    counter = 0
    def get_move(self, game_state):
        # print("Winner is would_i_lie_to_you.py")
        self.counter += 1
        remaining_matches = self.counter % 500
        result = ""
        if remaining_matches > 49:
            result = Move.COOPERATE
        else:
            result = Move.DEFECT
        return result

        # if not game_state.opponent_history: # First round, no history yet
        #     return Move.COOPERATE
        # else:
        #     opponent_last_move = game_state.last_opponent_move()
        #     #......#
        # return Move.COOPERATE
