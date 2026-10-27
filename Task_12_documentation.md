# Task 12: Polynomial and Nonlinear Equation Solving

## 1. Introduction

Polynomial and nonlinear equation solving involves finding unknown values that satisfy mathematical equations. Numerical methods are useful when equations are difficult to solve analytically.

This task uses Python and SciPy's `root()` function to find the intersection points of a circle and a parabola. A real-world adaptation changes the circle's radius and the parabola's shape to represent different boundary conditions.

## 2. Mathematical Concept

A polynomial equation can be expressed as:

\[
a_nx^n+\cdots+a_1x+a_0=0
\]

A nonlinear system consists of equations that are not all linear in the unknown variables. Numerical solvers estimate values that make the equations' residuals approach zero.

For this task, the original equations are:

Circle:

\[
x^2+y^2=4
\]

Parabola:

\[
y=x^2-1
\]

The system is rewritten as residual equations:

\[
f_1(x,y)=x^2+y^2-4=0
\]

\[
f_2(x,y)=y-(x^2-1)=0
\]

## 3. Original Program

The Python program imports NumPy and `root` from `scipy.optimize`. It defines both equations as residuals and uses two different initial guesses to find intersection points.

### Original Results

| Initial guess | x-coordinate | y-coordinate |
|---|---:|---:|
| [1.0, 1.0] | 1.517490 | 1.302776 |
| [-1.0, 1.0] | -1.517490 | 1.302776 |

Both runs converged successfully. The residuals were approximately zero, indicating that the calculated points satisfy both equations to numerical precision.

The two intersection points have opposite x-coordinates and equal y-coordinates, showing symmetry about the y-axis.

## 4. Real-World Adaptation

The adapted problem represents the intersection of a circular coverage boundary and a parabolic boundary.

The equations were changed to:

Circle:

\[
x^2+y^2=9
\]

Parabola:

\[
y=0.5x^2-1
\]

The circle's radius increased from 2 to 3 units, while the coefficient of \(x^2\) in the parabola changed from 1 to 0.5, making the parabola wider.

The corresponding residual equations are:

\[
f_1(x,y)=x^2+y^2-9=0
\]

\[
f_2(x,y)=y-(0.5x^2-1)=0
\]

### Adapted Results

| Initial guess | x-coordinate | y-coordinate |
|---|---:|---:|
| [1.0, 2.0] | 2.378414 | 1.828427 |
| [-1.0, 2.0] | -2.378414 | 1.828427 |

Both solutions converged successfully, with residuals extremely close to zero.

## 5. Input Values and Parameters

The original program uses a circle with radius 2 and a parabola defined by \(y=x^2-1\). The adapted program uses a circle with radius 3 and a parabola defined by \(y=0.5x^2-1\).

The initial guesses provide starting estimates for the numerical solver. Using guesses on opposite sides of the y-axis helps identify the two symmetric intersection points.

## 6. Real-World Applications

Nonlinear equation solving can be used in:

- Geometric intersection and computer graphics.
- Radio or wireless coverage modelling.
- Engineering design and structural analysis.
- Chemical equilibrium calculations.
- Calibration and control systems.
- Kinematics and physical modelling.

In a coverage-planning application, intersecting mathematical boundaries can help identify locations where two coverage regions or constraints meet. Actual deployment would require suitable real-world measurements and a model appropriate to the environment.

## 7. Assumptions and Limitations

1. The circle and parabola are ideal mathematical boundaries.
2. The equations are assumed to represent the system accurately.
3. Initial guesses influence which solution a numerical solver finds.
4. Convergence and small residuals are used to verify the calculated solutions.
5. The model does not account for environmental interference, terrain, or measurement uncertainty.

## 8. Conclusion

The original and adapted programs successfully used SciPy's nonlinear root solver to find two intersection points. Both solutions in each scenario were symmetric about the y-axis, and the residuals were close to zero. Changing the circle's radius and the parabola's shape changed the locations of the intersections, demonstrating how numerical methods can solve modified nonlinear systems.
