#!/usr/bin/env python3
"""
poster_1 · The Critical Window — executive function by age, with the
LogicLab Kids band and the smartphone marker.

The band runs 7-13: the app's age range. The marker stays at 11, because the
"more than half of children own a smartphone by 11" line is Common Sense
Media's number, not ours.

Palette and type are the same as poster_charts.py / wef_top4.py, lifted from
the shipped app's LLTheme.swift. Sized to match the existing
posterimages/03_developmental_window.png (2000 x 1256 px).

Figure: own work (Python / matplotlib).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

SURF   = "#F5F0E0"
INK    = "#111726"
SUB    = "#5A6070"
GOLD   = "#48A8A6"
SIENNA = "#E01C47"
TEAL   = "#1F6B6A"
GRID   = "#DCD2B8"
FONT   = "Inter"
OUT = "/Users/patrik/logiclabposter/posterimages/03_developmental_window.png"
DPI = 250

BAND = (7, 13)          # the LogicLab Kids age range
PHONE_AGE = 11          # Common Sense Media: half of children own one by 11

plt.rcParams.update({
    "font.family": FONT, "font.size": 12,
    "axes.edgecolor": INK, "axes.linewidth": 1.0,
    "text.color": INK, "axes.labelcolor": INK,
    "xtick.color": INK, "ytick.color": INK,
})

fig, ax = plt.subplots(figsize=(8.0, 5.024), dpi=DPI)
fig.patch.set_facecolor(SURF)
ax.set_facecolor(SURF)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.spines["left"].set_color(INK)
ax.spines["bottom"].set_color(INK)
ax.tick_params(axis="both", length=4, width=1.0)
ax.set_axisbelow(True)

age = np.array([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
ef = np.array([55, 62, 68, 74, 79, 83, 87, 90, 93, 95.5, 97.5, 99, 100.0])
xs = np.linspace(5, 17, 400)
phone_ef = float(np.interp(PHONE_AGE, age, ef))

ax.axvspan(*BAND, color=GOLD, alpha=0.22, zorder=0)
ax.text(sum(BAND) / 2, 101.8, "LogicLab Kids", ha="center", va="top",
        fontsize=15, color=TEAL, fontweight="bold")
ax.plot(xs, np.interp(xs, age, ef), color=INK, lw=2.4, zorder=4)
ax.scatter(age, ef, s=20, color=INK, zorder=5)
ax.axvline(PHONE_AGE, ymin=0, ymax=(phone_ef - 50) / (103 - 50), color=SIENNA,
           lw=1.3, ls="--", zorder=3)
ax.scatter([PHONE_AGE], [phone_ef], s=60, facecolor=SURF, edgecolor=SIENNA,
           linewidth=2.0, zorder=6)
ax.annotate(f"more than half of children\nown a smartphone by {PHONE_AGE}",
            xy=(PHONE_AGE, phone_ef), xytext=(13.4, 66), fontsize=10.5,
            color=SIENNA, va="center", ha="left", style="italic",
            arrowprops=dict(arrowstyle="-", color=SIENNA, lw=1.0))
ax.set_xlim(5, 17.2); ax.set_ylim(50, 103)
ax.set_xticks(range(5, 18)); ax.set_yticks([50, 60, 70, 80, 90, 100])
ax.set_xlabel("Age (years)", fontsize=12)
ax.set_ylabel("Executive function (% of age-17 performance)", fontsize=12)
ax.tick_params(axis="both", labelsize=11)
ax.grid(axis="y", color=GRID, lw=0.9, zorder=0)
fig.subplots_adjust(left=0.125, right=0.975, top=0.95, bottom=0.215)
for i, t in enumerate(("Brydges et al. (2014). Diamond (2013), Annual Review of Psychology.",
                       "CAS complex-EF, N = 2,036, ages 5-17.  Figure: own work.")):
    fig.text(0.125, 0.055 - i * 0.036, t, fontsize=9, color=SUB,
             ha="left", va="bottom", style="italic")

fig.savefig(OUT, dpi=DPI, facecolor=SURF)
plt.close(fig)
print("saved", OUT)
