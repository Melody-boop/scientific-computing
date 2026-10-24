
import numpy as np

# ==========================================
# PART 1: ORIGINAL WEATHER STATION PROGRAM
# ==========================================

temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])

mean_temp = np.mean(temperatures_c)
min_temp = np.min(temperatures_c)
max_temp = np.max(temperatures_c)

temperatures_f = 1.8 * temperatures_c + 32

print("PART 1: ORIGINAL RESULTS")
print(f"Daily mean: {mean_temp:.2f} C")
print(f"Minimum: {min_temp:.2f} C")
print(f"Maximum: {max_temp:.2f} C")
print("First six Fahrenheit readings:", temperatures_f[:6])


# ==========================================
# PART 2: EXPERIMENT - CHANGE ONE INPUT
# ==========================================

modified_temperatures_c = temperatures_c.copy()
modified_temperatures_c[0] = 28.5

new_mean_temp = np.mean(modified_temperatures_c)

print("\nPART 2: EXPERIMENT RESULTS")
print(f"Original mean: {mean_temp:.2f} C")
print(f"New mean: {new_mean_temp:.2f} C")
print(f"Change in mean: {new_mean_temp - mean_temp:.2f} C")


# Real-world application: Daily household electricity consumption

# Assumption: These are eight electricity readings in kWh
# recorded at different times during a day.
electricity_kwh = np.array([
    1.2, 0.8, 1.5, 2.1, 1.8, 2.4, 1.1, 1.6
])

# Calculate electricity consumption statistics
mean_usage = np.mean(electricity_kwh)
minimum_usage = np.min(electricity_kwh)
maximum_usage = np.max(electricity_kwh)

# Assumption: Electricity costs KSh 25 per kWh.
tariff = 25
total_usage = np.sum(electricity_kwh)
estimated_cost = total_usage * tariff

print("\n--- Household Electricity Analysis ---")
print(f"Average reading: {mean_usage:.2f} kWh")
print(f"Minimum reading: {minimum_usage:.2f} kWh")
print(f"Maximum reading: {maximum_usage:.2f} kWh")
print(f"Total recorded consumption: {total_usage:.2f} kWh")
print(f"Estimated electricity cost: KSh {estimated_cost:.2f}")

