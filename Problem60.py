from time import time


def main():

    print(isPrime(32))

    pLis = [2]
    pDic = {2:[]}

    for i in range(3, 10000, 2):
        if isPrime(i):
            pLis.append(i)
            pDic[i] = []

    print(pLis)
    print(pDic)

    for i in range(len(pLis)):
        for j in range(i+1, len(pLis)):
            p, q = pLis[i], pLis[j]
            if check(p, q):
                pDic[p].append(q)
                pDic[q].append(p)

    search([], pDic)


def search(lis, pDic):
    if not limit(lis):
        return
    if len(lis) == 5:
        print(lis)
        return
    if len(lis) == 0:
        for key in pDic:
            search(lis+[key], pDic)
    else:
        for item in pDic[lis[-1]]:
            if item > lis[-1]:
                search(lis+[item], pDic)


def limit(lis):
    if len(lis) > 1:
        for i in range(len(lis)-1):
            for j in range(i+1, len(lis)):
                if not check(lis[i], lis[j]):
                    return False
    return True


def check(p, q):
    if isPrime(int(str(p)+str(q))):
        if isPrime(int(str(q)+str(p))):
            return True
    return False


def isPrime(x):
    if x % 2 == 0:
        return False
    for i in range(3, round(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True


if __name__ == "__main__":
    s = time()
    main()
    e = time()
    print(e-s)
