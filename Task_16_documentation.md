# Task 16: Numerical Integration

## 1. Objective
The objective of this task is to estimate accumulated quantities using numerical integration. The program compares the trapezoidal rule and Simpson's rule to estimate electrical energy consumption from power measurements taken at regular time intervals.

## 2. Mathematical Concept
Numerical integration approximates the area under a curve. When power is measured over time, integrating power gives the energy consumed.

The trapezoidal rule approximates the area using trapezoids, while Simpson's rule approximates the curve using parabolic segments.

Energy is calculated using:

Energy = ∫ Power × time interval

Since power is measured in kilowatts and time in hours, the resulting energy is measured in kilowatt-hours (kWh).

## 3. Original Problem: Smart-Meter Energy Consumption
The original program uses power readings recorded every two hours over a 12-hour period.

### Results
- Energy using the trapezoidal rule: **15.700 kWh**
- Energy using Simpson's rule: **15.800 kWh**
- Difference between estimates: **0.100 kWh**

The results show that both methods produce similar estimates of energy consumption. The small difference illustrates how different numerical integration techniques can approximate the same accumulated quantity.

## 4. Real-World Adaptation: Household Electricity Consumption
The program was adapted to estimate energy consumption in a household using a different set of power readings taken every two hours over 12 hours.

### Results
- Energy using the trapezoidal rule: **12.100 kWh**
- Energy using Simpson's rule: **12.200 kWh**
- Difference between estimates: **0.100 kWh**

The household's estimated energy consumption is approximately **12.1–12.2 kWh** over the observation period. The graph saved as `Task_16_real_world_adaptation.png` shows how power consumption changes with time.

## 5. Interpretation
Both methods estimate the total energy consumed by accumulating power measurements over time. Simpson's rule produces an estimate 0.1 kWh higher than the trapezoidal rule in both examples. This difference results from the different ways the methods approximate the area under the power-time curve.

## 6. Applications
Numerical integration is useful for:
- Calculating electricity consumption from smart-meter data.
- Estimating distance travelled from velocity measurements.
- Calculating total fluid flow.
- Analysing signal energy.
- Estimating accumulated quantities in engineering and scientific experiments.

## 7. Limitations
The estimates depend on the frequency and accuracy of the measurements. Changes in power between recorded readings may not be fully captured, and numerical integration provides an approximation of actual energy consumption.

## 8. Conclusion
This task demonstrates how the trapezoidal and Simpson's rules can estimate energy consumption from power readings. The household adaptation produced estimates of 12.100 kWh and 12.200 kWh, showing that the two methods gave similar results for the supplied data. Numerical integration is useful for estimating accumulated quantities when measurements are available at discrete time intervals.
