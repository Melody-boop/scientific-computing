# Task 10: Root Finding — Bisection and Fixed-Point Methods

## 1. Introduction

Root-finding methods are numerical techniques used to find values of a variable that make a mathematical function equal to zero. This task implements the bisection and fixed-point iteration methods to estimate equilibrium temperatures in a heat-balance model.

## 2. Mathematical Concepts

### Bisection Method

The bisection method finds a root within an interval where the function has opposite signs at the two endpoints. The interval is repeatedly divided into two halves until the root is approximated to the required accuracy.

### Fixed-Point Iteration

Fixed-point iteration rewrites an equation in the form \(x=g(x)\). Starting with an initial estimate, the method repeatedly calculates new values until successive estimates differ by less than a specified tolerance.

## 3. Main Problem

The heat-balance function is defined as:

\[
f(T)=T-25-10e^{-T/20}
\]

The equilibrium temperature is found by solving \(f(T)=0\).

The bisection method uses the interval \([20,40]\), while fixed-point iteration uses:

\[
T=25+10e^{-T/20}
\]

The stopping tolerance is \(10^{-10}\).

### Results

- Bisection equilibrium temperature: **27.525211°C**
- Fixed-point equilibrium temperature: **27.525211°C**
- Fixed-point iterations: **13**
- The graph is saved as `Task_10_equilibrium_temperature.png`.

Both methods produced the same temperature to six decimal places, demonstrating agreement between the numerical approaches.

## 4. Real-World Adaptation

The second program models a simplified room-heating system. Heat supplied decreases exponentially as the room temperature increases, while heat loss increases with temperature.

The heat-balance function is:

\[
f(T)=(T-20)-12e^{-T/25}
\]

The corresponding fixed-point equation is:

\[
T=20+12e^{-T/25}
\]

The bisection method uses the interval \([20,40]\), and fixed-point iteration starts at \(25^\circ C\).

### Real-World Results

- Bisection equilibrium room temperature: **24.503163°C**
- Fixed-point equilibrium room temperature: **24.503163°C**
- Fixed-point iterations: **15**
- The graph is saved as `Task_10_real_world_adaptation.png`.

The agreement between the methods supports the numerical result for this simplified model. In a real building, additional factors such as insulation, ventilation, room size, and external temperature would need to be considered.

## 5. Applications

Root-finding methods are useful in:

- Engineering calculations and thermal equilibrium analysis.
- Finding business break-even points.
- Estimating unknown interest rates in financial models.
- Calibrating scientific instruments.
- Determining thresholds in mathematical and computational models.

## 6. Conclusion

This task demonstrated how the bisection and fixed-point iteration methods can be used to solve nonlinear equations. Both methods produced matching equilibrium-temperature estimates for the main problem and the real-world adaptation. The results illustrate the usefulness of numerical methods when exact analytical solutions are difficult to obtain.
