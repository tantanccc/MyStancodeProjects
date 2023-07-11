"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    width = CANVAS_WIDTH
    space = (width - GRAPH_MARGIN_SIZE * 2) / len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + space * year_index

    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       fill="black", width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, fill="black", width=LINE_WIDTH)
    for year_index in range(len(YEARS)):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, year_index)
        canvas.create_line(x_coordinate, 0, x_coordinate, CANVAS_HEIGHT, fill='black', width=LINE_WIDTH)
        canvas.create_text(x_coordinate + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[year_index],
                           fill="black", anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #

    color_index = 0
    for name in lookup_names:
        color = COLORS[color_index % len(COLORS)]
        for year_index in range(len(YEARS)-1):
            width = CANVAS_WIDTH

            # year 1 (start point of a line in an interval)
            year_index_1 = year_index
            year_1 = str(YEARS[year_index])
            if year_1 not in name_data[name]:
                rank_1_text = '*'
                rank_1 = 1000
            else:
                rank_1_text = rank_1 = int(name_data[name][year_1])

            # year 2 (end point of a line in an interval)
            year_index_2 = year_index + 1
            year_2 = str(YEARS[year_index + 1])
            if year_2 not in name_data[name]:
                rank_2_text = '*'
                rank_2 = 1000
            else:
                rank_2_text = rank_2 = int(name_data[name][year_2])
                # rank_2 = int(name_data[name][year_2])

            # first calculate the interval of each rank
            y_interval = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / 1000

            # year 1 coordinates
            x_coordinate_1 = get_x_coordinate(width, year_index_1)
            y_coordinate_1 = GRAPH_MARGIN_SIZE + y_interval * rank_1
            # year 2 coordinates
            x_coordinate_2 = get_x_coordinate(width, year_index_2)
            y_coordinate_2 = GRAPH_MARGIN_SIZE + y_interval * rank_2

            # check color within the COLORS
            if color_index >= len(COLORS):
                color_index = color_index - len(COLORS)

            canvas.create_line(x_coordinate_1, y_coordinate_1, x_coordinate_2, y_coordinate_2, fill=color,
                               width=LINE_WIDTH)

            if year_index_2 == len(YEARS)-1:   # for the last point
                canvas.create_text(x_coordinate_1 + TEXT_DX, y_coordinate_1, text=f'{name} {rank_1_text}',
                                   fill=color, anchor=tkinter.SW)
                canvas.create_text(x_coordinate_2 + TEXT_DX, y_coordinate_2, text=f'{name} {rank_2_text}',
                               fill=color, anchor=tkinter.SW)
            else:      # for other points
                canvas.create_text(x_coordinate_1 + TEXT_DX, y_coordinate_1, text=f'{name} {rank_1_text}',
                                   fill=color, anchor=tkinter.SW)

            # change color for the next name
            color_index += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
