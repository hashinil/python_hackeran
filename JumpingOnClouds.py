def jumpingOnClouds(c):
    # Write your code here
    jump = 0
    i = 0
    while i < len(c)-1:
        if c[i] == 0:
            if i+2 < len(c) and c[i+2] == 0:
                jump += 1
                i+=2
            elif i+1 < len(c) and c[i+1] == 0:
                jump += 1
                i+=1
                
    return jump
