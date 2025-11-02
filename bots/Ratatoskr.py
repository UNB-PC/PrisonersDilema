from bots.base import BaseBot, Move

class Ratatoskr(BaseBot):
    def __init__(self):
        self.defect_count=0
        self.self_defect=0
        self.niceness=0.4
    def get_move(self, game_state):
        #print(self.niceness)
        if not game_state.opponent_history: # first round, no history yet
            return Move.COOPERATE
        elif self.self_defect/(game_state.round_number+1) > 0.9:
            return Move.COOPERATE
        elif game_state.round_number>=498:
            self.defect_count=0
            self.self_defect=0
            return Move.DEFECT
        else:
            opponent_last_move = game_state.last_opponent_move()
            if opponent_last_move == Move.DEFECT:
                self.defect_count+=1
            if self.defect_count/(game_state.round_number+1) > self.niceness:
                return Move.DEFECT
            else:
                return Move.COOPERATE
