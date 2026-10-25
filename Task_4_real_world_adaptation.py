
from decimal import Decimal

# Simulate ten financial transactions of KSh 0.10 each
transactions = [0.10] * 10

# Calculate using floating-point arithmetic
float_total = sum(transactions)

# Calculate using Decimal for accurate decimal arithmetic
decimal_total = sum(Decimal("0.10") for _ in range(10))
expected_total = Decimal("1.00")

print("FINANCIAL CALCULATION")
print(f"Floating-point total: KSh {float_total:.17f}")
print(f"Decimal total: KSh {decimal_total:.2f}")
print(f"Expected total: KSh {expected_total:.2f}")

print("Float matches expected exactly:", float_total == 1.0)
print("Decimal matches expected exactly:", decimal_total == expected_total)
