from time import time
import math

def main():
    s = time()
    cLis = []
    cDic = {2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[]}
    for n in range(2, 13):
        combos(n, cLis)

    for item in cLis:
        item.insert(0, 0)
        if len(item) > 2:
            temp = cDic[sum(item)]
            temp.append(item)
            cDic[sum(item)] = temp

    count = 0
    for i in range(4, 1000000):
        if math.log10(i) % 1 == 0:
            e = time()
            print(e - s)
            if sNum(i, cDic[int(math.ceil(math.log10(i ** 2+1)))]):
                count += i**2
        else:
            if sNum(i, cDic[int(math.ceil(math.log10(i ** 2)))]):
                count += i**2
    print(count)


def sNum(num, comNum):
    square = num**2
    strSquare = str(square)

    for com in comNum:
        count = 0
        start, end = 0, 0
        for i in range(len(com)-1):
            start += com[i]
            end += com[i+1]
            count += int(strSquare[start:end])
#           print(int(strSquare[start:end]))
        if count == num:
            return True
    return False


def combos(lim, cLis, lis = []):
    if sum(lis) == lim:
        cLis.append(lis)
        return
    elif sum(lis) < lim:
        for i in range(1, 6):
            combos(lim, cLis, lis+[i])


if __name__ == "__main__":
    main()
