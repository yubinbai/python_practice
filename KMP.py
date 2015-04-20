# implemnt the kmp algorithm


def KMPnext(s):
    next = [-1 for x in range(len(s))]
    next[1] = 0

    cnd = 0
    pos = 2
    while pos < len(s):
        if s[pos - 1] == s[cnd]:
            cnd += 1
            next[pos] = cnd
            pos += 1
        elif cnd > 0:
            cnd = next[cnd]
        else:
            next[pos] = 0
            pos += 1
    return next


def KMPsearch(s, w):
    results = []

    m = 0
    i = 0
    next = KMPnext(w)

    while m + i < len(s):
        if w[i] == s[m + i]:
            if i == len(w) - 1:
                results.append(m)
                m += 1
                i = next[i]
            else:
                i += 1
        else:
            m = m + i - next[i]
            if next[i] != -1:
                i = next[i]
            else:
                i = 0

    return results

if __name__ == '__main__':
    print(KMPnext("aabbaabb"))

    print(KMPsearch("aabbaabb", "aab"))
