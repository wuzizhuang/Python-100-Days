import random

class card(object):

    def __init__(self,suite,face):
        self._suite = suite #花色
        self._face = face #牌面

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __show__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (self._suite,face_str)

    def __str__(self):
        return self.__show__()

# 定义扑克牌类
class Poker(object):

    def __init__(self):
        # 初始化一副扑克牌
        self._cards = [card(suite,face) for suite in '♠♥♣♦' for face in range(1,14)]
        self._current = 0
        self.initialize_deck()

    def initialize_deck(self):
        # 初始化牌堆并洗牌
        self._cards = [card(suite,face) for suite in '♠♥♣♦' for face in range(1,14)]
        self.shuffle()

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        return self._current < len(self._cards)

class Player(object):

    def __init__(self,name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get_card(self, deck, num = 4):
        draw_cards = set()
        while len(draw_cards) < num and deck.has_next:
            draw_cards.add(deck.next)
            if card not in draw_cards:
                self.cards_on_hand.append(card)

    def get(self,card):
        self._cards_on_hand.append(card)

    def arrange(self,card_key):
        self._cards_on_hand.sort(key = card_key)

def main():
    deck = Poker()
    deck.shuffle()
    player = Player('小明')
    player.get_card(deck,4)

