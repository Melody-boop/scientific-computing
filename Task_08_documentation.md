# Task 8: Iterative Methods for Linear Systems

## 1. Introduction

This task implements two numerical methods for solving systems of linear equations: the Jacobi method and the Gauss-Seidel method. The methods are applied to a simplified temperature-distribution problem. Their results are compared with the direct solution calculated using NumPy.

## 2. Mathematical Model

The system represents five interior points between two boundaries with fixed temperatures. The left boundary is maintained at 100°C, while the right boundary is initially set at 20°C.

The system is expressed as:

\[
Ax=b
\]

where \(A\) is the coefficient matrix, \(x\) contains the unknown interior temperatures, and \(b\) represents the boundary conditions.

## 3. Methods Used

### Jacobi Method

The Jacobi method calculates new values using the values from the previous iteration. It continues until the maximum change between successive approximations is less than the specified tolerance.

### Gauss-Seidel Method

The Gauss-Seidel method updates the solution one variable at a time and uses newly calculated values immediately within the same iteration. This can improve convergence speed.

### Direct Solution

The NumPy function `numpy.linalg.solve()` calculates a direct solution, which is used to check the accuracy of the iterative methods.

## 4. Original Results

With boundary temperatures of 100°C and 20°C, the approximate interior temperatures were:

- Point 1: 86.67°C
- Point 2: 73.33°C
- Point 3: 60.00°C
- Point 4: 46.67°C
- Point 5: 33.33°C

Jacobi converged in 150 iterations, while Gauss-Seidel converged in 75 iterations. Both methods produced results very close to the direct solution.

## 5. Input-Change Experiment

The right boundary temperature was changed from 20°C to 30°C, while the left boundary remained at 100°C.

The new approximate interior temperatures were:

- Point 1: 88.33°C
- Point 2: 76.67°C
- Point 3: 65.00°C
- Point 4: 53.33°C
- Point 5: 41.67°C

Jacobi converged in 150 iterations, while Gauss-Seidel converged in 76 iterations.

The increase in the right boundary temperature caused all five interior temperatures to increase. The results continued to agree closely with the direct solution.

## 6. Convergence Graph

The program generates a graph comparing the maximum change between successive iterations for Jacobi and Gauss-Seidel. The graph is saved as `Task_08_convergence.png`.

The graph helps compare how quickly the methods approach their final solutions. The number of iterations also shows that Gauss-Seidel converged in fewer iterations for this particular system.

## 7. Real-World Adaptation

The file `Task_08_real_world_adaptation.py` applies the Gauss-Seidel method to estimate temperatures at five points across a simplified room or enclosed space with different boundary temperatures.

### Assumptions

- The temperature distribution has reached a steady state.
- Heat transfer is represented using a simplified one-dimensional model.
- The boundary temperatures remain constant.
- Other factors, such as airflow, insulation differences, and additional heat sources, are not explicitly modelled.

### Results

For boundary temperatures of 100°C and 30°C, the program estimated temperatures of 88.33°C, 76.67°C, 65.00°C, 53.33°C, and 41.67°C. The method converged in 76 iterations.

### Interpretation

The model demonstrates how numerical methods can estimate unknown temperatures between boundaries. A more realistic room-temperature model would require additional physical assumptions and measurements.

## 8. Conclusion

Both Jacobi and Gauss-Seidel successfully solved the linear system and produced results close to the direct solution. In the experiments performed, Gauss-Seidel required fewer iterations than Jacobi. Changing the boundary temperature affected the entire interior temperature distribution. The real-world adaptation demonstrated how iterative methods can be applied to a simplified heat-distribution problem.