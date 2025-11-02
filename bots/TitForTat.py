from bots.base import BaseBot, Move


class TitForTat(BaseBot):
    def __init__(self):
        self.opp_history = []

    def get_move(self, game_state):
        if not self.opp_history:
            return Move.COOPERATE

        return self.opp_history[-1]

    def record_result(self, self_move, opponent_move):
        self.opp_history.append(opponent_move)