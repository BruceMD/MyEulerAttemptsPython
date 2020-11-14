from time import time

def main():

    dictF = {}
# saving a small amount of computation by saving the values of the factorils 0 to 9
    for i in range(10):
        dictF[i] = fact(i)
    print(dictF)

    dicLoop = {}
# dynamic programming to not waste time

    count = 0
    for n in range(1, 1000000):
        temp = findLoop(n, [], dicLoop)
        dicLoop[n] = temp
        if len(temp) == 60:
            count += 1
#            print(n)

    print(count)


def findLoop(x, lis, dicLoop):
    if x in lis:            # when we arrive at a loop, return
        return lis
    if x in dicLoop:        # dynamic programming to save time
        return findLoop(facSum(x), lis+dicLoop[x], dicLoop)
    return findLoop(facSum(x), lis+[x], dicLoop)


def facSum(n, v=0):
    if n == 0:
        return (v)
    return facSum(n//10, v+fact(n % 10))


def fact(n):
    if n <= 1:
        return 1
    return n*fact(n-1)


if __name__ == "__main__":
    s = time()
    main()
    e = time()
    print(e-s)