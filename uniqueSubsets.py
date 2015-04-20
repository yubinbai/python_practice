def subsets(seq):
    def _subsets(step):
        results.append(list(path))
        for i in range(step, len(seq)):
            if i != step and seq[i] == seq[i - 1]:
                continue
            path.append(seq[i])
            _subsets(i + 1)
            path.pop()
    seq = list(seq)
    seq.sort()
    results = []
    path = []
    _subsets(0)
    return results

if __name__ == '__main__':
    seq = 'abbcdefghijklmnopqrstuvw'
    print len(subsets(seq))

    # seq = [1, 2, 2]
    # for i in subsets(seq):
    #     print(i)
