
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Simulated online store traffic and checkout response time
users = np.array([100, 200, 300, 400, 500, 600, 700], dtype=float)
response_ms = np.array([110, 135, 175, 235, 320, 430, 570], dtype=float)

# Quadratic model
def model(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the model
parameters, covariance = curve_fit(model, users, response_ms)
a, b, c = parameters

predicted = model(users, a, b, c)
rmse = np.sqrt(np.mean((response_ms - predicted)**2))

print("Online Store Checkout Performance")
print(f"Fitted model: y = {a:.6f}x^2 + {b:.4f}x + {c:.2f}")
print(f"RMSE: {rmse:.2f} ms")
print(f"Predicted response at 800 users: {model(800, a, b, c):.2f} ms")

# Plot measured and fitted response times
x_plot = np.linspace(users.min(), 800, 300)

plt.figure(figsize=(10, 6))
plt.scatter(users, response_ms, label="Measured response times")
plt.plot(x_plot, model(x_plot, a, b, c), label="Fitted curve")
plt.xlabel("Concurrent users")
plt.ylabel("Checkout response time (ms)")
plt.title("Online Store Checkout Performance")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Task_14_real_world_adaptation.png", dpi=300)
print("Graph saved as Task_14_real_world_adaptation.png")
