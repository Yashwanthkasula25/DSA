# Read inputs
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter position: "))

# Initialize list with first two numbers
seq = [a, b]

# Generate up to position 'c'
for i in range(2, c):
    x = seq[i - 1] + seq[i - 2]
    seq.append(x)

# Print the c-th term (index c-1)
print("The number at position", c, "is:", seq[c - 1])
##