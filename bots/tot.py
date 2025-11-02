from bots.base import BaseBot, Move

class TotBot(BaseBot):
    def get_move(self, game_state):

        # if first round, cooperate
        if not game_state.opponent_history: 
            return Move.COOPERATE
        
        # if last round, defect
        if (game_state.round_number == 499):
            return Move.DEFECT

        # if opponent looks stagnant, defect
        if game_state.round_number > 20:
            if Move.DEFECT not in game_state.opponent_history[-20:]:
                return Move.DEFECT
            if Move.COOPERATE not in game_state.opponent_history[-20:]:
                return Move.DEFECT
            
        # otherwise, tit-for-tat
        if (game_state.last_opponent_move() == Move.COOPERATE):
            return Move.COOPERATE
        return Move.DEFECT
