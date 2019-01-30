if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    m=list(set(arr))
    m.sort(reverse=True)
    print(m[1])