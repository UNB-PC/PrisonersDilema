from bots.base import BaseBot, Move
import random

class Punisher(BaseBot):
    def __init__(self):
        self.my_history = []
        self.opp_history = []
        self.trust = 0.4
        self.temper = 0.0
        self.exploit_count = 0

    def get_move(self, game_state):
        if not self.opp_history:
            return Move.COOPERATE
        
        last_opp = self.opp_history[-1]
        if last_opp == Move.COOPERATE:
            self.trust = min(1.0, self.trust + 0.08)
            self.temper = max(0.0, self.temper - 0.03)
        else:
            self.trust = max(0.0, self.trust - 0.15)
            self.temper = min(1.0, self.temper + 0.12)

        total_rounds = len(self.opp_history)
        coop_rate = self.opp_history.count(Move.COOPERATE) / total_rounds
        
        # recent behavior (last 8 rounds)
        recent_window = min(8, total_rounds)
        recent_coop_rate = self.opp_history[-recent_window:].count(Move.COOPERATE) / recent_window
        
        # check if opponent is shifting strategy
        is_becoming_hostile = (coop_rate > 0.6 and recent_coop_rate < coop_rate - 0.2)
        
        # determine mode
        if coop_rate > 0.8 and recent_coop_rate > 0.75:
            mode = "exploit"
        elif coop_rate < 0.35 or recent_coop_rate < 0.25:
            mode = "retaliate"
        elif is_becoming_hostile:
            mode = "defensive"
        else:
            mode = "diplomat"

        # Decide move based on mode
        if mode == "exploit":
            self.exploit_count += 1
            # for exploitation: start at 20%, increase to 35%
            exploit_rate = min(0.35, 0.20 + (self.exploit_count * 0.01))
            if random.random() < exploit_rate:
                move = Move.DEFECT
            else:
                move = Move.COOPERATE
        elif mode == "retaliate":
            self.exploit_count = 0
            if self.opp_history[-1] == Move.DEFECT:
                move = Move.DEFECT if random.random() < 0.8 else Move.COOPERATE
            else:
                move = Move.COOPERATE if random.random() < 0.3 else Move.DEFECT
        elif mode == "defensive":
            self.exploit_count = 0
            if random.random() < 0.6:
                move = Move.COOPERATE
            else:
                move = Move.DEFECT
        else:
            # diplomat mode where i can use temper
            coop_probability = max(0.2, min(0.85, self.trust - self.temper * 0.4))
            if random.random() < coop_probability:
                move = Move.COOPERATE
            else:
                move = Move.DEFECT

        return move
        
    def record_result(self, self_move, opponent_move):
        self.my_history.append(self_move)
        self.opp_history.append(opponent_move)