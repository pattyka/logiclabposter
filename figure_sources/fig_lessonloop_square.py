#!/usr/bin/env python3
"""
FIG 4 — stage grammar and the reinforcement loop, re-laid out for the
poster_2 figure slot (square, ~1:1, transparent background).

The six stages run 3 + 3 instead of 6 across, so each box is twice the
width it was, and the loop row below closes back to STORY down the left
margin. Nothing floats: the figure fills its card.

Figure: own work (Python / matplotlib).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from matplotlib import font_manager as fm


def pick(names):
    avail = {f.name for f in fm.fontManager.ttflist}
    for n in names:
        if n in avail:
            return n
    return "DejaVu Sans"


FONT = pick(["Inter", "Helvetica Neue", "Arial"])

PAPER = "#F7F0DE"       # --cream-light, the figure card behind this
SOFT  = "#F1E7CE"
CARD  = "#EDE3CA"
TINT  = "#D3E6E5"
INK   = "#111726"
TEAL  = "#1F6B6A"
SUB   = "#5A6070"

plt.rcParams.update({"font.family": FONT, "font.size": 11, "text.color": INK})

fig, ax = plt.subplots(figsize=(10.0, 9.6), dpi=400)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis("off")
ax.set_position([0.008, 0.008, 0.984, 0.984])


def box(x, y, w, h, title, body, fill=PAPER, lw=1.0,
        title_size=11.8, body_size=10.0, gap=5.0):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=fill, edgecolor=INK,
                           linewidth=lw, zorder=3))
    ax.text(x + w / 2, y + h - 2.2, title, ha="center", va="top",
            fontsize=title_size, fontweight="bold", zorder=4)
    ax.text(x + w / 2, y + h - 2.2 - gap, body, ha="center", va="top",
            fontsize=body_size, color=SUB, linespacing=1.5, zorder=4)


def line(x1, y1, x2, y2, lw=1.3):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-",
                                 linewidth=lw, color=INK, zorder=6))


def arrow(x1, y1, x2, y2, lw=1.3):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                                 mutation_scale=15, linewidth=lw,
                                 color=INK, zorder=6))


X0, X1, X2, W = 4.0, 36.5, 69.0, 30.5
R1, R2, H = 68.0, 44.0, 19.0
LY, LH = 2.0, 17.0
MID1, MID2, MIDL = R1 + H / 2, R2 + H / 2, LY + LH / 2

# ───────────────────────────────────────────────── ONE LESSON — stage grammar
ax.text(0.5, 99.4, "ONE LESSON  ·  A FIXED STAGE GRAMMAR",
        ha="left", va="top", fontsize=12.5, fontweight="bold", color=TEAL)
ax.text(0.5, 95.2,
        "Every lesson in all six modules runs the same sequence. The four task types\n"
        "are interactive: the child acts, and never reads a definition.",
        ha="left", va="top", fontsize=10.0, color=SUB, linespacing=1.5)

box(X0, R1, W, H, "STORY",
    "the concept is planted in\na scene the child knows,\nbefore anything is named",
    fill=SOFT)
box(X1, R1, W, H, "QUIZ",
    "choose the sound\ncontinuation of an argument")
box(X2, R1, W, H, "SPOT-IT",
    "locate the faulty step\nin a passage")

box(X0, R2, W, H, "SORT-IT",
    "order a scrambled\nchain of inference")
box(X1, R2, W, H, "BUILD-IT",
    "assemble a conclusion\nfrom its premises")
box(X2, R2, W, H, "AI CHALLENGE",
    "a short Socratic dialogue.\nThe model may not give\nthe answer, and it comes\nlast: after the child has\ndone the work",
    fill=TINT, lw=1.7)

arrow(X0 + W, MID1, X1, MID1)
arrow(X1 + W, MID1, X2, MID1)

# SPOT-IT drops into the second row, which runs left to right again
line(X2 + W / 2, R1, X2 + W / 2, 65.6)
line(X2 + W / 2, 65.6, X0 + W / 2, 65.6)
arrow(X0 + W / 2, 65.6, X0 + W / 2, R2 + H)

arrow(X0 + W, MID2, X1, MID2)
arrow(X1 + W, MID2, X2, MID2)

ax.text(6.0, 41.6,
        "four interactive task types  ·  wrong answers are never punished: "
        "after two misses the answer and its explanation are shown",
        ha="left", va="top", fontsize=9.4, color=SUB)

# ──────────────────────────────────────────────────────────── Premack framing
ax.text(6.0, 37.6,
        "Premack (1959): a higher-probability behaviour can\n"
        "reinforce a lower-probability one. Screen entertainment is\n"
        "the highest-probability behaviour available to a contemporary\n"
        "child; structured reasoning practice is among the lowest.",
        ha="left", va="top", fontsize=10.0, color=SUB, linespacing=1.55)

ax.text(6.0, 28.6,
        "None of this is an in-app promise that a clever nine-year-old\n"
        "can negotiate around. The lock and the key are both in the\n"
        "operating system.",
        ha="left", va="top", fontsize=10.0, color=INK, linespacing=1.55,
        fontweight="bold")

# ─────────────────────────────────────────────────────────────────── the loop
ax.text(6.0, 21.4, "THE LOOP  ·  WHAT THE EARNED MINUTES BUY",
        ha="left", va="top", fontsize=12.5, fontweight="bold", color=TEAL)

box(X2, LY, W, LH, "REWARD",
    "on completion the ledger\nis credited:\n\n+20 points  ·  +5 minutes",
    fill=CARD, lw=1.7)
box(X1, LY, W, LH, "THE CHILD SPENDS",
    "chooses to cash in the\nbalance, inside the hours\nthe parent allowed")
box(X0, LY, W, LH, "THE SHIELD LIFTS",
    "ManagedSettings unshields\nthe selected apps for the\nearned interval, then\nre-applies the shield",
    fill=TINT, lw=1.7)

arrow(X2 + W / 2, R2, X2 + W / 2, LY + LH, lw=1.7)   # AI challenge -> reward
arrow(X2, MIDL, X1 + W, MIDL, lw=1.7)                # reward -> spends
arrow(X1, MIDL, X0 + W, MIDL, lw=1.7)                # spends -> shield

# the shield lifts, the balance runs out, and the next lesson starts
line(X0, MIDL, 1.6, MIDL, lw=1.7)
line(1.6, MIDL, 1.6, MID1, lw=1.7)
arrow(1.6, MID1, X0, MID1, lw=1.7)

ax.text(3.0, 32.0, "the balance runs out", ha="center", va="center",
        fontsize=9.4, color=SUB, rotation=90)

fig.text(0.012, 0.004,
         "Reward values are those of the current build.   Figure: own work (Python).",
         fontsize=9.0, color=SUB, ha="left", va="bottom")

OUT = "/Users/patrik/logiclabposter/posterimages/08_lesson_reward_loop.png"
fig.savefig(OUT, dpi=400, transparent=True)
print("saved", OUT, "| font:", FONT)
