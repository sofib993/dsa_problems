if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        cs = input().split()
        if cs[0] == "insert":
            arr.insert(int(cs[1]), int(cs[2])) 
        elif cs[0] == "print":
            print(arr)
        elif cs[0] == "remove":
            arr.remove(int(cs[1]))
        elif cs[0] == "append":
            arr.append(int(cs[1]))
        elif cs[0] == "sort":
            arr.sort()
        elif cs[0] == "pop":
            arr.pop(-1)
        elif cs[0] == "reverse":
            arr.reverse()
