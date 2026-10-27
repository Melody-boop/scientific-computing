# Task 19: Numerical Optimization Using SciPy

## 1. Introduction
Numerical optimization is used to find the best solution to a problem while satisfying specified constraints. In this task, SciPy's `minimize` function is used to minimize the cost of cloud-server resources while meeting a required computing capacity.

## 2. Objectives
- Use SciPy's `minimize` function to solve an optimization problem.
- Minimize total resource cost.
- Apply non-negative bounds and a capacity constraint.
- Adapt the optimization model to a small-business cloud-resource scenario.

## 3. Methodology
Two resource types are considered. Let \(x\) represent the units of Type A and \(y\) represent the units of Type B.

The objective function is:

\[
\min C=c_Ax+c_By
\]

Subject to the capacity requirement:

\[
a_Ax+a_By\geq K
\]

And the non-negativity constraints:

\[
x\geq0,\qquad y\geq0
\]

Where \(c_A\) and \(c_B\) are the costs per unit, \(a_A\) and \(a_B\) are the capacities per unit, and \(K\) is the required capacity. SciPy's Sequential Least Squares Programming (SLSQP) method was used to find a feasible low-cost solution.

## 4. Original Problem: Cloud Server Cost Optimization

The original model uses the following values:

| Parameter | Type A | Type B |
|---|---:|---:|
| Cost per unit | 12 | 18 |
| Capacity per unit | 100 | 170 |

The required capacity is 1,000 units.

### Results
- Optimization success: `True`
- Type A units: **0.0000**
- Type B units: **5.8824**
- Total capacity: **1,000.00**
- Minimum cost: **105.88 cost units**

The optimizer selected Type B resources because they provide the required capacity at a lower cost for the given parameters. The result allows fractional resource units, as the optimization model treats the decision variables as continuous quantities.

## 5. Real-World Adaptation: Small-Business Cloud Resources

The adapted model represents a small business selecting cloud resources with different costs and capacities.

| Parameter | Type A | Type B |
|---|---:|---:|
| Cost per unit | 10 | 16 |
| Capacity per unit | 80 | 150 |

The required capacity is 900 units.

### Results
- Optimization success: `True`
- Type A units: **0.0000**
- Type B units: **6.0000**
- Required capacity: **900.00**
- Total capacity: **900.00**
- Minimum cost: **96.00 cost units**
- Graph saved as `Task_19_real_world_adaptation.png`.

The optimized solution uses six Type B units to meet the capacity requirement exactly at a total cost of 96 cost units.

## 6. Discussion
Both optimization problems were solved successfully. The results show how optimization can help allocate resources while minimizing costs and meeting a capacity target. The adaptation illustrates how a small business could compare alternative cloud-resource options using mathematical optimization.

## 7. Limitations
The model assumes that resource costs and capacities are fixed and that resource quantities can be fractional. Actual servers may need to be purchased in whole units, and cloud services may involve additional costs such as storage, network traffic, maintenance, and variable usage charges. Integer constraints and more detailed pricing models may therefore be needed in a real deployment.

## 8. Conclusion
SciPy's `minimize` function successfully solved the original cloud-server allocation problem and the adapted small-business scenario. Both solutions met their capacity requirements while minimizing the modeled cost. This task demonstrates how numerical optimization can support resource allocation and cost-management decisions.