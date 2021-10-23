def find_max(counts):
    maximum = counts[0] 
    for count in counts:
     if count > maximum:
        maximum = count
    return maximum
