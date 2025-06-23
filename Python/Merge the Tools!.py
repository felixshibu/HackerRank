def merge_the_tools(string, k):
    # your code goes here
    n = len(string) / k
    new_string = ''
    result = []
    for i in range(0, len(string) + 1):
        if i == 0 or i == 1:
            new_string += string[i]
        elif i % n == 0:
            result.append(new_string)
            new_string = ''
            if i != len(string):
                new_string += string[i]
        else:
            if i != len(string):
                new_string += string[i]

    res = ''
    results = []
    for word in result:
        res = ''
        for i in word:
            if i not in res:
                res += i
        else:
            results.append(res)

    for f in results:
        print(f)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)