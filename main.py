
def in_array(array1, array2):
    r = []
    for i in array1:
        for j in array2:
            if i in j and i not in r:
                r.append(i)
    return sorted(r)


print(in_array(["live", "arp", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))