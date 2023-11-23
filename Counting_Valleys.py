def countingValleys(steps, path):
    # Write your code here
    dis = 0
    vally = 0
    for i in path:
        if i == 'U':
            dis += 1
            if dis == 0:
                vally += 1
        else:
            dis -= 1

    
    return vally
