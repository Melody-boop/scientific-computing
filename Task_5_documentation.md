# Task 5: Matrix Algebra and Matrix Operations

## 1. Introduction

Matrix algebra is an important concept in scientific computing. A matrix is a rectangular arrangement of numbers in rows and columns. Matrices are used to represent data and perform mathematical operations in applications such as computer graphics, machine learning, robotics, cryptography, and solving systems of equations.

This task uses Python and NumPy to perform matrix-vector multiplication, matrix addition, determinant calculation, and matrix inversion. It also demonstrates a practical application of matrices in computer graphics.

## 2. Tools and Requirements

- **Programming language:** Python
- **Library:** NumPy
- **Software:** Visual Studio Code and a Python environment

NumPy provides functions for efficient numerical calculations and matrix operations.

## 3. Matrix Operations

The program initially defines matrix A and vector x as follows:

\[
A=\begin{bmatrix}1&2\\3&4\end{bmatrix},
\qquad
x=\begin{bmatrix}5\\6\end{bmatrix}
\]

It also defines matrix B:

\[
B=\begin{bmatrix}2&1\\1&2\end{bmatrix}
\]

### 3.1 Matrix-vector multiplication

The program multiplies matrix A by vector x using the `@` operator.

\[
Ax=\begin{bmatrix}
1(5)+2(6)\\
3(5)+4(6)
\end{bmatrix}
=\begin{bmatrix}17\\39\end{bmatrix}
\]

**Output:** `[17 39]`

The result shows how each row of the matrix combines with the vector to produce a new vector.

### 3.2 Matrix addition

The program adds matrices A and B by adding their corresponding elements.

\[
A+B=\begin{bmatrix}3&3\\4&6\end{bmatrix}
\]

**Output:**
```text
[[3 3]
 [4 6]]
```

The addition is possible because both matrices have the same dimensions.

### 3.3 Determinant

The determinant of a 2 × 2 matrix is calculated using:

\[
\det(A)=ad-bc
\]

For the original matrix:

\[
\det(A)=(1\times4)-(2\times3)=-2
\]

**Output:** `-2.00`

Since the determinant is nonzero, matrix A is invertible.

### 3.4 Matrix inverse

The inverse of a matrix is a matrix that produces the identity matrix when multiplied by the original matrix.

For the original matrix, NumPy returns:

```text
[[-2.   1. ]
 [ 1.5 -0.5]]
```

This result represents the inverse of matrix A.

## 4. Experiment: Changing an Input Value

To investigate how an input affects the results, the element `4` in the second row of matrix A was changed to `5`.

The modified matrix became:

\[
A=\begin{bmatrix}1&2\\3&5\end{bmatrix}
\]

The vector and matrix B remained unchanged.

### 4.1 Results after the change

**Matrix-vector multiplication:**

```text
[17 45]
```

The second result increased from 39 to 45 because the second row of the matrix changed.

**Matrix addition:**

```text
[[3 3]
 [4 7]]
```

The bottom-right element increased from 6 to 7, reflecting the change in matrix A.

**Determinant:**

\[
\det(A)=(1\times5)-(2\times3)=-1
\]

The determinant changed from −2 to −1. It remained nonzero, meaning the modified matrix was still invertible.

**Inverse:**

```text
[[-5.  2.]
 [ 3. -1.]]
```

The inverse changed because the entries of the matrix and its determinant changed.

### 4.2 Interpretation

Changing one matrix element affected the multiplication result, matrix sum, determinant, and inverse. This demonstrates that matrix operations depend on the values of the matrix elements. The experiment also shows that a matrix can remain invertible even when its determinant changes, provided the determinant is not zero.

## 5. Real-World Application: Transforming Shapes in Computer Graphics

### 5.1 Problem description

Computer graphics applications use matrix operations to resize and rotate objects. This program models a square using four coordinate points, scales the square by a factor of two, and rotates it 90 degrees counterclockwise about the origin.

### 5.2 Input data and assumptions

The square is represented using the following points:

\[
P=\begin{bmatrix}
1&2&2&1\\
1&1&2&2
\end{bmatrix}
\]

Each column represents one point: (1,1), (2,1), (2,2), and (1,2).

The program assumes that:

- The object is a two-dimensional square.
- The scaling factor is 2 in both directions.
- The rotation angle is 90 degrees counterclockwise.
- The transformation takes place around the origin.
- No translation is applied.

### 5.3 Transformation matrices

The scaling matrix is:

\[
S=\begin{bmatrix}2&0\\0&2\end{bmatrix}
\]

The rotation matrix is:

\[
R=\begin{bmatrix}0&-1\\1&0\end{bmatrix}
\]

The combined transformation matrix is obtained by multiplying the rotation matrix by the scaling matrix:

\[
T=RS=\begin{bmatrix}0&-2\\2&0\end{bmatrix}
\]

The transformed coordinates are calculated using:

\[
P'=TP
\]

### 5.4 Output

**Original square coordinates:**

```text
[[1 2 2 1]
 [1 1 2 2]]
```

**Combined transformation matrix:**

```text
[[ 0 -2]
 [ 2  0]]
```

**Transformed square coordinates:**

```text
[[-2 -2 -4 -4]
 [ 2  4  4  2]]
```

### 5.5 Interpretation

The output shows that the square's coordinates were successfully scaled and rotated. The horizontal coordinates became negative because the rotation moved the square to the left side of the coordinate plane. The transformed points demonstrate how a single matrix multiplication can apply a transformation to multiple coordinates simultaneously.

This approach is useful in computer graphics, animation, game development, and other applications that require objects to be resized or rotated.

## 6. Conclusion

This task demonstrated how Python and NumPy can be used to perform matrix-vector multiplication, matrix addition, determinant calculation, and matrix inversion. Changing an element of a matrix affected the results of the operations, confirming the importance of input values in numerical computations.

The computer graphics adaptation further demonstrated how scaling and rotation matrices can be combined to transform an object's coordinates. Overall, matrix algebra provides an efficient mathematical foundation for solving scientific computing problems and implementing practical transformations.