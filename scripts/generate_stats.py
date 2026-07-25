"""
Reads data/solved.json and regenerates assets/progress_chart.png.
Run manually with: python scripts/generate_stats.py
Run automatically every day by .github/workflows/update-stats.yml
"""

import json
import os
from collections import Counter
from datetime import datetime

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(ROOT, "data", "solved.json")
OUT_PATH = os.path.join(ROOT, "assets", "progress_chart.png")

DIFFICULTY_COLORS = {"Easy": "#2ecc71", "Medium": "#f1c40f", "Hard": "#e74c3c"}


def load_data():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, "r") as f:
        return json.load(f)


def build_chart(entries):
    entries = sorted(entries, key=lambda e: e["date"])
    dates = [datetime.strptime(e["date"], "%Y-%m-%d") for e in entries]

    # Daily counts
    daily_counts = Counter(e["date"] for e in entries)
    unique_dates = sorted(daily_counts.keys())
    daily_values = [daily_counts[d] for d in unique_dates]

    # Cumulative total
    cumulative = []
    total = 0
    for d in unique_dates:
        total += daily_counts[d]
        cumulative.append(total)

    # Difficulty breakdown
    diff_counts = Counter(e["difficulty"] for e in entries)
    diff_labels = ["Easy", "Medium", "Hard"]
    diff_values = [diff_counts.get(d, 0) for d in diff_labels]

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), facecolor="#0d1117")

    # --- Left: cumulative solves over time ---
    ax1 = axes[0]
    ax1.set_facecolor("#0d1117")
    ax1.plot(unique_dates, cumulative, color="#00f7ff", marker="o", linewidth=2)
    ax1.fill_between(unique_dates, cumulative, color="#00f7ff", alpha=0.15)
    ax1.set_title(f"Cumulative Problems Solved (Total: {total})", color="white", fontsize=11)
    ax1.tick_params(axis="x", colors="white", rotation=45, labelsize=8)
    ax1.tick_params(axis="y", colors="white")
    for spine in ax1.spines.values():
        spine.set_color("#30363d")

    # --- Right: difficulty breakdown ---
    ax2 = axes[1]
    ax2.set_facecolor("#0d1117")
    bars = ax2.bar(diff_labels, diff_values, color=[DIFFICULTY_COLORS[d] for d in diff_labels])
    ax2.set_title("Solved by Difficulty", color="white", fontsize=11)
    ax2.tick_params(axis="x", colors="white")
    ax2.tick_params(axis="y", colors="white")
    for spine in ax2.spines.values():
        spine.set_color("#30363d")
    for bar, value in zip(bars, diff_values):
        ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05,
                  str(value), ha="center", color="white", fontsize=9)

    plt.tight_layout()
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    plt.savefig(OUT_PATH, facecolor=fig.get_facecolor(), dpi=150)
    print(f"Chart saved to {OUT_PATH}")


if __name__ == "__main__":
    data = load_data()
    if not data:
        print("No entries in data/solved.json yet — add one to generate the chart.")
    else:
        build_chart(data)
