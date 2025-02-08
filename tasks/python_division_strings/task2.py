# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input()) 
b = int(input())
g = a//b
k = a%b 
p = divmod(a , b )
print(f"{g}")
print(f"{k}")
print(f"{p}")










"""Read in two integers,a  and b, and print three lines.
The first line is the integer division a//b  (While using Python2 remember to import division from __future__).
The second line is the result of the modulo operator: a%b .
The third line prints the divmod of a and b ."""