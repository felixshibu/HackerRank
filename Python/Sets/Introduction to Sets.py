def average(array):
    # your code goes here
    set_arr = set(array)
    return sum(set_arr) / len(set_arr)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)