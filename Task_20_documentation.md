# Task 20: Random Numbers and Monte Carlo Methods

## 1. Introduction
Monte Carlo methods use random sampling to estimate numerical values or probabilities that may be difficult to calculate directly. By running many simulations, it is possible to approximate mathematical constants and analyze uncertain real-world situations.

This task uses Monte Carlo simulation to estimate the value of pi and then applies the method to estimate the probability of on-time deliveries.

## 2. Objectives
- Generate random numbers using NumPy.
- Estimate the value of pi through random sampling.
- Calculate the error between the estimated and actual values.
- Apply Monte Carlo simulation to estimate delivery reliability.
- Visualize the simulation results using Matplotlib.

## 3. Methodology

### 3.1 Estimating Pi
Random points are generated uniformly within a unit square, where both coordinates range from 0 to 1. Points satisfying the condition below fall inside a quarter-circle of radius 1:

\[
x^2+y^2\leq1
\]

The value of pi is estimated using:

\[
\pi\approx4\frac{N_{\text{inside}}}{N_{\text{total}}}
\]

Where:
- \(N_{\text{inside}}\) is the number of points inside the quarter-circle.
- \(N_{\text{total}}\) is the total number of random points generated.

### 3.2 Delivery Reliability Simulation
The adapted program simulates 10,000 delivery times using a normal distribution with a mean of 25 minutes and a standard deviation of 5 minutes. Negative simulated delivery times are replaced with zero.

A delivery is considered on time if it takes 30 minutes or less. The estimated probability is calculated as:

\[
P(\text{on time})\approx
\frac{\text{Number of on-time deliveries}}
{\text{Total simulated deliveries}}
\]

NumPy was used for random number generation and calculations, while Matplotlib was used to visualize the results.

## 4. Original Problem: Estimating Pi

The original simulation generated 10,000 random points using a fixed random seed to make the results reproducible.

### Results
- Total points: **10,000**
- Points inside the quarter-circle: **7,889**
- Estimated pi: **3.155600**
- Actual pi: **3.141593**
- Absolute error: **0.014007**
- Graph saved as `Task_20_monte_carlo.png`.

The estimated value is close to the actual value of pi. The difference occurs because the estimate depends on the random points sampled. Increasing the number of points may improve accuracy, although convergence is not guaranteed to be strictly monotonic with every increase.

## 5. Real-World Adaptation: Delivery Reliability

The adapted simulation models delivery times for a service with an assumed average delivery time of 25 minutes and a standard deviation of 5 minutes. A delivery deadline of 30 minutes is used.

### Results
- Total simulated deliveries: **10,000**
- Average simulated delivery time: **24.99 minutes**
- Deliveries within 30 minutes: **8,407**
- Deliveries exceeding 30 minutes: **1,593**
- Estimated on-time delivery probability: **0.8407**
- Estimated on-time delivery percentage: **84.07%**
- Graph saved as `Task_20_real_world_adaptation.png`.

The simulation estimates that approximately 84.07% of deliveries arrive within the 30-minute deadline under the chosen assumptions. The remaining 15.93% exceed the deadline.

## 6. Discussion
The original simulation demonstrates how Monte Carlo methods can approximate a mathematical constant through random sampling. The delivery adaptation demonstrates how the same approach can estimate the probability of an event in a practical scenario.

Using a fixed random seed makes the simulation reproducible. However, the results remain estimates based on a simulated model rather than observations of actual deliveries.

## 7. Limitations
The accuracy of Monte Carlo estimates depends on the number of simulations and the sampling method. The delivery model assumes a normal distribution with a fixed mean and standard deviation, which may not accurately represent real delivery times. Factors such as traffic, weather, distance, and demand are not included.

Actual delivery data would be needed to validate the model and determine whether its assumptions are realistic.

## 8. Conclusion
Monte Carlo simulation was successfully used to estimate pi and model delivery reliability. The first simulation estimated pi as 3.155600, while the adapted simulation estimated that 84.07% of deliveries would arrive within 30 minutes under the specified assumptions. The task demonstrates how random sampling can support numerical estimation and practical decision-making under uncertainty.