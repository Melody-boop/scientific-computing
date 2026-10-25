# Task 4: Floating-Point Arithmetic and Numerical Errors

## 1. Introduction

This task explores floating-point arithmetic, numerical errors, and the importance of selecting suitable mathematical formulas in scientific computing. Computers represent many decimal numbers using binary floating-point values, which can introduce small rounding errors. The task also compares a direct mathematical formula with a more numerically stable equivalent.

## 2. Inputs and Mathematical Operations

The program uses the following inputs and operations:

- `0.1` and `0.2`: added together and compared with `0.3`.
- `np.isclose()`: checks whether two floating-point values are sufficiently close within a tolerance.
- `np.sqrt(2)`: calculates the square root of 2.
- `1.414`: serves as an approximate value of the square root of 2.
- Absolute error: calculated as the absolute difference between the true and approximate values.
- Relative error: calculated by dividing the absolute error by the absolute value of the true value.
- Values of `x`: used to compare a direct formula with a numerically stable equivalent.

The two formulas compared are:

Direct formula:

\[
\frac{\sqrt{1+x}-1}{x}
\]

Stable formula:

\[
\frac{1}{\sqrt{1+x}+1}
\]

The formulas are mathematically equivalent for the tested positive values of \(x\).

## 3. Original Program Results and Interpretation

### Floating-point comparison

The program produced:

- `0.1 + 0.2 = 0.30000000000000004`
- Exact comparison: `False`
- Tolerance-based comparison: `True`

The result demonstrates that the sum of two decimal values may not be represented exactly in binary floating-point arithmetic. Therefore, direct equality comparisons can fail even when the difference is extremely small. The tolerance-based comparison correctly identifies the two values as sufficiently close.

### Absolute and relative error

The program reported:

- Absolute error: `0.00021356`
- Relative error: `0.01510114%`

The absolute error measures the difference between the actual square root of 2 and its approximation, 1.414. The relative error expresses this difference as a percentage of the true value. Both measurements help describe the accuracy of an approximation.

### Comparison of mathematical formulas

Using the original values of \(x\), the program produced:

| x | Direct formula | Stable formula |
|---|---:|---:|
| \(10^{-4}\) | 0.499987500624 | 0.499987500625 |
| \(10^{-8}\) | 0.499999996961 | 0.499999998750 |
| \(10^{-12}\) | 0.500044450291 | 0.500000000000 |

The results show that the direct formula becomes less accurate as \(x\) becomes extremely small. This happens because it subtracts two nearly equal numbers, which can cause loss of significant digits through cancellation. The stable formula avoids this subtraction and produces a more reliable result for very small positive values of \(x\).

## 4. Experiment: Changing the Input Values

The original values of \(x\), `1e-4`, `1e-8`, and `1e-12`, were changed to `1e-2`, `1e-3`, and `1e-4`.

The modified program produced:

| x | Direct formula | Stable formula |
|---|---:|---:|
| \(10^{-2}\) | 0.498756211209 | 0.498756211209 |
| \(10^{-3}\) | 0.499875062461 | 0.499875062461 |
| \(10^{-4}\) | 0.499987500624 | 0.499987500625 |

### Effect of the change

With the new input values, both formulas produced almost identical results. The noticeable difference between the formulas became much smaller because the experiment no longer included the extremely small values of \(10^{-8}\) and \(10^{-12}\).

As \(x\) approaches zero through positive values, both formulas approach 0.5. However, the stable formula remains preferable when working with extremely small values because it reduces the loss of numerical accuracy associated with subtracting nearly equal numbers.

## 5. Real-World Application: Financial Calculations

Floating-point arithmetic can be relevant in financial applications, including transaction processing, billing systems, and accounting software. Small numerical differences can become important when calculations involve many transactions or repeated operations.

For this adaptation, ten financial transactions of KSh 0.10 each were processed using ordinary floating-point arithmetic and Python's `Decimal` type.

### Inputs and assumptions

- Number of transactions: 10.
- Amount per transaction: KSh 0.10.
- Expected total: KSh 1.00.
- The transactions are assumed to have equal values, with no additional charges or deductions.
- `Decimal` is used to represent the monetary amounts as decimal values.

### Results

The program produced:

- Floating-point total: `KSh 1.00000000000000000`
- Decimal total: `KSh 1.00`
- Expected total: `KSh 1.00`
- Floating-point matches expected exactly: `True`
- Decimal matches expected exactly: `True`

### Interpretation

Both methods produced the expected total in this experiment. The floating-point result did not show an error in the final sum, while `Decimal` represented the decimal transaction amounts and total directly.

This experiment does not demonstrate an incorrect financial total. Instead, it illustrates two ways to perform the calculation and shows that the results can agree for a particular set of inputs. In other calculations, floating-point representation errors may become more noticeable. For financial systems that require exact decimal arithmetic, `Decimal` is generally a more suitable choice than binary floating-point values.

## 6. Conclusion

The task demonstrated that floating-point arithmetic can produce small representation errors and that numerical accuracy depends on both the input values and the mathematical method used. Exact equality comparisons may be unreliable for floating-point numbers, so tolerance-based comparisons are often more appropriate.

The experiment also showed that mathematically equivalent formulas can differ in numerical stability. The stable formula performed better for extremely small values of \(x\), while both formulas gave almost identical results for the larger values tested. Finally, the financial adaptation demonstrated how `Decimal` can be used for monetary calculations where exact decimal representation is important.
