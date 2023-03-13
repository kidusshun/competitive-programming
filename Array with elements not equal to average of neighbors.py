import functools

def avg_neighbors_cmp(a, b):
    n = len(lst)
    print(a,b,n)
    avg_a = (a[(i-1)%n] + a[(i+1)%n])/2
    avg_b = (b[(j-1)%n] + b[(j+1)%n])/2
    if avg_a == a[i]:
        return -1
    elif avg_b == b[j]:
        return 1
    else:
        return 0

lst = [4, 2, 6, 3, 9, 5]

sorted_lst = sorted(lst, key=functools.cmp_to_key(avg_neighbors_cmp))

print(sorted_lst)