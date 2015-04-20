import random


def rand7():
    return random.randint(1, 8)


def rand10():
    currSum = 0
    while True:
        currSum = rand7() - 1
        currSum *= 7
        currSum += rand7() - 1

        if currSum <= 39:
            break

    return (currSum - 1) % 10 + 1

if __name__ == '__main__':
    from collections import Counter
    c = Counter([rand10() for x in range(1000)])
    print(c)
