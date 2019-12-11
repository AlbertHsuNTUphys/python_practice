def Count_Change_Ways(n, s):
    if len(s) == 1:
        if n % s[-1]:
            return 0
        else:
            return 1
        
    d = {}
    s.sort(reverse=True)
    t = 0
    coef = [0]
    for i in range(n//s[0]+1):
        t += myccw(n, s, tuple(coef), d)
        coef[0] += 1
    # print(d)
    return t

# dict: (len(coef), remainers)

def myccw(n, s, coef, d):
    # print(coef)
    ts = calculate_sum(s, coef)
    rem = n-ts
    # print(rem)
    if rem < 0:
        return 0
    if len(coef) == len(s)-1:
        if rem % s[-1]:
            return 0
        else:
            # print('good')
            return 1

    if ((len(coef), rem) in d):
        # print('used dict')
        return d[(len(coef), rem)]

    tp = rem // s[len(coef)]
    total = 0
    for i in range(tp+1):
        total += myccw(n, s, coef + (i,), d)

    # if len(coef) > 3:
    d[(len(coef), rem)] = total

    return total


def calculate_sum(s, c):
    total = 0
    for i, j in zip(s, c):
        total += i*j
    return total




if __name__ == "__main__":
    # print(Count_Change_Ways(200, [100, 50, 20, 10, 5, 3, 2, 1] ))
    print(Count_Change_Ways(1000, [1, 2, 5, 10, 50, 100, 101] ) )




