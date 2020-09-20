import matplotlib.pyplot as plt


def show_squares():
    """Shows square nos. in a graph"""

    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    plt.plot(input_values, squares, linewidth=5)

    # Set chart title and label axes.
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)

    # Set size of tick labels.
    plt.tick_params(axis='both', labelsize=14)

    plt.show()


def show_scatter_squares():
    """Plots a single point of interest"""

    x_values = list(range(1, 1001))
    y_values = [x**2 for x in x_values]

    plt.scatter(x_values, y_values,
                c=y_values, cmap=plt.cm.Blues,
                edgecolors='none', s=40)

    # Set chart title and label axes.
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)

    # Set size of tick labels.
    plt.tick_params(axis='both', which='major', labelsize=14)

    # Set the range for each axes.
    plt.axis([0, 1100, 0, 1100000])

    plt.show()
