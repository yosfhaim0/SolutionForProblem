def solution(N, S):
    if S == "":
        return N * 2
    else:
        sits = S.split(" ")
        sits.sort()
        d = {}
        for i in sits:
            if i[0] in d:
                d[i[0]] = d[i[0]] + i[1]
            else:
                d[i[0]] = i[1]
        count = 0
        for x, y in d.items():
            count += g(x, y)
    return count


def g(num, let):
    BJ = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in let:
        if i == 'B':
            BJ[0] = 1
        if i == 'C':
            BJ[1] = 1
        if i == 'D':
            BJ[2] = 1
        if i == 'E':
            BJ[3] = 1
        if i == 'F':
            BJ[4] = 1
        if i == 'G':
            BJ[5] = 1
        if i == 'H':
            BJ[6] = 1
        if i == 'J':
            BJ[7] = 1
    count = 0
    if BJ[0:4] == [0, 0, 0, 0] and BJ[4:8] == [0, 0, 0, 0]:
        return 2
    if BJ[0:4] == [0, 0, 0, 0]:
        return 1
    if BJ[4:8] == [0, 0, 0, 0]:
        return 1
    if BJ[2:6] == [0, 0, 0, 0]:
        return 1
    return 0


if __name__ == "__main__":
    print(solution(2, '1A 2F 1C'))
