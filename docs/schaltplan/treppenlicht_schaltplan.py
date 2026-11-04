import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

fig = plt.figure(figsize=(11.69, 8.27))  # A4 quer
ax = fig.add_axes((0, 0, 1, 1)); ax.set_xlim(0, 297); ax.set_ylim(0, 210); ax.axis("off")

L, N, O3, K4, SW = "#8b4513", "#1f5fa8", "#000000", "#7f7f7f", "#c0392b"

def box(x, y, w, h, titel, fc, ec, fs=11):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.6", fc=fc, ec=ec, lw=1.8))
    ax.text(x + w / 2, y + h - 3, titel, ha="center", va="top", fontsize=fs, weight="bold")

def kl(x, y, name, rechts=False, fs=11):
    ax.add_patch(Circle((x, y), 1.9, fc="white", ec="#333", lw=1.3, zorder=5))
    ax.text(x + (3.5 if rechts else -3.5), y, name, ha="left" if rechts else "right", va="center",
            fontsize=fs, weight="bold", zorder=6)

def ln(pts, c, lw=3.0, ls="-"):
    xs, ys = zip(*pts); ax.plot(xs, ys, color=c, lw=lw, ls=ls, solid_capstyle="round", zorder=2)

ax.text(148.5, 202, "Treppenlicht – Shelly + Koppelrelais anschließen", ha="center", fontsize=19, weight="bold")
ax.text(148.5, 194.5, "Finder 14.01 bleibt · Shelly 1 Mini Gen3 als zusätzlicher Taster · ABB ESB20-11N meldet „Licht brennt“ · Stand 04.11.2026 (Klemmen vom Gerät)",
        ha="center", fontsize=10, color="#444")

# Sammelschienen L / N links
ln([(14, 180), (14, 25)], L, 4); ax.text(14, 183, "L", ha="center", fontsize=14, weight="bold", color=L)
ln([(24, 180), (24, 25)], N, 4); ax.text(24, 183, "N", ha="center", fontsize=14, weight="bold", color=N)
ax.text(19, 19, "vom LS\n„Treppenhaus“", ha="center", fontsize=9, va="top")

# Finder
box(55, 120, 58, 58, "Finder 14.01\n(vorhanden)", "#f2f2f2", "#333")
kl(59, 160, "", rechts=True); ax.text(63, 160, "L", fontsize=11, weight="bold", va="center")
kl(59, 148, "", rechts=True); ax.text(63, 148, "N", fontsize=11, weight="bold", va="center")
kl(109, 160, "3"); kl(109, 136, "4")
ax.text(84, 128, "Taster → 3 · Lampe ← 4", ha="center", fontsize=9, color="#555")
ln([(14, 160), (57.1, 160)], L, 2.2); ln([(24, 148), (57.1, 148)], N, 2.2)

# Taster (vorhanden)
ax.add_patch(FancyBboxPatch((128, 168), 30, 14, boxstyle="round,pad=0.5", fc="#f7f7f7", ec="#777", lw=1.2))
ax.text(143, 175, "Taster\n(vorhanden)", ha="center", va="center", fontsize=9)
ln([(110.9, 160), (122, 160), (122, 175), (127.4, 175)], O3, 2.0)
ln([(158.6, 175), (166, 175), (166, 186), (14, 186), (14, 180)], L, 2.0)

# Lampen
ax.add_patch(FancyBboxPatch((128, 128), 30, 14, boxstyle="round,pad=0.5", fc="#fffbe6", ec="#c9a227", lw=1.2))
ax.text(143, 135, "Lampen\n(vorhanden)", ha="center", va="center", fontsize=9)
ln([(110.9, 136), (127.4, 136)], K4, 2.0)

# Shelly
box(55, 30, 70, 70, "Shelly 1 Mini Gen3\n„Treppenlicht“", "#e8f1fb", "#1f5fa8")
for y, n in [(78, "L"), (68, "N")]:
    kl(59, y, "", rechts=True); ax.text(63, y, n, fontsize=11, weight="bold", va="center")
