import collections
import random

hand_size = 13
Card = collections.namedtuple('Card', ['rank', 'suit'])
Bid = collections.namedtuple('Bid', ['level', 'suit'])
rankVal = {'2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, '10':8,
        'J':9, 'Q':10, 'K':11, 'A':12}
suitVal = {'NoTrump':4, 'Spades':3, 'Hearts':2, 'Diamonds':1, 'Clubs':0}
playerDict = {0:'N', 1:'E', 2:'S', 3:'W'}

def cardKey(Card, trumpSuit=None, leading_suit=None):
    if trumpSuit == None and leading_suit == None:
        return rankVal[Card[0]]

    elif trumpSuit == 'NoTrump':
        if Card[1] == leading_suit:
            return rankVal[Card[0]]
        else:
            return 0

    elif leading_suit != None:
        if Card[1] == trumpSuit:
            return rankVal[Card[0]]+13
        if Card[1] == leading_suit:
            return rankVal[Card[0]]
        else:
            return 0

    else:
        if Card[1] == trumpSuit:
            return rankVal[Card[0]]+13
        else:
            return rankVal[Card[0]]





class Hand:
    def __init__(self, list_of_cards):
        self.cards = { 'Spades' : [], 'Hearts' : [], 'Diamonds' : [], 
                'Clubs' : [] }
        for card in list_of_cards:
            self.cards[card[1]].append(card)
        for suit in self.cards:
            self.cards[suit].sort(key=cardKey, reverse=True)

    def has(self, suit):
        if len(self.cards[suit]):
            return True
        else:
            return False

    def __str__(self):
        def getRanks(suit):
            ranks = []
            for card in suit:
                ranks.append(card[0])
                ranks.append(', ')
            return ''.join(ranks)[:-2]

        spades_str = 'Spades: ' + getRanks(self.cards['Spades'])
        hearts_str = 'Hearts: ' + getRanks(self.cards['Hearts'])
        diamonds_str = 'Diamonds: ' + getRanks(self.cards['Diamonds'])
        clubs_str = 'Clubs: ' + getRanks(self.cards['Clubs'])
        return f'{spades_str}\n{hearts_str}\n{diamonds_str}\n{clubs_str}'


class Deck:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks ]

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self):
        players = []
        pointer = 0
        for player in range(4):
            cards_to_be_dealt = self._cards[pointer:(pointer+13)]
            pointer += 13
            players.append(Hand(cards_to_be_dealt))
        return players

class Auction:
    def __init__(self, playerList):
        self._bidlist = []
        self._declarer = None
        self._playerList = playerList

    def _contractAccepted(self):
        if len(self._bidlist)>=4 and set(self._bidlist[-3:]).issubset(set(['pass'])) :
            # print('accepted')
            return True
        else:
            # print('not accepted')
            return False

    def _isLarger(self, bid):
        if set(self._bidlist).issubset(set(['pass'])):
            return True
        i = -1
        while self._bidlist[i] == 'pass':
            i -= 1
        # print('last valid bid: ', self._bidlist[i])
        if (self._bidlist[i][0]*5+ suitVal[self._bidlist[i][1]] < 
                bid[0]*5+suitVal[bid[1]]):
            # print(self._bidlist[i])
            # print('larger!')
            return True
        else:
            return False

    def bid(self):
        playerCounter = 0
        print('Player 1 starts bidding.')
        while not self._contractAccepted():
            while not self._newBid(playerCounter, self._playerList[playerCounter]):
                pass
            playerCounter += 1
            playerCounter = playerCounter % 4
        self._declarer = playerCounter
        print('Final contract:', self._lastBid())
        print('Delcarer:', playerDict[self._declarer])

    def declarer(self):
        return player
    def _lastBid(self):
        i = -1
        while self._bidlist[i] == 'pass':
            i -= 1
        return self._bidlist[i]

    def _newBid(self, player, hand):
        # print(self._bidlist)
        print('=====================================================')
        print(f'player {playerDict[player]}\'s bid!')
        print('Your hand:\n')
        print(hand, '\n')
        print('Your bid:')
        level = input('Level (1~7 or pass): ')
        if (level == 'pass' and set(self._bidlist[:3]).issubset(set(['pass']))
                and len(self._bidlist) == 3):
            print('Pass out!')
            print('=====================================================')
            raise Exception('PassOut')
        elif level == 'pass':
            self._bidlist.append('pass')
            print('Your bid: Pass\n')
            print('=====================================================')
            return True
        elif level.isdecimal() and 0 < int(level) < 8:
            level = int(level)
            suit = input('Suit (s/h/d/c/nt): ')
            if suit == 's' and self._isLarger(Bid(level, 'Spades')):
                self._bidlist.append(Bid(level, 'Spades'))
                print('Your bid: ', self._bidlist[-1], '\n')
                print('=====================================================')
                return True
            if suit == 'h' and self._isLarger(Bid(level, 'Hearts')):
                self._bidlist.append(Bid(level, 'Hearts'))
                print('Your bid: ', self._bidlist[-1], '\n')
                print('=====================================================')
                return True
            if suit == 'd' and self._isLarger(Bid(level, 'Diamonds')):
                self._bidlist.append(Bid(level, 'Diamonds'))
                print('Your bid: ', self._bidlist[-1], '\n')
                print('=====================================================')
                return True
            if suit == 'c' and self._isLarger(Bid(level, 'Clubs')):
                self._bidlist.append(Bid(level, 'Clubs'))
                print('Your bid: ', self._bidlist[-1], '\n')
                print('=====================================================')
                return True
            if suit == 'nt' and self._isLarger(Bid(level, 'NoTrump')):
                self._bidlist.append(Bid(level, 'NoTrump'))
                print('Your bid: ', self._bidlist[-1], '\n')
                print('=====================================================')
                return True
        print('Invalid bid!')
        print('=====================================================')
        return False

