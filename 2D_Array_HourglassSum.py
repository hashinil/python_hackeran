def hourglassSum(arr):
    sums = []
    
    for col in range(4):
        for row in range(4):
            sums.append(sum(arr[col][row:row+3]) + arr[col+1][row+1]+ sum(arr[col+2][row:row+3]))

    return max(sums)       

s = [[1, 2, 1, 0, 0, 0],
     [0, 1, 0, 0, 0, 0],
     [1, 1, 1, 0, 0, 0],
     [0, 0, 2, 4, 4, 0],
     [0, 0, 0, 2, 0, 0],
     [0, 0, 1, 2, 4, 0]]

print(hourglassSum(s))
# #
