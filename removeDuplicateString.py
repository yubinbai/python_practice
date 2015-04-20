import operator


def removeDuplicate(source):
    target = []
    charSet = set()
    for x in range(len(source)):
        if source[x] not in charSet:
            charSet.add(source[x])
            target.append(source[x])
    return ''.join(target)


def lastOccurance(source):
    target = []
    charSet = {}
    for x in range(len(source)):
        charSet[source[x]] = x
    sortedSet = sorted(charSet.items(), key=operator.itemgetter(1))
    return ''.join(c[0] for c in sortedSet)

if __name__ == '__main__':
    s = 'adfeggasdfshello'
    print(s)
    print(lastOccurance(s))
    print(s)
    print(removeDuplicate(s))
