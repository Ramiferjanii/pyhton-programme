# Enter your code here. Read input from STDIN. Print output to STDOUT


# Step 1: Read inputs
x, k = map(int, input().split())  # Read the values of x and k
n = input()  # Read the polynomial
def polynomial(n) :
    return n
# Step 2: Evaluate the polynomial at x
# In Python 2, the use of eval() with raw_input() can be directly translated to input()
# Since we are using Python 3 here, we will use eval() with the provided polynomial
result = eval(polynomial(n))

# Step 3: Compare the result with k and print the answer
print(result == k)