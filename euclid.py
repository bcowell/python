# Find the greatest common denominator of two numbers
# using Euclid's algorithm
# Ex. GCD(20,8) = 4

def gcd(a, b):
    while (b != 0):
        temp = a
        a = b
        b = temp % b
    
    return a

# Examples
print(gcd(60, 96))  # expecting 12
print(gcd(20,8))    # expecting 4

