def solution(S, C):
    table = S.split('\n')
    nameC = table[0]
    indexC = (nameC.split(',')).index(C)
    maxV = -10000
    for i in table[1:]:
        temp = int(i.split(',')[indexC])
        if temp > maxV:
            maxV = temp
    return maxV


if __name__ == "__main__":
    A = 'city,temp2,temp\nParis,7,-3\nDubai,4,-4\nPort,-1,-2'
    print(solution(A, "temp"))