kl(59, 48, "", rechts=True); ax.text(63, 48, "SW", fontsize=11, weight="bold", va="center")
kl(121, 78, "I"); kl(121, 64, "O")
ax.text(90, 37, "I–O = potentialfrei, Impuls 0,7 s\nSW = „Licht brennt“ (detached)", ha="center", fontsize=8.5, color="#1f5fa8")
ln([(14, 78), (57.1, 78)], L, 3.2); ln([(24, 68), (57.1, 68)], N, 3.2)
ax.text(36, 81, "NEU", fontsize=9, weight="bold", color=L)
# I an L
ln([(122.9, 78), (134, 78)], L, 3.2)
ax.text(135.5, 78, "L", fontsize=12, weight="bold", color=L, va="center")
ax.text(128, 85, "NEU: I → L", fontsize=9.5, weight="bold", color=L, ha="center")
# O an Klemme 3
ln([(122.9, 64), (150, 64), (150, 106), (117, 106), (117, 160), (110.9, 160)], O3, 3.2)
ax.text(152, 72, "NEU: O → Finder 3\n(parallel zum Taster)", fontsize=10, weight="bold", color=O3, va="center")

# Koppelrelais
box(185, 30, 70, 90, "Koppelrelais\nABB ESB20-11N", "#fdf2e9", "#b9770e")
kl(189, 102, "", rechts=True); ax.text(193, 102, "A1", fontsize=11, weight="bold", va="center")
kl(189, 90, "", rechts=True); ax.text(193, 90, "A2", fontsize=11, weight="bold", va="center")
kl(251, 70, "1"); kl(251, 56, "2")
kl(251, 42, "R4  (frei)"); kl(189, 42, "", rechts=True); ax.text(193, 42, "R3 (frei)", fontsize=10, va="center")
ax.text(220, 80, "Spule A1–A2\nSchließer 1–2\nÖffner R3–R4 (frei)", ha="center", fontsize=9, color="#b9770e")
# A1 an Klemme 4
ln([(110.9, 136), (118, 136), (118, 125), (172, 125), (172, 102), (187.1, 102)], K4, 3.2)
ax.text(150, 128, "NEU: Finder 4 → A1", fontsize=10, weight="bold", color="#555")
# A2 an N
ln([(187.1, 90), (178, 90)], N, 3.2)
ax.text(176.5, 90, "N", fontsize=12, weight="bold", color=N, va="center", ha="right")
ax.text(170, 95, "NEU: A2 → N", fontsize=9.5, weight="bold", color=N, ha="center")
# 13 an L, 14 an SW
ln([(252.9, 70), (264, 70)], L, 3.2)
ax.text(265.5, 70, "L", fontsize=12, weight="bold", color=L, va="center")
ax.text(272, 76, "NEU: 1 → L", fontsize=9.5, weight="bold", color=L, ha="center")
ln([(252.9, 56), (272, 56), (272, 12), (44, 12), (44, 48), (57.1, 48)], SW, 3.2)
ax.text(160, 14.5, "NEU: 2 → Shelly SW", fontsize=10, weight="bold", color=SW)

# Hinweise rechts oben
ax.add_patch(FancyBboxPatch((180, 128), 112, 58, boxstyle="round,pad=0.6", fc="#fff3cd", ec="#c9a227", lw=1.5))
ax.text(183, 183, "⚠ VORHER", fontsize=11, weight="bold", va="top")
ax.text(183, 176.5,
        "1. LS „Treppenhaus“ AUS, Spannungsfreiheit prüfen.\n"
        "2. ABB laut Aufdruck (Foto 04.11.): A1 oben, A2 unten,\n"
        "    1–2 = Schließer, R3–R4 = Öffner (bleibt frei).\n"
        "3. Finder-Drehschalter auf BE oder BP (nicht IT/IP),\n"
        "    sonst schaltet ein Impuls brennendes Licht AUS.\n"
        "4. Prüfen: Taster legt L auf Klemme 3 (4-Leiter)?\n"
        "    Wenn der Taster N schaltet → STOPP, Plan passt nicht.",
        fontsize=8.8, va="top", linespacing=1.35)

ax.add_patch(FancyBboxPatch((180, 2), 112, 6, boxstyle="round,pad=0.6", fc="#e8f6e8", ec="#2e7d32", lw=1.2))
ax.text(183, 5, "DANACH: Taster → Licht + „brennt“ an · HA-Impuls → Licht · Licht aus → „brennt“ aus",
        fontsize=7.2, va="center")
ax.text(8, 5, "dicke Linie = neu · dünne Linie = vorhanden · „L“/„N“ = an L bzw. N vom LS Treppenhaus", fontsize=8.5, color="#444", va="center")

import os
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "treppenlicht_schaltplan")
fig.savefig(out + ".pdf"); fig.savefig(out + ".png", dpi=110)
print(out + ".pdf")
