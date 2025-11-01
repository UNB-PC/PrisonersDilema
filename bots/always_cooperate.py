from bots.base import BaseBot, Move

class AlwaysCooperate(BaseBot):
    def get_move(self, game_state):
        if not game_state.opponent_history: # First round, no history yet
            return Move.COOPERATE
        else:
            opponent_last_move = game_state.last_opponent_move()
            #......#
        return Move.COOPERATE
