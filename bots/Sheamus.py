from bots.base import BaseBot, Move

class Sheamus(BaseBot):
    LastMoves = []
    roundCounter=0
    nice = True
    def get_move(self, game_state):
        roundCounter = roundCounter+1
        if not game_state.opponent_history: # First round, no history yet
            return Move.COOPERATE
        else:
            opponent_last_move = game_state.last_opponent_move()
            if nice = True:
              if len(LastMoves)>1:
                LastMoves.pop(0)
              LastMoves.append(opponent_last_move)
              if LastMoves[0] = Move.DEFECT and LastMoves[1] = Move.DEFECT:
                nice = False
            if opponent_last_move = Move.DEFECT and nice = False:
                return Move.DEFECT
            if roundCounter = 500:
                return Move.DEFECT
        return Move.COOPERATE
