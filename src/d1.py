import py5

rule = []
cells = []
cell_size = 1
generation = 0
is_scrolling = True
scale_factor = 4
num = 0
high_res = None


val = input("What rule to use (0-255)? ")
num = int(val) if val.isdigit() else 30  # default rule = 30
rule_str = format(num, "08b")
rule_list = [int(b) for b in rule_str]
scrolling = input("Do you want scrolling? : y/n ")


def settings():
    py5.size(350, 495)  # almost A4 ratiio


def setup():
    global cells, high_res
    py5.background(255)
    py5.no_stroke()

    high_res = py5.create_graphics(py5.width * scale_factor, py5.height * scale_factor)
    high_res.no_smooth()
    high_res.begin_draw()
    high_res.background(255)
    high_res.no_stroke()
    high_res.end_draw()

    cols = py5.width // cell_size
    cells = [0] * cols
    cells[cols // 2] = 1


def draw():
    global cells, generation
    if not is_scrolling or high_res is None:
        return

    y = generation * cell_size

    if scrolling == "y":
        if y >= py5.height:
            py5.copy(
                0,
                cell_size,
                py5.width,
                py5.height - cell_size,
                0,
                0,
                py5.width,
                py5.height - cell_size,
            )

            py5.fill(255)
            py5.rect(0, py5.height - cell_size, py5.width, cell_size)

            y = py5.height - cell_size
        else:
            generation += 1

        render_row_dual(cells, y)

        cells = generate_next(cells)
    else:
        if y < py5.height:
            render_row_dual(cells, y)
            cells = generate_next(cells)
            generation += 1


def render_row_dual(row_cells, y_pos):
    """Renders a single generation row to both the display window and the high-resolution buffer.

    This function iterates through the state of each cell in the current row. If a cell
    is active (1), it draws a corresponding rectangle on the standard Py5 canvas and
    a scaled version on the hidden high-resolution Py5Graphics buffer for export.

    Args:
        row_cells (list[int]): A list of integers representing the binary state (0 or 1)
            of each cell in the current generation.
        y_pos (int): The vertical coordinate (row index) where the cells should
            be rendered on the canvas.

    Returns:
        None: The function performs drawing operations and does not return a value.
    """
    if high_res is None:
        return

    """
    here we draw on the screen
    """
    py5.fill(0)
    for i, state in enumerate(row_cells):
        if state == 1:
            py5.rect(i * cell_size, y_pos, cell_size, cell_size)

    """
    here we draw on the high-res buffer
    """
    high_res.begin_draw()
    high_res.fill(0)
    for i, state in enumerate(row_cells):
        if state == 1:
            high_res.rect(
                i * cell_size * scale_factor,
                y_pos * scale_factor,
                cell_size * scale_factor,
                cell_size * scale_factor,
            )
    high_res.end_draw()


def generate_next(current_cells):
    """
    Calculates the next state of the grid based on Conway's Rules.

    Args:
        current_grid (list): A 2D list representing the current generation.

    Returns:
        list: The 2D grid for the subsequent generation.
    """
    n = len(current_cells)
    next_gen = [0] * n

    for i in range(n):
        left = current_cells[(i - 1) % n]
        me = current_cells[i]
        right = current_cells[(i + 1) % n]

        # Binary to decimal
        index = 7 - (left * 4 + me * 2 + right * 1)
        next_gen[i] = rule_list[index]

    return next_gen


def key_pressed():
    global is_scrolling
    if py5.key == " ":
        is_scrolling = not is_scrolling

    if (py5.key == "s" or py5.key == "S") and high_res is not None:
        if not is_scrolling or (generation * cell_size >= py5.height):
            filename = f"rule_{num}_{generation}.png"
            high_res.save(filename)
            print(f"PNG saved: {filename}")


if __name__ == "__main__":
    py5.run_sketch()
