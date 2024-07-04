a = 5  # In binary (8421): 0101
b = 4  # In binary (8421): 0100

# 1. and(&) operator
# The & operator performs a bitwise AND. It compares each bit of the binary representation of a and b. 
# Only if both bits are 1, the resulting bit is 1; otherwise, it is 0.
# 0101
# 0100
# ----
# 0100 (4 in decimal)
and_p = a & b
print(and_p)  # Output: 4

# 2. xor (^) operator
# The ^ operator performs a bitwise XOR. It compares each bit of the binary representation of a and b.
# If the bits are different, the resulting bit is 1; otherwise, it is 0.
# 0101
# 0100
# ----
# 0001 (1 in decimal)
xor_p = a ^ b
print(xor_p)  # Output: 1

# 3. leftshift (<<) operator
# The << operator shifts the bits of a to the left by the specified number of positions (1 in this case).
# Each shift to the left multiplies the number by 2.
# 0101 << 1
# 1010 (10 in decimal)
leftshift = a << 1
print(leftshift)  # Output: 10

# 4. rightshift (>>) operator
# The >> operator shifts the bits of a to the right by the specified number of positions (1 in this case).
# Each shift to the right divides the number by 2.
# 0101 >> 1
# 0010 (2 in decimal)
rightshift = a >> 1
print(rightshift)  # Output: 2

