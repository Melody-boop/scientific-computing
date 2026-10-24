# Task 3: Mathematical Functions and Vectorization

## 1. Objective

The objective of this task is to understand mathematical functions and vectorization in Python using NumPy. The program simulates network latency measurements in milliseconds, converts them into seconds, and squares the converted values. It compares a traditional loop with a vectorized operation to demonstrate the difference in execution time.
## 2. Inputs and Mathematical Operations

### Inputs
- Random number generator seed: `42`.
- Number of simulated network latency readings: `1,000,000` in the original program.
- Network latency range: 5 to 250 milliseconds.
- Timeit repetitions: the loop runs once, while the vectorized operation runs three times and its average execution time is calculated.

### Mathematical Operations
1. Convert latency measurements from milliseconds to seconds by dividing each value by `1000`.
2. Square each converted latency value.
3. Measure the execution time of both the loop-based and vectorized implementations.
4. Calculate the approximate speed-up by dividing the loop execution time by the vectorized execution time.

The vectorized implementation uses NumPy to perform operations on the entire array without explicitly looping through each value in Python.
## 3. Results and Interpretation

### Original Program Results

The original program processed one million simulated network latency readings and produced the following results:

- First five squared latency values: `[0.03787665, 0.01266192, 0.04637842, 0.03092504, 0.00078812]`
- Loop execution time: 2.7278 seconds
- Vectorized execution time: 0.0317 seconds
- Approximate speed-up: 86.0 times

The results show that the vectorized implementation was considerably faster than the loop-based implementation. The loop processes each value individually, while NumPy performs the operations on the entire array efficiently. The squared latency values are expressed in seconds squared (s²).

Execution times may vary depending on the computer and system conditions.

## 4. Experiment: Changing the Number of Readings

The original program was modified by reducing the number of simulated latency readings from 1,000,000 to 100,000.

### Experimental Results

- First five squared latency values: `[0.03787665, 0.01266192, 0.04637842, 0.03092504, 0.00078812]`
- Loop execution time: 0.3378 seconds
- Vectorized execution time: 0.0108 seconds
- Approximate speed-up: 31.2 times

### Effect of the Change

Reducing the dataset size decreased the execution time of both implementations. The loop execution time decreased from 2.7278 seconds to 0.3378 seconds, while the vectorized execution time decreased from 0.0317 seconds to 0.0108 seconds.

The vectorized implementation remained faster than the loop-based implementation. The approximate speed-up changed from 86.0 times to 31.2 times, showing that the performance advantage of vectorization can vary with dataset size and execution conditions.

The first five values remained unchanged because the random number generator uses the same seed, 42, and the smaller dataset retains the same initial readings.

## 5. Adaptation to a Real-World Problem

### Application: Website API Response-Time Analysis

Vectorization can be applied when monitoring the response times of website APIs. Developers can collect response-time measurements to evaluate how quickly a website's services respond to requests.

For this adaptation, six sample API response times are used: 35, 42, 28, 65, 51, and 39 milliseconds.

### Assumptions and Inputs

- The response times are measured in milliseconds.
- The six readings represent sample API requests.
- The measurements are assumed to be valid and non-negative.
- NumPy is used to process all readings simultaneously.

### Mathematical Operations

1. Store the response times in a NumPy array.
2. Convert milliseconds to seconds by dividing each value by 1,000.
3. Square each converted response time using a vectorized operation.
4. Calculate the average response time to provide an additional performance indicator.

### Python Implementation

```python
import numpy as np

# Sample website API response times in milliseconds
response_ms = np.array([35, 42, 28, 65, 51, 39])

# Convert milliseconds to seconds
response_seconds = response_ms / 1000.0

# Square each response time using vectorization
squared_response = response_seconds ** 2

# Calculate average response time
average_response = np.mean(response_ms)

print("Response times in seconds:", response_seconds)
print("Squared response times:", squared_response)
print(f"Average response time: {average_response:.2f} ms")
```

### Expected Outputs

- Response times in seconds: `[0.035, 0.042, 0.028, 0.065, 0.051, 0.039]`
- Squared response times: `[0.001225, 0.001764, 0.000784, 0.004225, 0.002601, 0.001521]`
- Average response time: `43.33 ms`

### Interpretation

The average response time is 43.33 milliseconds for the six sample requests. The squared values show the result of applying a mathematical operation to every measurement using NumPy.

A developer could use response-time measurements and additional performance indicators to investigate slow API requests and monitor service performance. Squared response times alone do not establish whether an API is performing well or poorly; they must be interpreted alongside suitable performance targets and other measurements.

## 6. Conclusion

This task demonstrated how mathematical functions and vectorization can be implemented using NumPy. The experiment showed that vectorization was faster than a traditional loop for both tested dataset sizes, although the measured speed-up varied.

The website API example demonstrated how vectorization can process real-world response-time measurements efficiently. Overall, vectorization is a useful technique for numerical computing because it simplifies array operations and can significantly reduce execution time for large datasets.