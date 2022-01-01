def robberies(houses):
    if len(houses) == 1: return 1

    if len(houses) == 2:
        result = houses[0] if houses[0] > houses[len(houses) - 1] else houses[len(houses) - 1]

    even = 0
    odd = 0
    result = 0

    for i in range(0, len(houses)):
        if i % 2:
            even += (houses[i])
        else:
            odd += (houses[i])

    temp = even if even > odd else odd
    
    temp2 = houses[0] + houses[len(houses) - 1]
    
    result = temp if temp > temp2 else temp2

    return result


print(robberies([2,6,3,7]))