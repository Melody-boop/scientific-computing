
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
