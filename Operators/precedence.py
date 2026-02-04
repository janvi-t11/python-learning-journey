# Python Operator Precedence (Highest to Lowest)

# 1. Parentheses
result = (10 + 5) * 2  # Parentheses first

# 2. Exponentiation
result = 2 ** 3 ** 2  # Right to left: 2 ** (3 ** 2) = 512

# 3. Unary operators
result = -5
result = +5
result = ~5  # Bitwise NOT

# 4. Multiplication, Division, Floor Division, Modulo
result = 10 * 2
result = 10 / 2
result = 10 // 2
result = 10 % 3

# 5. Addition, Subtraction
result = 10 + 5
result = 10 - 5

# 6. Bitwise shifts
result = 5 << 1  # Left shift
result = 5 >> 1  # Right shift

# 7. Bitwise AND
result = 5 & 3

# 8. Bitwise XOR
result = 5 ^ 3

# 9. Bitwise OR
result = 5 | 3

# 10. Comparison operators
result = 5 == 5
result = 5 != 3
result = 5 < 10
result = 5 > 3

# 11. Logical NOT
result = not True

# 12. Logical AND
result = True and False

# 13. Logical OR (Lowest)
result = True or False

# Example showing precedence
print(2 + 3 * 4)  # Output: 14 (multiplication before addition)
print((2 + 3) * 4)  # Output: 20 (parentheses override)