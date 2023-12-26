x = int(b'10', 2)
y = int(b'01', 2)
s = 1


# And:           Bits that are set in both x and y are set.
print(x & y)

# Or:            Bits that are set in either x or y are set.
print(x | y)

# Xor:           Bits that are set in x or y but not both are set.
print(x ^ y)

# Not:           Bits that are set in x are not set, and vice versa.
print(~x)

# Shift left:    Shift the bits of x, y steps to the left
print(x << s)

# Shift right:   Shift the bits of x, y steps to the right.
print(x >> s)
