import random


def shuffleArray(cards):
    '''
    shuffle an array of cards
    '''
    for i in range(len(cards) - 1):
        j = random.randrange(i + 1, len(cards))
        cards[i], cards[j] = cards[j], cards[i]

if __name__ == '__main__':
	cards = list(range(1, 11))
	shuffleArray(cards)
	print(cards)
