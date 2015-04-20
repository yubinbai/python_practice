# n peg hanoi tower problem, use bfs instead of dfs, and don't have a full
# analytical solution
import sys
import copy


def solutionWorks(currentSolution, stacksAfterSolution, initialStacks, finalStacks):
    for x in range(len(currentSolution)):
        i, j = currentSolution[x]
        stacksAfterSolution[j].append(stacksAfterSolution[i].pop())

    if str(stacksAfterSolution) == str(finalStacks):
        return True
    else:
        return False


def stepLegitimate(stacksAfterSolution, i, j):
    if len(stacksAfterSolution[i]) == 0 or \
            (len(stacksAfterSolution[j]) > 0 and stacksAfterSolution[i][-1] > stacksAfterSolution[j][-1]):
        return False
    return True

# DFS cannot work, need to use BFS


def moveDiscs(initialStacks, finalStacks, results):
    import collections
    solutions = collections.deque()
    solutions.append([])
    K = len(initialStacks) - 1

    while len(solutions) > 0:
        currentSolution = copy.deepcopy(solutions.popleft())

        if len(currentSolution) > 7:
            continue

        stacksAfterSolution = copy.deepcopy(initialStacks)
        if solutionWorks(currentSolution, stacksAfterSolution, initialStacks, finalStacks):
            for x in range(len(currentSolution)):
                results.append(list(currentSolution[x]))
            return

        # add other solutions in queue
        for i in range(1, K + 1):
            for j in range(1, K + 1):
                if j != i and stepLegitimate(stacksAfterSolution, i, j):
                    currentSolution.append([i, j])
                    solutions.append(copy.deepcopy(currentSolution))
                    currentSolution.pop()


if __name__ == '__main__':
    # N, K = [int(x) for x in sys.stdin.readline().split()]
    N, K = 6, 4
    initialStacks = [[] for x in range(K + 1)]
    finalStacks = [[] for x in range(K + 1)]

    # initial = [int(x) for x in sys.stdin.readline().split()]
    # final = [int(x) for x in sys.stdin.readline().split()]
    initial = [4, 2, 4, 3, 1, 1]
    final = [1, 1, 1, 1, 1, 1]

    for i in range(N - 1, -1, -1):
        initialStacks[initial[i]].append(i + 1)

    for i in range(N - 1, -1, -1):
        finalStacks[final[i]].append(i + 1)

    print(initialStacks)
    print(finalStacks)

    results = []
    moveDiscs(initialStacks, finalStacks, results)
    print(len(results))
    for i in range(len(results)):
        print(results[i][0], results[i][1])
