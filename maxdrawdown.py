def get_maxDrawdown(l):   
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            break
        if i == len(l)-2:
            return 0
    
    l = l[i:] 
    # print(l)

    maxlist = [l[0]]
    currentmax = l[0]
    currentmin = l[0]
    drawdown = []

    for i in range(len(l)-1):
        if l[i+1] < currentmin:
            currentmin = l[i+1]
        if (i < len(l) and l[i] < l[i+1] and l[i+1] > l[i+2] and l[i+1] > currentmax):
            drawdown.append(currentmax-currentmin)
            currentmax = l[i+1]
            currentmin = l[i+1]
    
    # print('max', currentmax)
    # print('min', currentmin)
    drawdown.append(currentmax-currentmin)
    # print(drawdown)
    return max(drawdown)


# if __name__ == "__main__":
    # print(get_maxDrawdown([1, 7, 3, 4, 5, 9, 4, 3, 7, 1, 6]))
    # print(get_maxDrawdown([13,24,3,41,15,16,10])) 
    # print(get_maxDrawdown([1,1,1,1,1,2])) 




