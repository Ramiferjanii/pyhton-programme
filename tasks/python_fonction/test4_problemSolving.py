import os


def countPairs(arr):
    count = 0
    power_of_twos = [1 << i for i in range(31)]  # Since 2^0 to 2^30 are within the range of 0 ≤ arr[i] < 212

    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] & arr[j]) in power_of_twos:
                count += 1
    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = countPairs(arr)

    fptr.write(str(result) + '\n')

    fptr.close()