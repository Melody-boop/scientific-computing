
# Task 13: Interpolation

## Objective
To estimate values between known data points using linear interpolation and cubic spline interpolation with SciPy.

## Method
The program uses hourly temperature measurements and the `interp1d` and `CubicSpline` functions from `scipy.interpolate`. It estimates temperatures at 10-minute intervals and compares the two interpolation methods using graphs.

## Original Problem
Hourly temperature measurements were provided from 8:00 AM to 2:00 PM.

- Linear estimate at 10:30 AM: 23.25°C
- Cubic spline estimate at 10:30 AM: 23.36°C

## Real-World Application
The adapted program models greenhouse temperature sensor readings from 6:00 AM to 12:00 PM. It estimates intermediate temperatures to help monitor conditions between hourly measurements.

- Linear estimate at 8:30 AM: 21.50°C
- Cubic spline estimate at 8:30 AM: 21.46°C

## Results
Both methods estimate intermediate temperatures from recorded measurements. Linear interpolation connects adjacent data points with straight lines, while cubic spline interpolation uses smooth cubic curves. Their estimates can differ slightly.

## Applications
- Temperature sensor monitoring
- Estimating missing measurements
- Sensor calibration
- Engineering and scientific data analysis

## Conclusion
Interpolation provides a practical way to estimate values between measured data points. SciPy makes it possible to implement and compare linear and cubic spline interpolation efficiently.
