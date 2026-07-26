if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    m = max(arr)
    i = 0
    while (i < n):
        if (m == arr[i]):
            del arr[i]
            n -= 1
        else:
            i += 1
    print(max(arr))

