# Cellular Automata

A collection of Python visualization tools for cellular automata, built with [py5](https://py5coding.org/).

To learn more about the theory behind these patterns, check out [The Nature of Code](https://natureofcode.com/cellular-automata/) and the [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/cellular-automata/supplement.html).

---

## 1D Cellular Automata Generator

A visualization tool for 1-Dimensional Cellular Automata based on Wolfram's elementary rules. Each rule number (0–255) encodes a different binary lookup table that determines how each cell evolves from one row to the next, producing everything from simple repetitive patterns to complex, seemingly random behaviour. Read more on [Wolfram MathWorld](https://mathworld.wolfram.com/ElementaryCellularAutomaton.html).


### Design Philosophy: High-Resolution Export

This tool is specifically built with physical printing in mind. While the real-time window renders at a standard 350 x 495 resolution to maintain smooth performance, the script utilizes a hidden `Py5Graphics` buffer.

This background canvas mirrors the main display at a much higher density (4x scale factor). When you save an image, the final PNG export is 1400 x 1980 pixels. This ensures that the discrete, pixel-art geometry of the cellular automata remains razor-sharp and professional when scaled up for physical media, completely avoiding blurriness.


### Interesting Rules

Some rules produce particularly striking or complex patterns worth exploring:

| Group | Rules |
|-------|-------|
| 1 | 18, 22, 26, 30, 45 |
| 2 | 60, 73, 75, 82, 89 |
| 3 | 90, 101, 102, 110, 124 |
| 4 | 126, 129, 135, 137, 146 |
| 5 | 149, 150, 153, 154, 161 |
| 6 | 165, 167, 169, 181, 182 |
| 7 | 193, 195, 210, 218, 225 |

---

## Conway's Game of Life

A visualization of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) — a 2D cellular automaton devised by mathematician John Horton Conway in 1970. Unlike the 1D automaton above, the grid evolves based on the state of each cell's eight neighbours simultaneously, producing emergent behaviour like stable structures, oscillators, and gliders from a random initial state. Read more on [LifeWiki](https://conwaylife.com/wiki/Main_Page).

The grid uses a **toroidal topology** — cells wrap around all four edges, so no population is ever lost off-screen.


### Design Philosophy

The simulation runs on a 350 x 495 grid (close to A4 ratio) with a cell size of 2px, giving a 175 x 247 cell grid. A `Py5Graphics` buffer at 2x scale is used for high-resolution PNG exports, keeping the saved output crisp at 700 x 990 pixels.

---

## How to Run
For 1D Cellular Automata:

```bash
python src/d1.py
```
Upon running, the terminal will prompt you for two inputs:

- **Rule Number:** Choose a rule between 0 and 255 (defaults to 30).
- **Scrolling:** Enter `y` or `n` to dictate whether the generation should scroll indefinitely or stop at the bottom of the screen.



For Game of Life:

```bash
python src/gol.py
```
The grid initialises with a random distribution of live and dead cells. No inputs are required — it runs immediately.

---

## Controls
While the Py5 window is active, you can use the following keyboard controls:

For 1D Cellular Automata:

| Key | Action |
|-----|--------|
| `Spacebar` | Pause / Resume the generation |
| `S` | Save a high-resolution snapshot to your project folder (saved as `rule_[num]_[generation].png`) |
| `Esc` | Stop and close the sketch |

For Game of Life:

| Key | Action |
|-----|--------|
| `Spacebar` | Pause / Resume the simulation |
| `S` | Save a high-resolution snapshot (saved as `conway_gen_[generation].png`) |
| `Esc` | Stop and close the sketch |

---

## Installation & Setup

It is recommended to run this project inside a Python virtual environment to manage dependencies. Follow these steps to get it running on your local machine:

**1. Clone the repository and navigate to it:**
```bash
git clone https://github.com/geotsant/CellularAutomata.git
cd CellularAutomata
```

**2. Create a virtual environment:**
```bash
python -m venv .venv
```

**3. Activate the virtual environment:**

Mac/Linux:
```bash
source .venv/bin/activate
```

Windows:
```bash
.venv\Scripts\activate
```

**4. Install the required libraries:**
```bash
pip install -r requirements.txt
```

---

## Troubleshooting

### Virtual Environment Activation (Linux/Bash)
If you are using a strict Bash setup (`set -u`) and the activation command fails, use the following instead:
```bash
set +u; source .venv/bin/activate; set -u
```

### Dependency Issues (Arch Linux)
If py5 fails to find a Java Runtime, ensure you have the OpenJDK installed:

```bash
sudo pacman -S jre-openjdk
```
