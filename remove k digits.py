def removeKdigits(num, k):
    st = []
    for i in num:
        while k and len(st) > 0 and st[-1] > i:
            k -= 1
            st.pop()
        st.append(i)
    while k:
        k -= 1
        st.pop()
    st = "".join(st).lstrip("0")
    return st if st else "0"
removeKdigits("1432219", 3)