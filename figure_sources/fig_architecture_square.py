#!/usr/bin/env python3
"""
FIG 3 — system architecture, re-laid out for the poster_2 figure slot.

The slot is ~539 x 517 px, so the figure is drawn square (10 x 9.6 in)
instead of the old 12 x 6.6 landscape that left 40% of the card empty.
Background is transparent: the poster's own cream shows through, and the
box fills match --cream-light so the diagram reads as part of the card.

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

# palette — matched to the poster tokens, not to the old paper figures
PAPER = "#F7F0DE"       # --cream-light, the figure card behind this
SOFT  = "#F1E7CE"
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


def box(x, y, w, h, title, body="", lw=1.0, title_size=12.5, body_size=10.4,
        fill=PAPER, gap=5.2, zorder=3, tcolor=INK):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=fill, edgecolor=INK,
                           linewidth=lw, zorder=zorder))
    if body:
        ax.text(x + w / 2, y + h - 2.2, title, ha="center", va="top",
                fontsize=title_size, fontweight="bold", color=tcolor,
                zorder=zorder + 1)
        ax.text(x + w / 2, y + h - 2.2 - gap, body, ha="center", va="top",
                fontsize=body_size, color=SUB, linespacing=1.5,
                zorder=zorder + 1)
    else:
        ax.text(x + w / 2, y + h / 2, title, ha="center", va="center",
                fontsize=title_size, fontweight="bold", color=tcolor,
                zorder=zorder + 1)


def arrow(x1, y1, x2, y2, lw=1.3, rad=0.0):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                                 mutation_scale=15, linewidth=lw,
                                 color=INK, zorder=6,
                                 connectionstyle=f"arc3,rad={rad}"))


# ─────────────────────────────────────────────────────────── PARENT (top band)
ax.add_patch(Rectangle((0.5, 87.0), 99, 12.5, facecolor=PAPER,
                       edgecolor=INK, linewidth=1.8, zorder=2))
ax.text(3.0, 97.6, "PARENT", ha="left", va="top",
        fontsize=13, fontweight="bold", color=TEAL, zorder=7)

for x, txt in [
    (26.0, "Grants Family Controls\nauthorization"),
    (54.0, "Selects the restricted apps\nthrough Apple's system picker"),
    (82.0, "Sets the economy once: exchange\nrate, daily cap, allowed hours"),
]:
    ax.text(x, 93.3, txt, ha="center", va="center", fontsize=10.4,
            color=SUB, linespacing=1.55, zorder=7)

# ─────────────────────────────────────────────────────── CHILD DEVICE (left)
ax.add_patch(Rectangle((0.5, 24.0), 60.5, 58.0, facecolor=PAPER,
                       edgecolor=INK, linewidth=1.8, zorder=2))
ax.text(30.75, 80.6, "CHILD DEVICE", ha="center", va="top",
        fontsize=12.5, fontweight="bold", color=TEAL, zorder=7)

box(3.0, 63.0, 55.5, 12.5, "LogicLab Kids client",
    "SwiftUI, MVVM  (iOS, on TestFlight)\n"
    "Kotlin and Jetpack Compose  (Android, in development)",
    fill=SOFT, gap=4.6, title_size=12.5, body_size=10.0)

box(3.0, 40.0, 26.5, 21.5, "Offline lesson engine",
    "6 modules, 36 lessons\nauthored as JSON and\nbundled with the app\n\n"
    "runs with no network",
    title_size=11.6, body_size=10.0)

box(32.0, 40.0, 26.5, 21.5, "Reward ledger",
    "points and earned\nminutes per child\n\n"
    "written on completion,\nsynced to Firestore",
    title_size=11.6, body_size=10.0)

box(3.0, 26.0, 55.5, 12.0, "Parental layer",
    "Per-child credentials created by the parent\n"
    "Role-based Firestore rules: a child reads only their own data",
    fill=SOFT, gap=4.6, title_size=12.0, body_size=10.0)

# ────────────────────────────────────────────────────── GOOGLE CLOUD (right)
ax.add_patch(Rectangle((64.5, 24.0), 35.0, 58.0, facecolor=PAPER,
                       edgecolor=INK, linewidth=1.8, zorder=2))
ax.text(82.0, 80.6, "GOOGLE CLOUD", ha="center", va="top",
        fontsize=12.5, fontweight="bold", color=TEAL, zorder=7)

box(67.0, 63.5, 30.0, 12.0, "Firebase Authentication",
    "parent and child identities", title_size=11.4, body_size=10.0, gap=4.8)
box(67.0, 46.5, 30.0, 13.0, "Cloud Firestore",
    "profiles, lesson progress,\nreward ledger",
    title_size=11.6, body_size=10.0, gap=4.8)
box(67.0, 26.0, 30.0, 15.5, "Gemini",
    "the constrained tutor;\nnever gives the answer",
    title_size=11.6, body_size=10.0, gap=4.8)

# ──────────────────────────────────────────────────────── OS enforcement band
ax.add_patch(Rectangle((0.5, 7.0), 99.0, 12.0, facecolor=TINT,
                       edgecolor=INK, linewidth=1.8, zorder=2))
ax.text(50.0, 17.0, "OPERATING SYSTEM  ·  WHERE THE CONTINGENCY IS ENFORCED",
        ha="center", va="top", fontsize=11.8, fontweight="bold",
        color=TEAL, zorder=7)
ax.text(50.0, 12.4,
        "FamilyControls  ·  ManagedSettings (applies and lifts the shield)  ·  "
        "DeviceActivity (daily cap, allowed windows)",
        ha="center", va="top", fontsize=10.0, color=SUB, zorder=7)

# ─────────────────────────────────────────────────────────────────── arrows
arrow(30.75, 86.8, 30.75, 82.2)                       # parent -> child device
ax.text(32.2, 84.5, "setup", ha="left", va="center", fontsize=9.6, color=SUB)

arrow(58.7, 69.0, 67.0, 68.5)                         # client -> auth
arrow(58.7, 51.0, 67.0, 52.5, rad=0.06)               # ledger -> firestore
arrow(67.0, 33.0, 58.7, 45.0, rad=0.10)               # gemini -> device
arrow(30.75, 23.8, 30.75, 19.2)                       # device -> OS
arrow(82.0, 23.8, 82.0, 19.2)                         # cloud  -> OS

ax.text(32.2, 21.5, "\"unlock the earned minutes\"", ha="left", va="center",
        fontsize=9.6, color=SUB)

ax.text(0.5, 4.6,
        "The picker returns opaque tokens and the shield is applied by the operating system, "
        "not by the app:\nLogicLab Kids never learns which apps the parent chose.",
        ha="left", va="top", fontsize=9.6, color=SUB, linespacing=1.5)
ax.text(0.5, 0.4,
        "Architecture of the shipped build.   Figure: own work (Python).",
        ha="left", va="top", fontsize=9.0, color=SUB)

OUT = "/Users/patrik/logiclabposter/posterimages/07_system_architecture.png"
fig.savefig(OUT, dpi=400, transparent=True)
print("saved", OUT, "| font:", FONT)