class Tricks:
    def __init__(self, auction):
        self._scoreTable = {'EW':[], 'NS':[]}
        self._declarer = auction._declarer
        self._playerList = auction._playerList
        self._cardTable = []
        self._trumpSuit = auction._lastBid()[1]
        self._contract = auction._lastBid()
    
    def declarer(self):
        return playerDict[self._declarer]

    def dummy(self):
        return playerDict[(self._declarer+2)%4]

    def _newTrick(self, opener, n_of_trick):
        print('\n\n\n\n\n\n>>> New Trick! Trick number', n_of_trick)
        cards = [None, None, None, None]
        leadingCard = self._playCard(self._playerList[opener], opener)
        leadingSuit = leadingCard[1]
        # print(leadingSuit)
        cards[opener] = leadingCard

        for i in range(1, 4):
            playerNumber = (opener+i)%4
            cards[playerNumber] = self._playCard(
                    self._playerList[playerNumber], playerNumber, leadingSuit)

        keys = []
        for t in cards:
            keys.append(cardKey(t, self._trumpSuit, leadingSuit))

        print(keys)
        self._cardTable.append(cards)
        winner =  keys.index(max(keys))
        print('winner:', winner)
        print('>>> {} won the trick!'.format(playerDict[winner]))
        if winner in (1, 3):
            self._scoreTable['EW'].append(n_of_trick)
        if winner in (0, 2):
            self._scoreTable['NS'].append(n_of_trick)
        return winner

    def _illegalCard(self, card, hand, leadingSuit):
        # print(leadingSuit)
        # print(card)
        # print(card[0])
        # print(card[1:])
        # print(not card[0] in 'SHDC')
        # print(not card[1:] in ['2', '3', '4', '5', '6', 
            # '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] )
        # print()
        if (not card[0] in 'SHDC') or (not card[1:] in ['2', '3', '4', '5', '6', 
            '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] ):
            print('illegalInput')
            return True
        
        cardDict = {'S':'Spades', 'H': 'Hearts', 'D':'Diamonds', 'C':'Clubs'}

        c = Card(card[1:], cardDict[card[0]])
        print('>>> your card:', c)
        # print(hand.cards['Spades'])

        if not ( (c in hand.cards['Spades']) 
            or (c in hand.cards['Hearts']) 
            or (c in hand.cards['Diamonds'])
            or (c in hand.cards['Clubs'])):
            print('no such card')
            return True

        if leadingSuit != None and hand.has(leadingSuit) and leadingSuit != c[1]:
            if c[0] != leadingSuit:
                return True

        return False
        card = card.upper()

    def _playCard(self, player, playerNumber, leadingSuit=None):
        print('=====================================================')
        print('>>> {}\'s turn! Here are your cards:'.format(playerDict[playerNumber]))
        print(player)
        userInputCard = input('Card: ').upper()
        while self._illegalCard(userInputCard, player, leadingSuit):
            userInputCard = input('illegal card! Please try again:').upper()
        cardDict = {'S':'Spades', 'H': 'Hearts', 'D':'Diamonds', 'C':'Clubs'}
        card = Card(userInputCard[1:], cardDict[userInputCard[0]])
        player.cards[card[1]].remove(card)
        return card
        
    def play(self):
        next_leader = (self._declarer+1)%4
        for i in range(1, 14):
            next_leader = self._newTrick(next_leader, i)
            
            if (self._declarer in (0, 2)):
                if (len(self._scoreTable['NS']) >= self._contract[0]+6 ):
                    print('NS has made the contract and won!')
                    exit()
                if (len(self._scoreTable['EW']) >= 8-self._contract[0] ):
                    print('NS has failed to make the contract. EW won!')
                    exit()

            if (self._declarer in (1, 3)):
                if (len(self._scoreTable['EW']) >= self._contract[0]+6 ):
                    print('EW has made the contract and won!')
                    exit()
                if (len(self._scoreTable['NS']) >= 8-self._contract[0] ):
                    print('EW has failed to make the contract. NS won!')
                    exit()



    

