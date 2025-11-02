from bots.base import BaseBot, Move

class TotReversedBot(BaseBot):
    def get_move(self, game_state):

        # if first round, defect
        if not game_state.opponent_history: 
            return Move.DEFECT
        
        # if last round, coooperate
        if (game_state.round_number == 499):
            return Move.COOPERATE

        # if opponent looks stagnant, cooperate
        if game_state.round_number > 20:
            if Move.DEFECT not in game_state.opponent_history[-20:]:
                return Move.COOPERATE
            if Move.COOPERATE not in game_state.opponent_history[-20:]:
                return Move.COOPERATE
            
        # otherwise, tit-for-tat
        if (game_state.last_opponent_move() == Move.COOPERATE):
            return Move.COOPERATE
        return Move.DEFECT
