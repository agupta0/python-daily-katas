"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


# Define the 'preparation_time_in_minutes()' function below.
# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preperation time based on the number of layers 

    :param number_of_layers: int - how many laters you are cooking
    :return: int - preperation bake time (in minutes) derived from 'PREPERATION_TIME'.

    Function that takes the number of layers in the lasagna as
    an argument and returns how many minutes the lasagna needs to be prepapred
    based on the `PREPARATION_TIME`.
    """
    return PREPARATION_TIME * number_of_layers



#define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time during making the lasanga 

    :param number_of_layers: int - how many laters you are cooking
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - elapsed bake time (in minutes).

    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
