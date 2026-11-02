🇩🇪 [Deutsche Version](README.md)

# Stairwell light → Home Assistant (Shelly 1 Mini Gen3)

The stairwell light is driven by a **Finder 14.01** staircase timer in the distribution board. It should also be
switchable from Home Assistant (e.g. via motion sensors, or when the doorbell rings in the evening), and HA should
show whether the light is on. The Finder **stays**; a **Shelly 1 Mini Gen3** just briefly "presses the button" in
parallel to the existing push buttons. If the Shelly fails, buttons and timer keep working as before.

> **🟡 Status 2026-11-02: planning, enclosure ready to print.** Shelly (in stock) and coupling relay (ordered).
> **Open:** read the Finder mode (must be **BE** or **BP**), check that the buttons switch the phase (4-wire
> connection), installation, HA integration.

| | |
|---|---|
| Device | Shelly 1 Mini Gen3 (terminals SW · O · I · L · N), same type as the [door opener](https://github.com/Sparxx947/shelly-tueroeffner) |
| Trigger | contact **I → O** in parallel to the stairwell buttons: I on the button phase (L), O to **Finder terminal 3** |
| Pulse | auto-off **0.7 s** (below 5 s, otherwise the Finder enters service mode ME/MP = 60 min permanent light) |
| "Light on" feedback | **coupling relay** 230 V (ABB ESB20-11N-06): coil between Finder terminal 4 and N, NO contact L → **SW**; SW set to "detached" |
| Shelly supply | L/N from the "stairwell" circuit breaker |
| Finder 14.01 | mode **BE** (retriggerable) or **BP** (with switch-off warning) – **not IT/IP**, otherwise a second pulse switches a burning light OFF |
| Enclosure | 3D-printed DIN-rail enclosure, 2 modules – [docs/gehaeuse.en.md](docs/gehaeuse.en.md) |
| Firmware | stock Shelly, local, cloud off |

## Principle

```
CB "stairwell" ── L ──┬── Finder 14.01 L ── terminal 4 ──► lamps
                      │        terminal 3 ◄──┬── buttons GF / 1F / 2F (switch L)
                      │                      └── Shelly O   (I = L)  ← additional "button"
                      └── Shelly L                    terminal 4 ──► coupling relay coil ── N
                                                                     NO contact: L ──► Shelly SW
```

Why the coupling relay? Connecting SW directly to terminal 4 lets the leakage current of the Shelly input make LED
lamps glow when off (forum reports, not measured here).

## Safety

- **All terminals carry 230 V.** Work only de-energised (breaker off, verify absence of voltage). If in doubt: a
  qualified electrician.
- Printed PETG is **not** flame-retardant – see [fire safety](docs/gehaeuse.en.md#fire-safety--an-honest-assessment).
- After installation: measure terminal 4 against N in the OFF state (does the coupling relay release reliably?).

## Contents

| Path | Content |
|---|---|
| [docs/gehaeuse.en.md](docs/gehaeuse.en.md) | DIN-rail enclosure: design, differences to the door opener, checks, printing, fire safety |
| `gehaeuse/` | OpenSCAD source, STL (body, lid), ready 3MF for Bambu Lab P1S, view |

## License

MIT – see [LICENSE](LICENSE).
