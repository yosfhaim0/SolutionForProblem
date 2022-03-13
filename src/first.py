def solution(message, K):
    word = message.split(" ")
    OP = ""
    count = 0
    if count + len(word[0]) > K:
        return OP
    for i in range(len(word)):
        if count + len(word[i]) > K:
            return OP[:-1]
        else:
            count = count + len(word[i]) + 1
            OP = OP + word[i] + " "
    return OP[:-1]


if __name__ == "__main__":
    print(solution('abc jkggggggggggg', 15))
