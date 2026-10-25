# Task 6: Solution of Systems of Linear Equations

## 1. Introduction

This task demonstrates how Python and NumPy can be used to solve systems of linear equations. The program uses the `numpy.linalg.solve()` function to determine unknown values from known inputs. It also verifies the solution using matrix multiplication and calculates the residual to check the accuracy of the results.

## 2. Mathematical Concept

A system of linear equations can be represented in matrix form as:

**Ax = b**

Where:
- **A** is the coefficient matrix containing the known coefficients.
- **x** is the vector of unknown values.
- **b** is the vector containing the known results.

The program uses `np.linalg.solve(A, b)` to calculate the unknown values. It then uses `A @ solution` to verify the solution and `b - A @ solution` to calculate the residual.

## 3. Original Problem: Server Resource Allocation

The original problem involves two types of servers with different resource requirements.

- Type A uses 4 CPU units and 8 GB of memory.
- Type B uses 2 CPU units and 12 GB of memory.
- Total CPU usage is 20 units.
- Total memory usage is 72 GB.

Let **x** represent the number of Type A servers and **y** represent the number of Type B servers.

The equations are:

4x + 2y = 20

8x + 12y = 72

The program represents these equations using a NumPy coefficient matrix and a vector of known resource totals.

### Original Results

- Type A servers: 3
- Type B servers: 4
- Verified resource totals: 20 CPU units and 72 GB of memory
- Residual norm: 0.0

The results show that three Type A servers and four Type B servers satisfy both resource equations.

## 4. Changing an Input Parameter

To observe how changing an input affects the solution, the total CPU requirement was increased from 20 to 24 units, while the memory requirement remained at 72 GB.

The input vector was changed from:

`b = np.array([20.0, 72.0])`

to:

`b = np.array([24.0, 72.0])`

### Results After the Change

- Type A servers: 4
- Type B servers: 3
- Verified resource totals: 24 CPU units and 72 GB of memory
- Residual norm: 0.0

The change increased the number of Type A servers from three to four and reduced the number of Type B servers from four to three. This demonstrates how changing an input parameter affects the solution while the memory requirement remains constant.

## 5. Real-World Adaptation: Campus Event Ticket Sales

The second program applies systems of linear equations to a campus event ticket-sales problem.

The assumptions are:

- Adult tickets cost KSh 500 each.
- Student tickets cost KSh 300 each.
- A total of 40 tickets were sold.
- Total ticket revenue was KSh 15,600.
- All tickets sold were either adult or student tickets, and the stated revenue came entirely from these sales.

Let **x** represent the number of adult tickets sold and **y** represent the number of student tickets sold.

The equations are:

x + y = 40

500x + 300y = 15,600

The first equation represents the total number of tickets sold. The second represents the total revenue collected.

The program uses `np.linalg.solve()` to determine the number of tickets sold in each category.

### Results

- Adult tickets sold: 18
- Student tickets sold: 22
- Verified ticket count: 40
- Verified revenue: KSh 15,600
- Residual norm: 0.0

### Interpretation

The results indicate that 18 adult tickets and 22 student tickets were sold.

Adult ticket revenue was 18 × KSh 500 = KSh 9,000, while student ticket revenue was 22 × KSh 300 = KSh 6,600. The combined revenue was KSh 15,600, matching the given total.

This demonstrates how systems of linear equations can help event organizers estimate unknown quantities when the total number of items and total revenue are known.

## 6. Conclusion

This task demonstrated how NumPy can solve systems of linear equations using matrix operations. The original server allocation program showed how resource requirements can be used to determine unknown server quantities. Changing the CPU requirement produced a different solution, demonstrating the effect of changing an input parameter.

The ticket-sales adaptation applied the same mathematical method to a different real-world problem. In both programs, matrix multiplication confirmed the calculated results, and a residual norm of zero indicated that the computed solutions satisfied the given equations.

The task illustrates the usefulness of linear algebra in resource allocation, planning, and solving practical problems involving multiple unknown quantities.