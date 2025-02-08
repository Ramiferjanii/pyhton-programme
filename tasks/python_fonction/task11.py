
def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        dec = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        print(f"{dec:>{width}} {octa:>{width}} {hexa:>{width}} {bina:>{width}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)






    """We calculate the width of the binary representation of the largest number.

For each number from 1 to the given number:

Convert the number to decimal, octal, hexadecimal (capitalized), and binary formats.

Print each of these values, right-aligned to the width of the largest binary representation."""