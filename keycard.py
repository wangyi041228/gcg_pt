import random


def work(deck):
    lst_deck_ori = list(deck)
    count = 0
    tries = 1_000_000
    for _ in range(tries):
        lst_deck = lst_deck_ori.copy()
        random.shuffle(lst_deck)
        open_hand = lst_deck[:5]

        set_blacklist = set(x.upper() for x in open_hand)
        # set_blacklist = set(open_hand)

        if 'A' in open_hand or 'a' in open_hand:
            count += 1
            continue
        new_hand_count = 0
        i = 5
        while new_hand_count < 5:

            card = lst_deck[i].upper()
            # card = lst_deck[i]

            if card == 'A':  # or card == 'a'
                count += 1
                break
            if card not in set_blacklist:
                new_hand_count += 1
            i += 1
    print(count / tries)


def work0():
    count = 0
    tries = 100_000
    deck = list(range(30))
    for _ in range(tries):
        a, b = random.sample(deck, 2)
        if a < 10 or b < 10:
            count += 1
    print(count / tries)


def main():
    decks = [
        'ABCDEFGHIJKLMNOabcdefghijklmno',
        'ABCDEFGHIJKLMNOPabcdefghijklmn',
        'ABCDEFGHIJKLMNOPQabcdefghijklm',
        'ABCDEFGHIJKLMNOPQRabcdefghijkl',
    ]
    for deck in decks:
        work(deck)


if __name__ == '__main__':
    main()
