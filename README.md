🇬🇧 [English version](README.en.md)

# Treppenhauslicht → Home Assistant (Shelly 1 Mini Gen3)

Das Treppenhauslicht hängt an einem **Finder 14.01** (Treppenlichtzeitschalter) im Verteiler. Es soll zusätzlich
aus Home Assistant einschaltbar sein, etwa per Bewegungsmelder oder abends beim Klingeln. HA soll außerdem anzeigen,
ob das Licht gerade brennt. Der Finder **bleibt**. Ein **Shelly 1 Mini Gen3** drückt nur parallel zu den
vorhandenen Tastern kurz „auf den Knopf“. Fällt der Shelly aus, funktionieren Taster und Zeitschalter wie bisher.

> **🟡 Stand 02.11.2026: Planung, Gehäuse druckfertig.** Shelly (Bestand) und Koppelrelais (bestellt) vorhanden
> bzw. unterwegs. **Offen:** Stellung des Finder ablesen (muss **BE** oder **BP** sein), prüfen, ob die Taster
> die Phase schalten (4-Leiter-Anschluss), Einbau, HA-Einbindung.

| | |
|---|---|
| Gerät | Shelly 1 Mini Gen3 (Klemmen SW · O · I · L · N), derselbe Typ wie beim [Türöffner](https://github.com/Sparxx947/shelly-tueroeffner) |
| Auslöser | Kontakt **I → O** parallel zu den Treppenhaus-Tastern: I an der Taster-Phase (L), O an **Finder Klemme 3** |
| Impuls | Auto-Off **0,7 s** (unter 5 s, sonst schaltet der Finder in den Servicemodus ME/MP = 60 min Dauerlicht) |
| Rückmeldung „Licht brennt“ | **Koppelrelais** 230 V (ABB ESB20-11N-06): Spule zwischen Finder Klemme 4 und N, Schließer L → **SW**; SW im Shelly „detached“ |
| Versorgung Shelly | L/N vom Leitungsschutzschalter „Treppenhaus“ |
| Finder 14.01 | Betriebsart **BE** (nachtriggerbar) oder **BP** (mit Ausschaltvorwarnung) – **nicht IT/IP**, sonst schaltet ein zweiter Impuls brennendes Licht AUS |
| Gehäuse | Hutschienengehäuse 2 TE zum Selbstdrucken – [docs/gehaeuse.md](docs/gehaeuse.md) |
| Firmware | Shelly-Original, lokal, Cloud aus (Tasmota: siehe Türöffner-Repo, praktisch nicht möglich) |

## Prinzip

```
LS „Treppenhaus“ ── L ──┬── Finder 14.01 L ── Klemme 4 ──► Lampen
                        │        Klemme 3 ◄──┬── Taster EG / E1 / E2 (schalten L)
                        │                    └── Shelly O   (I = L)  ← zusätzlicher „Taster“
                        └── Shelly L                    Klemme 4 ──► Koppelrelais-Spule ── N
                                                                       Schließer: L ──► Shelly SW
```

Warum der Umweg über das Koppelrelais? Hängt man SW direkt an Klemme 4, lässt der Leckstrom des Shelly-Eingangs
LED-Lampen im ausgeschalteten Zustand glimmen (Erfahrungen aus Foren, hier nicht nachgemessen).

## Sicherheit

- **Hier liegt an allen Klemmen 230 V an.** Arbeiten nur spannungsfrei (LS „Treppenhaus“ aus, Spannungsfreiheit
  messen). Wer das nicht sicher kann: Elektrofachkraft.
- Gedrucktes PETG ist **nicht** flammhemmend – siehe [Brandschutz](docs/gehaeuse.md#brandschutz--ehrlich-eingeordnet).
- Nach dem Einbau: Klemme 4 gegen N im AUS-Zustand messen (fällt das Koppelrelais sicher ab?).

## Inhalt

| Pfad | Inhalt |
|---|---|
| [docs/gehaeuse.md](docs/gehaeuse.md) | Hutschienengehäuse: Aufbau, Unterschiede zum Türöffner, Prüfungen, Druck, Brandschutz |
| `gehaeuse/` | OpenSCAD-Quelle, STL (Körper, Deckel), fertige 3MF für Bambu Lab P1S, Ansicht |

## Lizenz

MIT – siehe [LICENSE](LICENSE).
