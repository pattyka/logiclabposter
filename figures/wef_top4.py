#!/usr/bin/env python3
"""
WEF core skills, cut to the top four.

The eight-bar version is correct but unreadable at the size the poster gives
it: the labels shrink below the point where a judge standing in front of the
stand can read them. Four bars is the shortest cut that still *shows* analytical
thinking winning rather than just asserting it, and the caption says it is a
cut. Style and palette are the same as poster_charts.py, which lifts them from
the shipped app's LLTheme.swift.

Figure: own work (Python / matplotlib).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SURF = "#F6F0DE"
INK  = "#111726"
SUB  = "#5A6070"
GOLD = "#48A8A6"
MUTED = "#C2B69A"
GRID = "#DCD2B8"
FONT, DISPLAY = "Inter", "DM Serif Display"
OUT = "/Users/patrik/logiclabposter/posterimages/05_wef_skills_2030.png"
DPI = 500

plt.rcParams.update({
    "font.family": FONT, "font.size": 12,
    "axes.edgecolor": INK, "axes.linewidth": 1.0,
    "text.color": INK, "axes.labelcolor": INK,
    "xtick.color": INK, "ytick.color": INK,
})

# Sized to the poster's figure box (287 x 204) so the chart fills it
# instead of floating in a third of it.
fig, ax = plt.subplots(figsize=(8.0, 5.6), dpi=DPI)
fig.patch.set_facecolor(SURF)
ax.set_facecolor(SURF)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.spines["left"].set_color(INK)
ax.spines["bottom"].set_color(INK)
ax.tick_params(axis="both", length=4, width=1.0)
ax.set_axisbelow(True)

labels = ["Analytical thinking", "Resilience, flexibility & agility",
          "Leadership & social influence", "Creative thinking"]
vals = [69, 67, 61, 57]
y = list(range(len(labels)))

ax.barh(y, vals, height=0.58, color=[GOLD] + [MUTED] * 3, zorder=3)
for yi, v in zip(y, vals):
    ax.text(v + 1.5, yi, f"{v}", ha="left", va="center", family=DISPLAY,
            fontsize=26 if yi == 0 else 17, color="#1F6B6A" if yi == 0 else SUB)

ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=14.5)
ax.invert_yaxis()
ax.set_xlim(0, 80)
ax.set_xticks([0, 20, 40, 60, 80])
ax.tick_params(axis="x", labelsize=13)
ax.set_xlabel("Share of employers rating it a core skill, 2025 (%)", fontsize=14)
ax.grid(axis="x", color=GRID, lw=0.9, zorder=0)

fig.subplots_adjust(left=0.405, right=0.955, top=0.93, bottom=0.265)
for i, t in enumerate(("World Economic Forum (2025), The Future of Jobs Report 2025.",
                       "Top four of the eight named.  Figure: own work.")):
    fig.text(0.405, 0.075 - i * 0.038, t, fontsize=10.5, color=SUB,
             ha="left", va="bottom", style="italic")

fig.savefig(OUT, dpi=DPI, facecolor=SURF)
plt.close(fig)
print("saved", OUT)
