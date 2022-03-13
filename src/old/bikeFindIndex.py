import random
#for testing
def CREAT():
    N = random.randrange(2, 100000)
    A = []
    for i in range(N):
        A.append(random.randint(-1000000000, 10000000000))
    return A


def solution(A):
    A.sort()
    max1 = 0
    for i in range(len(A) - 1):
        if abs(A[i] - A[i + 1]) > max1:
            max1 = abs(A[i] - A[i + 1])
    return max1 // 2


if __name__ == "__main__":
    A = [10, 0, 8, 2, -1, 12, 11, 3]
    print(solution(A))
    B = [5, 5]
    print(solution(B))

    for i in range(5):
        print(solution(CREAT()))


def solution2(A):
    N = len(A)
    MP = 1
    A.sort()
    m = [i for i in A if i > 0]
    m = list(dict.fromkeys(m))
    for i in m:
        if MP != i:
            return MP
        else:
            MP = MP + 1
    return MP