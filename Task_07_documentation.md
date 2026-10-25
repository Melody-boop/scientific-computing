# TASK 7: GAUSSIAN ELIMINATION AND LU DECOMPOSITION

## 1. Introduction

Gaussian elimination and LU decomposition are numerical methods used to solve systems of linear equations of the form \(Ax=b\).

Gaussian elimination transforms a system into an upper-triangular form, which can then be solved using back-substitution. LU decomposition expresses a coefficient matrix as the product of a lower-triangular matrix and an upper-triangular matrix. When the same coefficient matrix is used with different measurement vectors, its LU factorization can be calculated once and reused, making the process more efficient.

This task demonstrates how LU decomposition can solve several systems that share the same coefficient matrix.

## 2. Inputs and Mathematical Operations

The coefficient matrix used in the program is:

\[
A=\begin{bmatrix}
4 & -1 & 0\\
-1 & 4 & -1\\
0 & -1 & 3
\end{bmatrix}
\]

The program uses three measurement vectors:

\[
b_1=\begin{bmatrix}15\\10\\10\end{bmatrix},\quad
b_2=\begin{bmatrix}16\\11\\9\end{bmatrix},\quad
b_3=\begin{bmatrix}14\\12\\11\end{bmatrix}
\]

The mathematical operation is to solve \(Ax=b\) for the unknown vector \(x\). The program uses SciPy's `lu_factor()` function to factorize the coefficient matrix and `lu_solve()` to calculate a solution for each measurement vector. It also calculates the residual, \(r=b-Ax\), and its norm to check the accuracy of the solution.

## 3. Original Program Results

The original program produced the following results:

| Measurement set | Calculated solution |
|---|---|
| 1 | [5.0000, 5.0000, 5.0000] |
| 2 | [5.3171, 5.2683, 4.7561] |
| 3 | [4.9024, 5.6098, 5.5366] |

The residual norms were `0.0`, approximately `1.78 × 10⁻¹⁵`, and `0.0`, respectively.

The direct solution calculated using `numpy.linalg.solve()` for the first measurement set was also `[5.0, 5.0, 5.0]`. This agrees with the LU decomposition result and provides a comparison confirming that the solution is correct.

## 4. Changing an Input Parameter

To investigate how changing an input affects the output, the second measurement vector was modified from:

`[16.0, 11.0, 9.0]`

to:

`[18.0, 11.0, 9.0]`

Only the first value of the second measurement vector was changed. The coefficient matrix and the other measurement vectors remained the same.

The modified program produced these results:

| Measurement set | Original solution | Modified solution |
|---|---|---|
| 1 | [5.0000, 5.0000, 5.0000] | [5.0000, 5.0000, 5.0000] |
| 2 | [5.3171, 5.2683, 4.7561] | [5.8537, 5.4146, 4.8049] |
| 3 | [4.9024, 5.6098, 5.5366] | [4.9024, 5.6098, 5.5366] |

The change affected only the solution for measurement set 2. The first and third solutions remained unchanged because their inputs were not modified. The residual norm for the modified second measurement set was approximately `1.78 × 10⁻¹⁵`, which is effectively zero.

This demonstrates that the solution depends on the measurement vector, even when the coefficient matrix remains fixed.

## 5. Real-World Adaptation: Simplified Electricity Network Model

### Problem description

The program was adapted to represent a simplified electricity-network model involving three nodes. The unknown values represent voltage-related quantities at the nodes, while the coefficient matrix represents fixed relationships within the network.

The model receives different measurement vectors while retaining the same coefficient matrix. This represents a situation where a system's underlying relationships remain constant but its measured inputs change.

### Assumptions

- The network is represented by a system of three linear equations.
- The coefficient matrix remains constant for all measurement sets.
- Each measurement vector represents a different set of network measurements.
- The model is illustrative and does not represent a complete electrical engineering simulation.
- The calculated values are interpreted as voltage-related quantities, without assigning a specific physical unit.

### Inputs

The coefficient matrix is:

\[
A=\begin{bmatrix}
4 & -1 & 0\\
-1 & 4 & -1\\
0 & -1 & 3
\end{bmatrix}
\]

The measurement vectors are:

\[
b_1=\begin{bmatrix}12\\8\\6\end{bmatrix},\quad
b_2=\begin{bmatrix}14\\9\\7\end{bmatrix},\quad
b_3=\begin{bmatrix}10\\7\\8\end{bmatrix}
\]

### Mathematical operations

The program factorizes the coefficient matrix once using LU decomposition. It then solves the three systems using the corresponding measurement vectors. For each solution, it calculates \(Ax\) and compares it with the original measurement vector. It also calculates the residual norm to assess numerical accuracy.

### Results

| Measurement set | Calculated node values | Residual norm |
|---|---|---|
| 1 | [3.9512, 3.8049, 3.2683] | 0.0 |
| 2 | [4.5854, 4.3415, 3.7805] | ≈ 1.78 × 10⁻¹⁵ |
| 3 | [3.3902, 3.5610, 3.8537] | 0.0 |

The verification step reproduced the original measurement vectors:

- Set 1: `[12.0, 8.0, 6.0]`
- Set 2: `[14.0, 9.0, 7.0]`
- Set 3: `[10.0, 7.0, 8.0]`

### Interpretation

The results show that different measurement vectors produce different calculated node values even though the coefficient matrix remains unchanged. The verification results agree with the original inputs, while the residual norms are zero or extremely close to zero. This indicates that the numerical solutions satisfy the modeled equations to within floating-point precision.

The adaptation illustrates why LU decomposition is useful in repeated calculations: the coefficient matrix only needs to be factorized once, and the resulting factorization can be reused for each new measurement vector.

## 6. Conclusion

The task demonstrated how systems of linear equations can be solved using LU decomposition and how a factorization can be reused when the coefficient matrix remains constant. Changing one input in the second measurement vector changed its calculated solution without affecting the other measurement sets. The direct-solution comparison, verification calculations, and residual norms supported the accuracy of the results.

The simplified electricity-network model further demonstrated how the same method can be applied to a related real-world scenario involving repeated measurements. Overall, LU decomposition provides an efficient approach to solving multiple systems that share the same coefficient matrix.
