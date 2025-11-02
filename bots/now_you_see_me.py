from bots.base import BaseBot, Move

class NowYouSeeMe(BaseBot):
    counter = 0
    def get_move(self, game_state):
        # print("Winner is now_you_see_me.py")
        self.counter += 1
        is_even = False
        if self.counter % 2 == 1:
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
