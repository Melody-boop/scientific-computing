# Task 09: Eigenvalues and Eigenvectors

## 1. Mathematical Concept

For a square matrix \(A\), an eigenvector is a non-zero vector \(v\) that satisfies the equation:

\[
Av = \lambda v
\]

Here, \(A\) is a square matrix, \(v\) is an eigenvector, and \(\lambda\) is the corresponding eigenvalue. The eigenvalue describes how the eigenvector is scaled by the matrix transformation.

Eigenvalues and eigenvectors have applications in network analysis, vibration analysis, stability studies, Principal Component Analysis (PCA), and Google's PageRank-related concepts.

## 2. Original Problem: Computer Network

The original program models a small undirected computer network containing four nodes: A, B, C, and D.

### Input Data

The network is represented by an adjacency matrix:

\[
A =
\begin{bmatrix}
0 & 1 & 1 & 0\\
1 & 0 & 1 & 1\\
1 & 1 & 0 & 1\\
0 & 1 & 1 & 0
\end{bmatrix}
\]

A value of 1 represents a connection between two nodes, while 0 indicates no direct connection. The diagonal entries are zero because nodes are not connected to themselves.

### Mathematical Operation

NumPy's `numpy.linalg.eig()` function calculates the eigenvalues and eigenvectors. The program selects the eigenvalue with the largest magnitude and its corresponding eigenvector. The absolute values of the eigenvector components are normalized to produce importance scores whose sum is 1.

### Original Output

- Dominant eigenvalue: 2.5616
- Node A importance: 0.2192
- Node B importance: 0.2808
- Node C importance: 0.2808
- Node D importance: 0.2192
- Verification of \(Av = \lambda v\): True

### Interpretation

Nodes B and C have the highest importance scores in the original network. Nodes A and D have lower scores. This suggests that B and C occupy more influential positions according to the eigenvector-based network measure.

## 3. Input Modification Experiment

One input was changed by removing the connection between nodes A and C. Since the network is undirected, both corresponding entries in the adjacency matrix were changed to zero.

### Modified Results

- Dominant eigenvalue: 2.1701
- Node A importance: 0.1454
- Node B importance: 0.3154
- Node C importance: 0.2696
- Node D importance: 0.2696
- Verification of \(Av = \lambda v\): True

### Comparison and Interpretation

Removing the connection reduced node A's importance score from 0.2192 to 0.1454. Node B's score increased from 0.2808 to 0.3154, while node D's score increased from 0.2192 to 0.2696. The dominant eigenvalue decreased from 2.5616 to 2.1701.

These changes demonstrate that modifying one network connection can affect the relative importance of multiple nodes. The verification remained true, confirming that the calculated eigenvalue and eigenvector satisfy the required equation within numerical precision.

## 4. Real-World Adaptation: Student Collaboration Network

The adapted program models five students: Alice, Brian, Carol, David, and Eva. A connection indicates that two students have collaborated on a project.

### Assumptions

1. Each student is represented by one node.
2. A connection represents collaboration between two students.
3. Collaboration is treated as mutual, so the adjacency matrix is symmetric.
4. The network is simplified and does not represent the frequency or quality of collaboration.
5. Importance scores describe network position rather than intelligence, academic achievement, or individual ability.

### Input Data

The adjacency matrix is:

\[
A =
\begin{bmatrix}
0 & 1 & 1 & 0 & 0\\
1 & 0 & 1 & 1 & 0\\
1 & 1 & 0 & 1 & 1\\
0 & 1 & 1 & 0 & 1\\
0 & 0 & 1 & 1 & 0
\end{bmatrix}
\]

The matrix represents the assumed collaboration links among the five students.

### Mathematical Operation

The program calculates the eigenvalues and eigenvectors of the adjacency matrix, identifies the dominant eigenvalue and its corresponding eigenvector, and normalizes the absolute eigenvector components to estimate each student's relative network importance.

### Output

- Dominant eigenvalue: 2.9354
- Alice importance: 0.1593
- Brian importance: 0.2136
- Carol importance: 0.2541
- David importance: 0.2136
- Eva importance: 0.1593
- Verification of \(Av = \lambda v\): True

### Interpretation

Carol has the highest importance score of 0.2541, followed by Brian and David, each with 0.2136. Alice and Eva each have a score of 0.1593. This indicates that Carol occupies the most influential position under this network model.

The results could help illustrate how collaboration networks can be analysed to identify highly connected and influential participants. However, the scores should not be used alone to evaluate a student's contribution or performance.

## 5. Conclusion

This task demonstrated how eigenvalues and eigenvectors can be calculated using Python and NumPy. The original network showed differences in node importance, and the input modification demonstrated how changing a connection affected the results. The student collaboration adaptation illustrated how the same mathematical technique can be applied to another network-based problem. In both programs, the verification confirmed that the calculated eigenvalue and eigenvector satisfied \(Av = \lambda v\) within numerical precision.