import py5
import random

grid = []
cols, rows = 0, 0
cell_size = 2
scale_factor = 2
generation = 0
is_paused = False


def settings():
    py5.size(350, 495)  # almost A4 ratio


def setup():
    global grid, cols, rows
    py5.background(255)
    py5.no_stroke()

    cols = py5.width // cell_size
    rows = py5.height // cell_size

    grid = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]


def draw():
    global grid, generation

    if is_paused:
        return

    py5.background(255)
    py5.fill(0)

    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == 1:
                py5.rect(x * cell_size, y * cell_size, cell_size, cell_size)

    grid = generate_next(grid)
    generation += 1


def generate_next(current_grid):
    next_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for y in range(rows):
        for x in range(cols):
            # Count live neighbors in a 3x3 area
            neighbors = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    # Skip the cell itself
                    if i == 0 and j == 0:
                        continue

                    # Wrap around the edges (toroidal array)
                    col = (x + i + cols) % cols
                    row = (y + j + rows) % rows
                    neighbors += current_grid[row][col]

            state = current_grid[y][x]

            # Apply Conway's Rules
            if state == 1 and (neighbors == 2 or neighbors == 3):
                # Any live cell with two or three live neighbours survives
                next_grid[y][x] = 1
            elif state == 0 and neighbors == 3:
                # Any dead cell with exactly three live neighbours becomes a live cell
                next_grid[y][x] = 1
            else:
                # All other live cells die in the next generation. Similarly, all other dead cells stay dead.
                next_grid[y][x] = 0

    return next_grid


def key_pressed():
    global is_paused

    if py5.key == " ":
        is_paused = not is_paused

    if py5.key == "s" or py5.key == "S":
        save_high_res()


def save_high_res():
    # Build the high-res buffer on demand to prevent frame rate drops
    print(f"Generating high-res snapshot for generation {generation}...")

    high_res = py5.create_graphics(py5.width * scale_factor, py5.height * scale_factor)
    high_res.begin_draw()
    high_res.background(255)
    high_res.no_stroke()
    high_res.fill(0)

    # Scale and draw the current grid state
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == 1:
                high_res.rect(
                    x * cell_size * scale_factor,
                    y * cell_size * scale_factor,
                    cell_size * scale_factor,
                    cell_size * scale_factor,
                )
    high_res.end_draw()

    filename = f"conway_gen_{generation}.png"
    high_res.save(filename)
    print(f"PNG saved: {filename}")


if __name__ == "__main__":
    py5.run_sketch()
