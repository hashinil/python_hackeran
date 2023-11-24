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
