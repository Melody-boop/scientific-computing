# Task 2: NumPy Arrays and Numerical Computation

## 1. Objective

The objective of this task is to demonstrate the use of NumPy arrays for numerical computation, statistical analysis, and vectorized operations. The task also investigates how changing an input value affects a calculated result and applies the same concepts to household electricity consumption.

## 2. Original Problem: Weather Temperature Analysis

### Inputs

The program uses an array containing 24 hourly temperature readings measured in degrees Celsius.

### Mathematical Operations

- `np.mean()` calculates the average temperature.
- `np.min()` identifies the minimum temperature.
- `np.max()` identifies the maximum temperature.
- The formula `1.8 * temperatures_c + 32` converts Celsius readings to Fahrenheit using a vectorized operation.
- Array slicing (`temperatures_f[:6]`) selects the first six Fahrenheit readings.

### Results

- Daily mean temperature: 23.12°C
- Minimum temperature: 17.50°C
- Maximum temperature: 29.40°C
- First six Fahrenheit readings: 65.3, 64.4, 64.04, 63.5, 64.22 and 66.2°F.

### Interpretation

The results show that the lowest recorded temperature was 17.50°C, while the highest was 29.40°C. The average temperature was approximately 23.12°C. NumPy made it possible to perform calculations on the entire array without writing a separate loop for each reading.

## 3. Experiment: Effect of Changing an Input

### Parameter Changed

The first temperature reading was increased from 18.5°C to 28.5°C. The remaining 23 readings were kept unchanged. A copy of the original array was used to preserve the initial data.

### Results

- Original mean: 23.12°C
- Modified mean: 23.54°C
- Change in mean: approximately 0.42°C.

### Interpretation

Increasing one reading by 10°C increased the daily mean by approximately 0.42°C. This is because the total sum of the readings increased by 10°C while the number of readings remained 24. The experiment demonstrates that changes in input data can affect statistical results.

## 4. Adapted Real-World Application: Household Electricity Consumption

### Problem Description

NumPy was applied to analyse eight household electricity-consumption readings. The program calculates the average, minimum, maximum and total consumption, then estimates the cost using an assumed electricity tariff.

### Assumptions

- The eight readings represent separate electricity-consumption amounts measured in kilowatt-hours (kWh).
- The readings are suitable for illustrating consumption analysis over a day.
- The electricity tariff is assumed to be KSh 25 per kWh.
- The estimated cost excludes taxes, standing charges and other possible billing adjustments.

### Inputs

The electricity readings are 1.2, 0.8, 1.5, 2.1, 1.8, 2.4, 1.1 and 1.6 kWh.

### Mathematical Operations

- `np.mean()` calculates average consumption per reading.
- `np.min()` identifies the lowest reading.
- `np.max()` identifies the highest reading.
- `np.sum()` calculates total recorded consumption.
- Multiplying the total consumption by the assumed tariff estimates the electricity cost.

### Results

- Average reading: 1.56 kWh
- Minimum reading: 0.80 kWh
- Maximum reading: 2.40 kWh
- Total recorded consumption: 12.50 kWh
- Estimated electricity cost: KSh 312.50.

### Interpretation

The eight readings total 12.50 kWh. At the assumed tariff of KSh 25 per kWh, the estimated cost is KSh 312.50. The minimum and maximum readings help identify periods of relatively low and high consumption. This type of analysis can help households understand their electricity usage and estimate costs.

The calculation is illustrative and does not represent an actual electricity bill.

## 5. Conclusion

This task demonstrated how NumPy arrays simplify numerical computation and statistical analysis. The experiment showed how changing an input value affects the mean, while the electricity-consumption application demonstrated how NumPy can be used to solve a different practical problem. These activities reinforced the importance of selecting appropriate inputs, applying mathematical operations correctly, and interpreting numerical outputs in context.