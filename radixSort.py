from math import log


def getDigit(num, base, digit_num):
    # pulls the selected digit
    return (num // base ** digit_num) % base


def makeBlanks(size):
    # create a list of empty lists to hold the split by digit
    return [[] for i in range(size)]


def split(a_list, base, digit_num):
    buckets = makeBlanks(base)
    for num in a_list:
        # append the number to the list selected by the digit
        buckets[getDigit(num, base, digit_num)].append(num)
    return buckets

# concatenate the lists back in order for the next step


def merge(a_list):
    new_list = []
    for sublist in a_list:
        new_list.extend(sublist)
    return new_list


def maxAbs(a_list):
    # largest abs value element of a list
    return max(abs(num) for num in a_list)


def radixSort(a_list, base):
    # there are as many passes as there are digits in the longest number
    passes = int(log(maxAbs(a_list), base) + 1)
    new_list = list(a_list)
    for digit_num in range(passes):
        new_list = merge(split(new_list, base, digit_num))
    return new_list

if __name__ == '__main__':
    import random
    aList = [random.randint(0, 10000) for x in range(100)]
    sortedList = radixSort(aList, 10)
    print sortedList
    for i in range(len(sortedList) - 1):
        if sortedList[i] > sortedList[i + 1]:
            print("Error")
