from core.tournament import Tournament
from core.util import plot_bar_race
import matplotlib.pyplot as plt
from core.util import draw_leaderboard
from bots.always_cooperate import AlwaysCooperate
from bots.always_defect import AlwaysDefect

def main(compete=False):
    # Add bot instances here:
    bots = [
        AlwaysCooperate(),
        AlwaysDefect()
    ]

    tournament = Tournament(bots, noise_rate=0.03)
    history = tournament.run_evolution(
        generations=20,
        survival_rate=0.80,
        rounds_per_match=500,
        mutate=True
    )

    if compete:
        # Export final results
        tournament.export_results()

        # Plot evolution
        all_bots = [
            "AlwaysCooperate",
            "AlwaysDefect"
        ]

        result = plot_bar_race(history, all_bots, interval=1000, frames_per_gen=5)
        ani = result[0]
        try:
            ani.save("tournament_evolution.mp4", writer="ffmpeg", fps=8)
            print("[Info] Video saved as 'tournament_evolution.mp4'.")
        except Exception as e:
            print(f"[Warning] Could not save video: {e}")
        plt.show()

        draw_leaderboard(result[1], result[2])


if __name__ == "__main__":
    main(False)
