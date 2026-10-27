# Task 11: Newton–Raphson and Secant Methods

## 1. Introduction

Root-finding methods are numerical techniques used to find values of a variable that make a mathematical function equal to zero. This task applies the Newton–Raphson and Secant methods to calculate the Internal Rate of Return (IRR) of an investment.

The IRR is the discount rate at which the Net Present Value (NPV) of an investment equals zero.

## 2. Mathematical Concepts

### Newton–Raphson Method

The Newton–Raphson method uses a function and its derivative to estimate a root:

\[
x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}
\]

It can converge quickly when the initial estimate is suitable and the derivative is well behaved.

### Secant Method

The Secant method estimates the derivative using two previous estimates. Its update formula is:

\[
x_{n+1}=x_n-f(x_n)\frac{x_n-x_{n-1}}{f(x_n)-f(x_{n-1})}
\]

Unlike Newton–Raphson, it does not require an explicitly supplied derivative.

## 3. Original Investment Scenario

The original investment consists of an initial outflow of KSh 10,000 followed by annual cash inflows of KSh 3,000, KSh 3,500, KSh 4,000, and KSh 2,500.

The NPV is calculated using:

\[
NPV(r)=\sum_{t=0}^{n}\frac{CF_t}{(1+r)^t}
\]

where \(CF_t\) represents the cash flow in year \(t\), and \(r\) is the discount rate.

### Original Results

- Newton–Raphson IRR: 11.542461%
- Secant Method IRR: 11.542461%
- NPV at both solutions: approximately KSh 0
- Both methods converged successfully.

The matching results show that both methods found the same root for the investment's NPV function.

## 4. Real-World Adaptation

The adapted scenario uses an initial investment of KSh 15,000 and annual cash inflows of KSh 4,000, KSh 5,000, KSh 6,000, and KSh 4,500.

The cash flows were changed to represent a different investment project. The same NPV function and root-finding methods were applied to determine its IRR.

### Adapted Results

- Newton–Raphson IRR: 11.039769%
- Secant Method IRR: 11.039769%
- NPV at both solutions: approximately KSh 0
- Both methods converged successfully.

The adapted scenario produced a lower IRR than the original scenario. This demonstrates that changing the initial investment and future cash inflows changes the investment's calculated return.

## 5. Input Values and Parameters

| Parameter | Original scenario | Adapted scenario |
|---|---|---|
| Initial investment | KSh 10,000 | KSh 15,000 |
| Year 1 cash inflow | KSh 3,000 | KSh 4,000 |
| Year 2 cash inflow | KSh 3,500 | KSh 5,000 |
| Year 3 cash inflow | KSh 4,000 | KSh 6,000 |
| Year 4 cash inflow | KSh 2,500 | KSh 4,500 |
| Newton–Raphson initial estimate | 0.10 | 0.10 |
| Secant initial estimates | 0.05 and 0.20 | 0.05 and 0.20 |

The programs use SciPy's `root_scalar` function. A tolerance of \(10^{-12}\) was specified to request a high-precision numerical solution.

## 6. Assumptions and Limitations

1. Cash flows occur at the end of each year.
2. The initial investment occurs at year zero.
3. The listed cash flows are assumed to be known and fixed.
4. No taxes, inflation, financing costs, or changes in cash flows are included.
5. The initial estimates are suitable for finding the intended root in these examples.
6. The calculated IRR is a mathematical estimate and does not guarantee the actual profitability of an investment.

## 7. Applications

Root-finding methods are useful in financial calculations, engineering equations, circuit analysis, calibration, and nonlinear mathematical models. In finance, IRR can help compare investment opportunities, although it should be considered alongside other measures such as NPV, risk, and the cost of capital.

## 8. Conclusion

Both Newton–Raphson and Secant methods successfully calculated the IRR for the original and adapted investment scenarios. Each pair of methods produced matching results, and the NPV at each calculated root was approximately zero. The adapted case demonstrated how different investment cash flows can affect the estimated rate of return.
