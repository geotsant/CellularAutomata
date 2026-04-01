# 1D Cellular Automata Generator

A Python visualization tool for 1-Dimensional Cellular Automata, built with [py5](https://py5coding.org/).

This project explores the mathematical beauty of cellular automata, allowing you to generate, visualize, and export different rule sets in real-time. To learn more about the theory behind these patterns, check out [The Nature of Code](https://natureofcode.com/cellular-automata/) and the [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/cellular-automata/supplement.html).

## Design Philosophy: High-Resolution Export

This tool is specifically built with physical printing in mind. While the real-time window renders at a standard 350 x 495 resolution to maintain smooth performance, the script utilizes a hidden `Py5Graphics` buffer.

This background canvas mirrors the main display at a much higher density (4x scale factor). When you save an image, the final PNG export is 1400 x 1980 pixels. This ensures that the discrete, pixel-art geometry of the cellular automata remains razor-sharp and professional when scaled up for physical media, completely avoiding blurriness.

## Installation & Setup

It is recommended to run this project inside a Python virtual environment to manage dependencies. Follow these steps to get it running on your local machine:

**1. Clone the repository and navigate to it:**
```bash
git clone <your-repository-url>
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
pip install py5
```

## How to Run

Once your virtual environment is active and py5 is installed, run the script from the terminal:
```bash
python src/main.py
```

Upon running, the terminal will prompt you for two inputs:

- **Rule Number:** Choose a rule between 0 and 255 (defaults to 30).
- **Scrolling:** Enter `y` or `n` to dictate whether the generation should scroll indefinitely or stop at the bottom of the screen.

## Interesting Rules

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

## Controls

While the Py5 window is active, you can use the following keyboard controls:

| Key | Action |
|-----|--------|
| `Spacebar` | Pause / Resume the generation |
| `S` | Save a high-resolution snapshot to your project folder (saved as `rule_[num]_[generation].png`) |
