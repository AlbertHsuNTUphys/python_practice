def Count_Change_Ways(N, S):
    l = len(S)
    if l == 0:
        return 0
    if l == 1:
        if N % S[0]:
            return 0
        else:
            return 1
    S.sort(reverse=True)
    count = 0
    coefficients = [0 for i in range(len(S))]
    coefficients[0] = (N // S[0] )+ 1
    while max(coefficients[:l-1]) != 0:

        coefficients[-1] = 0
        # print(coefficients)
        cursor = l-2
        while coefficients[cursor] == 0:
            cursor -= 1
            # print(cursor)
        coefficients[cursor] -= 1
        # print(cursor)
        # print(coefficients)
        while cursor < l-1:
            # print(cursor)
            cursor += 1
            coefficients[cursor] = (N - calculate_sum(S, coefficients)) // S[cursor]

        total = calculate_sum(S, coefficients)
        if total == N:
            # print(coefficients)
            count += 1

    return count

def calculate_sum(s, c):
    total = 0
    for i, j in zip(s, c):
        total += i*j
    return total




if __name__ == "__main__":
    print(Count_Change_Ways(200, [100, 50, 20, 10, 5, 3, 2, 1] ))




