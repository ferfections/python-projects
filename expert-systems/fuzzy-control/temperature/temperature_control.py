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
temp_variation = np.arange(-15, 15, 0.01)

# States:
temp_very_cold = fuzz.trapmf(temp_universe, [0, 0, 10, 15])
temp_cold = fuzz.trimf(temp_universe, [10, 15, 20])
temp_normal = fuzz.trimf(temp_universe, [15, 20, 25])
temp_hot = fuzz.trimf(temp_universe, [20, 25, 30])
temp_very_hot = fuzz.trapmf(temp_universe, [25, 30, 40, 40])

humd_very_low = fuzz.trapmf(humd_univers, [0, 0, 10, 20])
humd_low = fuzz.trimf(humd_univers, [10, 25, 40])
humd_normal = fuzz.trimf(humd_univers, [30, 40, 50])
humd_high = fuzz.trimf(humd_univers, [40, 55, 70])
humd_very_high = fuzz.trapmf(humd_univers, [60, 70, 100, 100])

var_big_descent = fuzz.trimf(temp_variation, [-15, -10, -7.5])
var_normal_descent = fuzz.trimf(temp_variation, [-10, -5, -2.5])
var_small_descent = fuzz.trimf(temp_variation, [-7.5, -3.75, 0])
var_stay = fuzz.trimf(temp_variation, [-3.75, 0, 3.75])
var_small_augment = fuzz.trimf(temp_variation, [0, 3.75, 7.5])
var_normal_augment = fuzz.trimf(temp_variation, [2.5, 5, 10])
var_big_augment = fuzz.trimf(temp_variation, [7.5, 10, 15])


def showTemperaturePlot():
    fig, ax = plt.subplots(nrows=1, figsize=(8, 3))

    ax.plot(temp_universe, temp_very_cold, 'b', linewidth=1.5, label='Very Cold')
    ax.plot(temp_universe, temp_cold, 'y', linewidth=1.5, label='Cold')
    ax.plot(temp_universe, temp_normal, 'g', linewidth=1.5, label='Normal')
    ax.plot(temp_universe, temp_hot, 'r', linewidth=1.5, label='Hot')
    ax.plot(temp_universe, temp_hot, 'purple', linewidth=1.5, label='Very Hot')

    ax.set_title('Belonging Functions for Temperature')
    ax.legend()
    ax.grid(True)
    plt.show()

def showHumidityPlot():
    fig, ax = plt.subplots(nrows=1, figsize=(8, 3))

    ax.plot(humd_univers, humd_very_low, 'b', linewidth=1.5, label='Very Low')
    ax.plot(humd_univers, humd_low, 'y', linewidth=1.5, label='Low')
    ax.plot(humd_univers, humd_normal, 'g', linewidth=1.5, label='Normal')
    ax.plot(humd_univers, humd_high, 'r', linewidth=1.5, label='High')
    ax.plot(humd_univers, humd_very_high, 'purple', linewidth=1.5, label='Very High')

    ax.set_title('Belonging Functions for Humidity')
    ax.legend()
    ax.grid(True)
    plt.show()

def input_fuzzyfication():
    actual_temp = 21.5



def main():
    showTemperaturePlot()
    showHumidityPlot()

if __name__ == "__main__":
    main()