# Task 17: Numerical Solution of Ordinary Differential Equations Using Euler's Method

## 1. Introduction
Euler's method is a numerical technique used to approximate solutions to ordinary differential equations (ODEs). It estimates the next value of a dependent variable using its current value and rate of change. This task applies Euler's method to model the cooling of an object and a hot meal during delivery.

## 2. Objectives
- Implement Euler's method to solve a first-order ordinary differential equation.
- Calculate temperature changes over time.
- Plot temperature against time.
- Apply the method to a practical food-delivery scenario.

## 3. Methodology
Newton's law of cooling describes how an object's temperature approaches the surrounding temperature over time.

The differential equation is:

\[
\frac{dT}{dt}=-k(T-T_a)
\]

Where:
- \(T\) is the object's temperature.
- \(T_a\) is the ambient temperature.
- \(k\) is the cooling constant.
- \(t\) is time.

Euler's method uses the formula:

\[
T_{n+1}=T_n+h[-k(T_n-T_a)]
\]

Where \(h\) is the time-step size. Python, NumPy, and Matplotlib were used to perform the calculations and plot the results.

## 4. Original Problem: Object Cooling

The original program models an object cooling from an initial temperature of 90°C towards an ambient temperature of 25°C. Euler's method is applied using one-minute time steps over 20 minutes.

### Results

- Initial temperature: 90.00°C
- Temperature after 20 minutes: 27.52°C
- The generated graph is saved as `Task_17_euler_method.png`.

Selected temperature readings:

| Time (minutes) | Temperature (°C) |
|---:|---:|
| 0 | 90.00 |
| 5 | 53.84 |
| 10 | 37.80 |
| 15 | 30.68 |
| 20 | 27.52 |

The results show that the object's temperature decreases over time and gradually approaches the ambient temperature.

## 5. Real-World Adaptation: Food Cooling During Delivery

The adapted program models a hot meal cooling inside a delivery container. The meal starts at 85°C and cools towards an ambient temperature of 24°C. A cooling constant of 0.08 per minute and a one-minute time step are used over a 30-minute period.

### Results

- Initial meal temperature: 85.00°C
- Temperature after 30 minutes: 29.00°C
- The generated graph is saved as `Task_17_real_world_adaptation.png`.

Selected temperature readings:

| Time (minutes) | Temperature (°C) |
|---:|---:|
| 0 | 85.00 |
| 5 | 64.20 |
| 10 | 50.50 |
| 15 | 41.46 |
| 20 | 35.51 |
| 25 | 31.59 |
| 30 | 29.00 |

The results indicate that the meal loses heat rapidly at first, then cools more slowly as its temperature approaches the surrounding temperature. This model can help illustrate how temperature changes during food delivery.

## 6. Discussion
Both programs demonstrate how Euler's method approximates solutions to differential equations. In both cases, the temperature decreases over time because the object's temperature is initially higher than the ambient temperature.

The real-world adaptation demonstrates a practical application in food delivery, where understanding temperature changes can help inform delivery duration and food-storage decisions.

## 7. Limitations
Euler's method is an approximation, so its accuracy depends on the selected time-step size. Larger time steps can produce greater numerical error. The cooling model also assumes a constant ambient temperature and cooling constant, which may not reflect changing weather, container insulation, food properties, or other real delivery conditions.

The predicted temperature alone does not establish whether food is safe to eat; food safety requires appropriate handling and temperature monitoring.

## 8. Conclusion
Euler's method was successfully implemented to model object cooling and adapted to simulate a hot meal cooling during delivery. The results show how numerical methods can be applied to practical problems involving temperature change. The exercise also demonstrates the usefulness of graphical representations in interpreting numerical solutions.