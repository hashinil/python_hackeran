def sockMerchant(n, ar):
    # Write your code here
    colors = {i:ar.count(i)  for i in ar}
    pairs = sum([colors[c]//2 for c in colors])
    return pairs
    
