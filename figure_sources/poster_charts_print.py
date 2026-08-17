#!/usr/bin/env python3
"""
The five data charts on poster_1 and poster_3, re-rendered at their final
PRINT size so the type inside them is legible from standing distance.

Why this file exists
--------------------
The originals were drawn at 8.0-8.8 in wide and then dropped into slots that
are 28.5 cm / 28.8 cm wide. At 1 CSS px = 1 mm on a 70 cm poster that is
~11.2 in, so they were being blown up by ~1.3x — and, worse, their aspect
ratios did not match the slots, so each one lost 20-80 mm of width to
letterboxing and ended up smaller than the space allowed.

Here every figure is drawn AT the slot's exact aspect ratio and AT its exact
print width in inches. That makes the figure 1:1 with the printed poster, so
a point size written below is literally the point size on the wall:

    poster_1 figure slot   285 x 162 px  ->  11.20 x 6.36 in   (ratio 1.761)
    poster_3 figure slot   288 x 203 px  ->  11.34 x 8.00 in   (ratio 1.418)

Type is set at 15 pt for axes and 11.5 pt for source lines — roughly 5 mm and
4 mm cap-to-baseline on the print, readable at 1.5-2 m.

Palette and typefaces are the shipped app's (Theme/LLTheme.swift), same as
the previous pass. Backgrounds are transparent so the poster's own cream
shows through.

Same data and same scientific structure as the submitted EUCYS paper figures.

Figures: own work (Python / matplotlib).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# ============================== LLTheme.swift, verbatim ======================
PAPER  = "#EFE3C7"   # LLTheme.bg
SURF   = "#F7F0DE"   # --cream-light: the card these sit on
INK    = "#111726"
SUB    = "#5A6070"
GOLD   = "#48A8A6"   # the one accent
GREEN  = "#48A8A6"
SIENNA = "#E01C47"   # reserved for the threat
TEAL   = "#1F6B6A"

MUTED = "#C2B69A"    # de-emphasised bars, inside the parchment family
GRID  = "#DCD2B8"

FONT    = "Inter"
DISPLAY = "DM Serif Display"

# ── type scale, in real printed points (the figures are 1:1 with the poster)
AXIS   = 15.0        # tick labels
LABEL  = 15.5        # axis titles
NOTE   = 13.0        # the italic one-liners inside the plot
CREDIT = 11.5        # source lines

plt.rcParams.update({
    "font.family": FONT, "font.size": AXIS,
    "axes.edgecolor": INK, "axes.linewidth": 1.3,
    "text.color": INK, "axes.labelcolor": INK,
    "xtick.color": INK, "ytick.color": INK,
})

OUT = "/Users/patrik/logiclabposter/posterimages"
DPI = 320

# slot geometry, in inches, measured off the rendered posters
P1 = (11.20, 6.36)   # poster_1 .img-wrap  (285 x 162 px)
P3 = (11.34, 8.00)   # poster_3 .fig-canvas (288 x 203 px)


def frame(figsize):
    fig, ax = plt.subplots(figsize=figsize, dpi=DPI)
    ax.set_facecolor("none")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(INK)
    ax.spines["bottom"].set_color(INK)
    ax.tick_params(axis="both", length=5, width=1.3, labelsize=AXIS)
    ax.set_axisbelow(True)
    return fig, ax


def credit(fig, l1, l2, x=0.135, y=0.055):
    for i, t in enumerate((l1, l2)):
        fig.text(x, y - i * 0.036, t, fontsize=CREDIT, color=SUB,
                 ha="left", va="bottom", style="italic")


def big(ax, x, y, text, color, size, ha="center", va="bottom"):
    """Numbers are set in the display serif, as on the poster itself."""
    ax.text(x, y, text, ha=ha, va=va, fontsize=size, color=color,
            family=DISPLAY)


def save(fig, name):
    fig.savefig(f"{OUT}/{name}.png", dpi=DPI, transparent=True)
    plt.close(fig)
    print(f"saved {name}.png")


# ═══════════════════════════════ poster_1 · FIG 1 — screen media use ═════════
fig, ax = frame(P1)
x, w = [0, 1], 0.32
v19, v21 = [4 + 44 / 60, 7 + 22 / 60], [5 + 33 / 60, 8 + 39 / 60]
ax.bar([xi - w / 2 for xi in x], v19, w, color=MUTED, label="2019", zorder=3)
ax.bar([xi + w / 2 for xi in x], v21, w, color=SIENNA, label="2021", zorder=3)
for xi, v, l in zip([xi - w / 2 for xi in x], v19, ["4:44", "7:22"]):
    big(ax, xi, v + 0.18, l, SUB, size=20)
for xi, v, l in zip([xi + w / 2 for xi in x], v21, ["5:33", "8:39"]):
    big(ax, xi, v + 0.18, l, SIENNA, size=26)
ax.set_xticks(x)
ax.set_xticklabels(["Tweens (8–12)", "Teens (13–18)"], fontsize=LABEL)
ax.set_ylim(0, 10.4); ax.set_yticks([0, 2, 4, 6, 8, 10]); ax.set_xlim(-0.62, 1.62)
ax.set_ylabel("Daily entertainment screen media (hours)", fontsize=LABEL)
ax.grid(axis="y", color=GRID, lw=1.1, zorder=0)
leg = ax.legend(frameon=False, fontsize=AXIS, loc="upper left")
for t in leg.get_texts():
    t.set_color(INK)
fig.subplots_adjust(left=0.105, right=0.985, top=0.965, bottom=0.210)
credit(fig, "Common Sense Media (2019, 2021), The Common Sense Census.",
            "+17% across both groups in two years.  Figure: own work.",
            x=0.105, y=0.048)
save(fig, "04_screen_media")


# ═══════════════════════════ poster_1 · FIG 2 — developmental window ═════════
fig, ax = frame(P1)
age = np.array([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
ef = np.array([55, 62, 68, 74, 79, 83, 87, 90, 93, 95.5, 97.5, 99, 100.0])
xs = np.linspace(5, 17, 400)
ax.axvspan(7, 11, color=GOLD, alpha=0.22, zorder=0)
ax.text(9, 101.6, "LogicLab Kids", ha="center", va="top", fontsize=18,
        color=TEAL, fontweight="bold")
ax.plot(xs, np.interp(xs, age, ef), color=INK, lw=3.0, zorder=4)
ax.scatter(age, ef, s=26, color=INK, zorder=5)
ax.axvline(11, ymin=0, ymax=(87 - 50) / (103 - 50), color=SIENNA, lw=1.7,
           ls="--", zorder=3)
ax.scatter([11], [87], s=90, facecolor=SURF, edgecolor=SIENNA, linewidth=2.6,
           zorder=6)
ax.annotate("more than half of children\nown a smartphone by 11",
            xy=(11, 87), xytext=(12.1, 66), fontsize=NOTE, color=SIENNA,
            va="center", ha="left", style="italic",
            arrowprops=dict(arrowstyle="-", color=SIENNA, lw=1.2))
ax.set_xlim(5, 17.2); ax.set_ylim(50, 103)
ax.set_xticks(range(5, 18)); ax.set_yticks([50, 60, 70, 80, 90, 100])
ax.set_xlabel("Age (years)", fontsize=LABEL)
ax.set_ylabel("Executive function\n(% of age-17 performance)", fontsize=LABEL)
ax.grid(axis="y", color=GRID, lw=1.1, zorder=0)
fig.subplots_adjust(left=0.135, right=0.985, top=0.965, bottom=0.240)
credit(fig, "Brydges et al. (2014). Diamond (2013), Annual Review of Psychology.",
            "CAS complex-EF, N = 2,036, ages 5-17.  Figure: own work.",
            x=0.135, y=0.046)
save(fig, "03_developmental_window")


# ══════════════════════════ poster_3 · FIG 5 — EEG connectivity ══════════════
fig, ax = frame(P3)
x, vals = [0, 1], [79, 42]
ax.bar(x, vals, width=0.5, color=[GREEN, SIENNA], zorder=3)
for xi, v in zip(x, vals):
    big(ax, xi, v + 2.4, f"{v}", SIENNA if xi == 1 else GREEN, size=42)
ax.text(0.5, 91.5, "47% fewer connections with ChatGPT", ha="center",
        va="bottom", fontsize=NOTE, color=SUB, style="italic")
ax.set_xticks(x)
ax.set_xticklabels(["Brain-only\n(no tools)", "ChatGPT\n(LLM assistant)"],
                   fontsize=LABEL)
ax.set_xlim(-0.62, 1.62); ax.set_ylim(0, 100); ax.set_yticks([0, 20, 40, 60, 80])
ax.set_ylabel("Significant brain connections\n(alpha band, EEG dDTF)",
              fontsize=LABEL)
ax.grid(axis="y", color=GRID, lw=1.1, zorder=0)
fig.subplots_adjust(left=0.150, right=0.980, top=0.965, bottom=0.215)
credit(fig, "Kosmyna et al. (2025), MIT Media Lab, arXiv:2506.08872. Adult sample.",
            "Alpha-band dDTF, p < .05, Sessions 1-3, N = 54.  Figure: own work.",
            x=0.150, y=0.048)
save(fig, "02_eeg_connectivity")


# ═══════════════════════════ poster_3 · FIG 6 — ability to quote ═════════════
fig, ax = frame(P3)
x, vals = [0, 1, 2], [11.1, 11.1, 83.3]
ax.bar(x, vals, width=0.58, color=[MUTED, MUTED, SIENNA], zorder=3)
for xi, v in zip(x, vals):
    big(ax, xi, v + 2.4, f"{v:.1f}", SIENNA if xi == 2 else SUB,
        size=34 if xi == 2 else 24)
ax.text(0.02, 0.975, "ChatGPT group vs. Search and Brain-only:  p < .001",
        transform=ax.transAxes, ha="left", va="top", fontsize=NOTE,
        color=SUB, style="italic")
ax.set_xticks(x)
ax.set_xticklabels(["Brain-only\n(no tools)\n2 of 18", "Search\nEngine\n2 of 18",
                    "ChatGPT\n(LLM assistant)\n15 of 18"], fontsize=LABEL)
ax.set_ylim(0, 100); ax.set_yticks([0, 20, 40, 60, 80, 100])
ax.set_ylabel("Failed to quote their own essay (%)", fontsize=LABEL)
ax.grid(axis="y", color=GRID, lw=1.1, zorder=0)
fig.subplots_adjust(left=0.120, right=0.980, top=0.965, bottom=0.258)
credit(fig, "Kosmyna et al. (2025), MIT Media Lab, arXiv:2506.08872. Adult sample.",
            "Session 1 quoting task, N = 54 (18 per group).  Figure: own work.",
            x=0.120, y=0.044)
save(fig, "01_ai_quoting")


# ═════════════════════════ poster_3 · FIG 7 — WEF skills 2030 ════════════════
fig, ax = frame(P3)
labels = ["Analytical thinking", "Resilience, flexibility\n& agility",
          "Leadership & social\ninfluence", "Creative thinking",
          "Motivation &\nself-awareness", "Technological literacy",
          "Empathy & active\nlistening", "Curiosity & lifelong\nlearning"]
vals = [69, 67, 61, 57, 52, 51, 50, 50]
y = list(range(len(labels)))
ax.barh(y, vals, height=0.62, color=[GOLD] + [MUTED] * 7, zorder=3)
for yi, v in zip(y, vals):
    big(ax, v + 1.6, yi, f"{v}", TEAL if yi == 0 else SUB,
        size=26 if yi == 0 else 19, ha="left", va="center")
ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=AXIS)
ax.invert_yaxis(); ax.set_xlim(0, 82); ax.set_xticks([0, 20, 40, 60, 80])
ax.set_xlabel("Share of employers rating it a core skill, 2025 (%)",
              fontsize=LABEL)
ax.grid(axis="x", color=GRID, lw=1.1, zorder=0)
fig.subplots_adjust(left=0.235, right=0.980, top=0.975, bottom=0.185)
credit(fig, "World Economic Forum (2025), The Future of Jobs Report 2025.",
            "Top eight core skills named by employers.  Figure: own work.",
            x=0.235, y=0.042)
save(fig, "05_wef_skills_2030")

print("font:", FONT, "/", DISPLAY)
