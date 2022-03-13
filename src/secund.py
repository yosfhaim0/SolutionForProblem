def solution(A, D):
    balance = 0
    countToMinus100 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    countTo3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    mounthArr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(A)):
        balance = balance + A[i]
        mount = D[i].split("-")[1]
        if A[i] < 0:
            countTo3[int(mount) - 1] += 1
            countToMinus100[int(mount) - 1] += A[i]
    mount = 12
    for i in range(len(countToMinus100)):
        if countTo3[i] >= 3 and countToMinus100[i] <= -100:
            mount -= 1
    return balance - (5 * mount)


if __name__ == "__main__":
    print(solution([100, 100, -10, -20, -30], ['2020-01-01', '2020-02-01', '2020-02-11', '2020-02-05', '2020-02-08']))
