# bots/justin.py
# Programming Club Iterated Prisoner's Dilemma Tournament
# Author: Justin Babineau

import random
from bots.base import BaseBot, Move

class JustinBot(BaseBot):
    """JustinBot — Adaptive strategy bot for the Programming Club Iterated Prisoner's Dilemma Tournament"""

    def __init__(self, name="JustinBot"):
        """Sets up bot"""
        super().__init__()
        self.name = name
        self.mode = "friendly"         # current behavioral mode
        self.coop_prob = 0.68          # initial cooperation probability
        self.window = 20               # history window for analysis
        self.opponent_type = None      # opponents behavioral mode
        self.last_forgive_round = -5   # number of rounds required to pass before forgiving again
        self.last_coop_rate = 0

    def reset(self):
        """Reset memory and state before each match"""
        super().reset()
        self.mode = "friendly"
        self.coop_prob = 0.68
        self.opponent_type = None
        self.last_forgive_round = -5
        self.last_coop_rate = 0

    def compute_coop_rate(self):
        """Compute opponent cooperation rate each move"""
        recent_opp = self.opponent_history[-self.window:]
        if not recent_opp:
            return 1.0
        coop_rate = recent_opp.count(Move.COOPERATE) / len(recent_opp)
        self.last_coop_rate = coop_rate
        return coop_rate

    def classify_opponent(self):
        """Classify opponent based on cooperation rate"""
        if len(self.opponent_history) >= 20:
            coop_rate_20 = self.opponent_history[-20:].count(Move.COOPERATE) / 20
            if coop_rate_20 > 0.9:
                self.opponent_type = "cooperator"
            elif coop_rate_20 < 0.4:
                self.opponent_type = "defector"
            else:
                self.opponent_type = "mixed"

    def update_mode(self, coop_rate):
        """Update mode based on recent cooperation"""
        if len(self.self_history) < 20:
            return
        if coop_rate >= 0.6:
            self.mode = "friendly"
        elif coop_rate < 0.3:
            self.mode = "defensive"
        else:
            self.mode = "probing"

    def get_move(self, game_state):
        """Decide next move based on opponent behavior and current mode"""
        coop_rate = self.compute_coop_rate()
        self.classify_opponent()
        self.update_mode(coop_rate)
        round_number = game_state.round_number

        # Forgive occasional accidental defections
        forgive_allowed = (round_number - self.last_forgive_round) >= 5
        if forgive_allowed and len(self.opponent_history) >= 2:
            if (self.opponent_history[-1] == Move.DEFECT and
                self.opponent_history[-2] == Move.COOPERATE and
                self.opponent_type != "defector"):
                self.last_forgive_round = round_number
                return Move.COOPERATE

        # Randomness for unpredictability
        rand_factor = random.uniform(-0.02, 0.02)

        # Early rounds: slightly more cooperative to test opponent
        if round_number < 10:
            self.coop_prob = 0.7
        else:
            if self.mode == "friendly":
                if self.opponent_type == "cooperator":
                    self.coop_prob = 0.95
                elif self.opponent_type == "defector":
                    self.coop_prob = 0.3
                else:
                    self.coop_prob = 0.65 * coop_rate + 0.35
            elif self.mode == "defensive":
                if self.opponent_type == "defector":
                    self.coop_prob = 0.05
                else:
                    self.coop_prob = 0.25 * coop_rate
            else:  # probing
                self.coop_prob = 0.1 if self.opponent_type == "defector" else 0.5

        # Choose final move
        return Move.COOPERATE if random.random() < self.coop_prob + rand_factor else Move.DEFECT
