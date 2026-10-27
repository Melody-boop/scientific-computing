from scipy.optimize import root_scalar

# Adapted investment scenario
# Initial investment is KSh 15,000
# Annual cash inflows are in Kenyan shillings
cash_flows = [-15000, 4000, 5000, 6000, 4500]


# Calculate Net Present Value (NPV)
def npv(rate):
    return sum(
        cf / (1 + rate) ** t
        for t, cf in enumerate(cash_flows)
    )


# Derivative of the NPV function
def d_npv(rate):
    return sum(
        -t * cf / (1 + rate) ** (t + 1)
        for t, cf in enumerate(cash_flows)
        if t > 0
    )


# Newton-Raphson method
newton = root_scalar(
    npv,
    fprime=d_npv,
    x0=0.10,
    method="newton",
    xtol=1e-12
)

# Secant method
secant = root_scalar(
    npv,
    x0=0.05,
    x1=0.20,
    method="secant",
    xtol=1e-12
)

# Display results
print("ADAPTED INVESTMENT SCENARIO")
print(f"Initial investment: KSh {abs(cash_flows[0]):,.2f}")
print(f"Newton-Raphson IRR: {newton.root:.6%}")
print(f"Secant Method IRR: {secant.root:.6%}")
print(f"NPV at Newton solution: KSh {npv(newton.root):.6f}")
print(f"NPV at Secant solution: KSh {npv(secant.root):.6f}")
print("Newton-Raphson converged:", newton.converged)
print("Secant converged:", secant.converged)