# Parameters: 
#   1. Temperature (C) -> range(0.00-40.00)
#   2. Humidity (%) -> range(0.00%-100.00%)

# Return: 
#   Change in temperature (C) -> range(-15.00, +15.00)


import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

temp_universe = np.arange(0, 40, 0.01)
humd_univers = np.arange(0, 100, 0.01)
temp_variation = np.arange()

# States:
temp_very_cold = fuzz.trapmf(temp_universe, [0, 0, 10, 15])
temp_cold = fuzz.trimf(temp_universe, [10, 15, 20])
temp_normal = fuzz.trapmf(temp_universe, [15, 20, 25])
temp_hot = fuzz.trapmf(temp_universe, [20, 25, 30])
temp_very_hot = fuzz.trapmf(temp_universe, [25, 30, 40, 40])

humd_very_low = fuzz.trapmf(humd_univers, [0, 0, 10, 20])
humd_low = fuzz.trapmf(humd_univers, [10, 25, 40])
humd_normal = fuzz.trapmf(humd_univers, [30, 40, 50])
humd_high = fuzz.trapmf(humd_univers, [40, 55, 70])
humd_very_high = fuzz.trapmf(humd_univers, [60, 70, 100, 100])

var_big_descent = fuzz.trapmf(temp_variation, [-15, -10, -7.5])
var_normal_descent = fuzz.trapmf(temp_variation, [-10, -5, -2.5])
var_small_descent = fuzz.trapmf(temp_variation, [-7.5, -3.75, 0])
var_stay = fuzz.trapmf(temp_variation, [-3.75, 0, 3.75])
var_small_augment = fuzz.trapmf(temp_variation, [0, 3.75, 7.5])
var_normal_augment = fuzz.trapmf(temp_variation, [2.5, 5, 10])
var_big_augment = fuzz.trapmf(temp_variation, [7.5, 10, 15])

def fuzzy_input(x: int) -> int:
    return     