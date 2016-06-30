def toString(List):
    return ''.join(List)
def permute(a, l, r):
    if l == r:
        print (''.join(a))
    else:
        for i in range(l, r + 1):
            temp = a[l]
            a[l] = a[i]
            a[i] = temp
            permute(a, l + 1, r)
            temp = a[l]
            a[l] = a[i]
            a[i] = temp


str = "abc"
n = len(str)
a = list(str)
permute(a, 0, n - 1)
