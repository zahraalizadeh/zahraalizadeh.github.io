from collections import Counter


def count_letters(words):
    counter = Counter()
    for word in words.split():
        counter.update(word)
    return sum(counter.itervalues())


def DNA(x, y):
    n = count_letters(x)
    m = count_letters(y)

    C = [[0] * (n + 1)] * (m + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[j - 1] == y[i - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = max(C[i][j - 1], C[i - 1][j])

    # print C
    return C[m][n]


x = "ABCHJG"
y = "ABCG"
print DNA(x, y)