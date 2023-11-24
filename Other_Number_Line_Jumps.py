def kangaroo(x1, v1, x2, v2):

    if x1<x2 and v1<v2:
        return "NO"
    
    if x2<x1 and v2<v1:
        return "NO"

    k1_dis = x1
    k2_dis = x2
    jump = 0

    while k1_dis != k2_dis:
        if k1_dis >= 10000 or k2_dis >= 10000:
            return "NO"
        else:
            k1_dis += v1
            k2_dis += v2
            jump +=1
        
    
    return jump,"YES"


print(kangaroo(0, 2, 0, 2))
print(kangaroo(0, 2, 5, 3))


def kangaroo(x1, v1, x2, v2):
    # Check if kangaroos have the same starting position and same jump distance
    if x1 == x2 and v1 == v2:
        return "YES"
    # Check if kangaroos have the same starting position but different jump distances
    elif x1 == x2 and v1 != v2:
        return "NO"
    # Check if kangaroos will never meet based on their relative positions and jump distances
    elif (x1 - x2) % (v2 - v1) == 0 and (x1 - x2) / (v2 - v1) >= 0:
        return "YES"
    else:
        return "NO"

# Example usage:
x1, v1, x2, v2 = map(int, input().split())
result = kangaroo(x1, v1, x2, v2)
print(result)
