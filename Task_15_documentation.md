# Task 15: Numerical Differentiation

## 1. Objective
The objective of this task is to estimate the rate of change of position using numerical differentiation. The task demonstrates how finite-difference methods can estimate the speed of a moving vehicle from recorded GPS positions.

## 2. Mathematical Concept
Numerical differentiation approximates the derivative of a function using discrete data points.

The main methods are:

**Forward Difference**

\[
f'(x)\approx\frac{f(x+h)-f(x)}{h}
\]

**Central Difference**

\[
f'(x)\approx\frac{f(x+h)-f(x-h)}{2h}
\]

**Backward Difference**

\[
f'(x)\approx\frac{f(x)-f(x-h)}{h}
\]

Central differences are generally more accurate for interior data points, while forward and backward differences are useful at the beginning and end of a dataset.

## 3. Original Problem: Vehicle Speed Estimation
The original program estimates a vehicle's speed from GPS position readings recorded at one-second intervals. Numerical differentiation is applied to approximate the instantaneous speed at each recorded time.

### Results

| Time (s) | Position (m) | Estimated Speed (m/s) |
|---:|---:|---:|
| 0 | 0.0 | 4.80 |
| 1 | 4.8 | 5.10 |
| 2 | 10.2 | 5.65 |
| 3 | 16.1 | 6.25 |
| 4 | 22.7 | 6.95 |
| 5 | 30.0 | 7.65 |
| 6 | 38.0 | 8.00 |

The results show that the estimated speed generally increases over time, indicating that the vehicle is accelerating.

The program also generates a graph showing the relationship between time and estimated speed.

## 4. Real-World Adaptation: Delivery Motorcycle Speed Analysis
The original problem was adapted to estimate the speed of a delivery motorcycle using GPS readings recorded every two seconds.

The program uses a forward difference at the first point, central differences at the interior points, and a backward difference at the final point.

### Results

| Time (s) | Position (m) | Estimated Speed (m/s) |
|---:|---:|---:|
| 0 | 0.0 | 3.50 |
| 2 | 7.0 | 4.25 |
| 4 | 17.0 | 5.75 |
| 6 | 30.0 | 7.25 |
| 8 | 46.0 | 8.75 |
| 10 | 65.0 | 10.25 |
| 12 | 87.0 | 11.00 |

The results indicate that the motorcycle's estimated speed increases from 3.50 m/s to 11.00 m/s over the 12-second observation period. This suggests that the motorcycle is accelerating.

The generated graph, `Task_15_real_world_adaptation.png`, illustrates the change in estimated speed over time.

## 5. Applications
Numerical differentiation has several practical applications, including:

- Estimating vehicle speed from GPS position data.
- Calculating acceleration from velocity measurements.
- Measuring rates of change in scientific experiments.
- Analysing sensor data and monitoring system performance.
- Studying gradients and sensitivity in numerical models.

## 6. Limitations
Numerical differentiation provides an approximation rather than an exact derivative. Its accuracy depends on the spacing and quality of the recorded data. GPS measurement errors and irregular sampling can affect the estimated speed.

## 7. Conclusion
This task demonstrates how numerical differentiation can estimate speed from discrete position measurements. The original vehicle example and the delivery motorcycle adaptation show how finite-difference methods can be applied to real-world motion analysis. These techniques are useful in transportation, navigation, engineering, and other applications involving changing quantities.
