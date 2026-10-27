# Task 14: Curve Fitting and Approximation

## 1. Objective

The objective of this task is to understand curve fitting and use Python libraries to model the relationship between measured data and a mathematical function. The task also demonstrates how a fitted model can estimate values beyond the measured data.

## 2. Mathematical Concept

Curve fitting finds the parameters of a mathematical function that best represents observed data. The least-squares method minimizes the sum of squared differences between actual and predicted values.

In this task, a quadratic model is used:

\[
y=ax^2+bx+c
\]

The `scipy.optimize.curve_fit` function estimates the parameters \(a\), \(b\), and \(c\). The root mean square error (RMSE) measures the difference between observed and predicted values.

## 3. Original Problem: Server Response Time

The original program models server response time using measurements collected at different numbers of concurrent users.

### Results

- Fitted model: \(y=0.002167x^2-0.1345x+85.00\)
- RMSE: 1.55 ms
- Predicted response time at 400 users: 377.86 ms

The small RMSE indicates that the fitted curve closely represents the measured data.

## 4. Real-World Adaptation: Online Store Checkout Performance

The adapted program investigates the relationship between concurrent users and checkout response time in an online store. A quadratic model is fitted to the measurements, and the fitted curve is used to estimate response time at 800 concurrent users.

### Results

- Fitted model: \(y=0.001161x^2-0.1732x+119.29\)
- RMSE: 3.11 ms
- Predicted response time at 800 users: 723.57 ms

The RMSE suggests that the model fits the measured checkout data reasonably well. The prediction indicates that response time may increase as more users access the store simultaneously.

## 5. Tools and Libraries Used

- **NumPy:** Stores and processes numerical data.
- **SciPy:** Fits the quadratic model using `curve_fit`.
- **Matplotlib:** Visualizes measured values and the fitted curve.

## 6. Applications

Curve fitting is useful in performance modelling, trend analysis, sensor calibration, demand forecasting, experimental research, and predicting system behaviour from observed measurements.

## 7. Conclusion

This task demonstrates how curve fitting can be used to represent measured data mathematically and make predictions. Both programs successfully fitted quadratic models and generated graphs. The online store adaptation shows how this technique can support performance planning by estimating checkout response time under heavier traffic.

However, predictions beyond the measured range are extrapolations and may not reflect actual system performance. Real server testing would be necessary to verify the prediction at 800 concurrent users.
