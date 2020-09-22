import matplotlib.pyplot as plt
import generating_data as mpl
from random_walk import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def run_mpl():
    # mpl.show_squares()
    mpl.show_scatter_squares()


def run_random_walk():
    while True:
        # Make a random walk and plot the points
        rw = RandomWalk(50000)
        rw.fill_walk()

        # Set the size of the plotting window
        plt.figure(dpi=128, figsize=(10, 6))

        point_numbers = list(range(rw.num_points))
        plt.scatter(rw.x_values, rw.y_values,
                    c=point_numbers, cmap=plt.cm.Blues,
                    edgecolors='none', s=1)

        # Emphasize the starting and ending points
        plt.scatter(0, 0, c='green', edgecolors='none', s=100)
        plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

        # Remove the axes
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)

        plt.show()

        keep_running = input("Make another walk? (y/n): ")
        if keep_running == 'n':
            break


if __name__ == '__main__':
    # print_hi('PyCharm')
    # run_mpl()
    run_random_walk()

