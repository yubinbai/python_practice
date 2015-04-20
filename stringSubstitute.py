'''
Replace all occurrence of the given pattern to 'X'. For example, given that
the pattern="abc", replace "abcdeffdfegabcabc" with "XdeffdfegX". Note that
multiple occurrences of abc's that are contiguous will be replaced with only one
'X'. 
'''


def find(s, pos, w):
    for i in range(len(w)):
        if s[pos + i] != w[i]:
            return False
    return True


def replace(s, w):
    target = []
    i = 0
    while i < len(s):
        if find(s, i, w):
            i += len(w)
            while i < len(s) - len(w) + 1 and find(s, i, w):
                i += len(w)
            target.append('X')
        else:
            target.append(s[i])
            i += 1
    return ''.join(target)


def replace2(s, w):  # in-place solution, sliding window
    source = list(s)
    i = 0
    j = 0
    while i < len(s):
        if find(s, i, w):
            i += len(w)
            while i < len(s) - len(w) + 1 and find(s, i, w):
                i += len(w)
            source[j] = 'X'
            j += 1
        else:
            source[j] = source[i]
            i += 1
            j += 1
    return ''.join(source[0:j])

if __name__ == '__main__':
    s = "abcdeffdfegabcabcabccbc"
    w = "abc"
    print(replace(s, w))
    print(replace2(s, w))
