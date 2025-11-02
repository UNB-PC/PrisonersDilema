from bots.base import BaseBot, Move

class Sheamus(BaseBot):
    def __init__(self)
        self.LastMoves = []
        self.roundCounter=0
        self.nice = True
    def get_move(self, game_state):
        self.roundCounter = self.roundCounter+1
        if not game_state.opponent_history: # First round, no history yet
            return Move.COOPERATE
        else:
            opponent_last_move = game_state.last_opponent_move()
            if self.nice == True:
              if len(self.LastMoves)>1:
                self.LastMoves.pop(0)
              self.LastMoves.append(opponent_last_move)
              if self.LastMoves[0] == Move.DEFECT and self.LastMoves[1] == Move.DEFECT:
                self.nice = False
            if opponent_last_move == Move.DEFECT and self.nice == False:
                return Move.DEFECT
            if self.roundCounter == 500:
                return Move.DEFECT
        return Move.COOPERATE
