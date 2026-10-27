# Task 18: Numerical Solution of Ordinary Differential Equations Using SciPy

## 1. Introduction
Ordinary differential equations (ODEs) describe how quantities change over time. SciPy provides `solve_ivp`, a numerical solver that approximates solutions to initial-value problems. This task uses `solve_ivp` to simulate capacitor charging in an RC circuit and compares the numerical results with the exact mathematical solution.

## 2. Objectives
- Use SciPy's `solve_ivp` to solve a first-order ODE.
- Model the voltage across a charging capacitor.
- Compare numerical results with the exact solution.
- Apply the method to a backup-power circuit scenario.

## 3. Methodology
The voltage across a capacitor in a charging RC circuit is described by:

\[
\frac{dV}{dt}=\frac{V_s-V}{RC}
\]

Where:
- \(V\) is the capacitor voltage.
- \(V_s\) is the supply voltage.
- \(R\) is resistance in ohms.
- \(C\) is capacitance in farads.
- \(t\) is time in seconds.

The exact solution for an initially uncharged capacitor is:

\[
V(t)=V_s\left(1-e^{-t/(RC)}\right)
\]

Python, NumPy, Matplotlib, and SciPy's `solve_ivp` were used to solve the equation, compare results, and generate graphs.

## 4. Original Problem: RC Circuit Charging

The original simulation uses a 5 V supply, resistance of 1,000 Ω, capacitance of 0.001 F, and an initial capacitor voltage of 0 V. The simulation runs for five seconds.

### Results
- Solver success: `True`
- Capacitor voltage at 5 seconds: **4.9663 V**
- Maximum error against the exact solution: **9.282 × 10⁻¹⁰ V**
- Graph saved as `Task_18_ode_solution.png`.

The capacitor voltage approaches the 5 V supply voltage as charging progresses. The very small numerical error shows that the computed solution closely matches the exact solution.

## 5. Real-World Adaptation: Backup-Power Capacitor Charging

The adapted simulation models a capacitor charging in a backup-power circuit using a 12 V supply, resistance of 2,200 Ω, capacitance of 0.002 F, and an initial voltage of 0 V. The simulation runs for 20 seconds.

### Results
- Solver success: `True`
- Supply voltage: **12.00 V**
- Resistance: **2,200 Ω**
- Capacitance: **0.0020 F**
- Capacitor voltage after 20 seconds: **11.8726 V**
- Maximum error against the exact solution: **2.209 × 10⁻⁹ V**
- Graph saved as `Task_18_real_world_adaptation.png`.

The capacitor voltage rises towards the 12 V supply voltage. The small error indicates that the numerical solution closely agrees with the exact solution for the selected parameters.

## 6. Discussion
Both simulations demonstrate the effectiveness of `solve_ivp` for solving initial-value problems. Comparing the numerical solutions with the exact solutions provides a way to evaluate numerical accuracy. The adaptation illustrates how differential equations can model voltage changes in an electrical circuit.

## 7. Limitations
The model assumes constant resistance and capacitance, an ideal voltage supply, and no leakage or other circuit losses. Real backup-power systems may involve additional components and charging behaviour that this simple RC model does not represent.

## 8. Conclusion
SciPy's `solve_ivp` successfully solved the original and adapted RC-circuit charging problems. Both numerical solutions closely matched their exact solutions, demonstrating how numerical ODE solvers can be used to model changing physical quantities over time.