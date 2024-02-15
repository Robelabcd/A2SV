if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max1 = max(arr)
    i = 0
    h = len(arr)
    while i < h:
        if arr[i] == max1:
            arr.remove(max1)
            h-=1
            continue
        i+=1
    print(max(arr))
