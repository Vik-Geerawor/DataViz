import pygal
from die import *


def run_die():
    # create a D6
    die_1 = Die()
    die_2 = Die()

    # make some rolls, and store results in a list
    results = []
    for roll_num in range(1000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    # analyze the results
    frequencies = []
    max_results = die_1.num_sides + die_2.num_sides
    for value in range(1, max_results+1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # visualize the results
    hist = pygal.Bar()

    hist.title = "Results of rolling two D6 1000 times."
    hist.x_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    hist.x_title = "Results"
    hist.y_title = "Frequency of Result"

    hist.add('D6 + D6', frequencies)
    hist.render_to_file('die_visual.svg')
