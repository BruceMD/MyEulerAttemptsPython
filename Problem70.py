def main():

    listP = [2]
    for p in range(3, 1000, 2):
        if isPrime(p):
            listP.append(p)
    print(listP)

    print(perPri(9, listP, []))


def perPri(x, listP, lis):
    n = 0
    if x == 1:
        return lis
    while n < len(listP):
        print(n)
        if x % listP[n] == 0:
            perPri(x / listP[n], listP, lis + [listP[n]])
            break
        else:
            n += 1


def isPrime(x):
    if x < 3:
        return False
    count = 0
    for i in range(3, round(x ** 0.5) + 1, 2):
        if x % i == 0:
            count += 1
            return False
    if count == 0:
        return True


if __name__ == "__main__":
    main()