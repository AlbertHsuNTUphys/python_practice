from ob import *

if __name__ == "__main__":
    # Game starts
    print('New game!')

    # Deal
    deck = Deck()
    deck.shuffle()
    players = deck.deal()

    # Bid
    auction = Auction(players)
    auction.bid()

    # Play
    tricks = Tricks(auction)
    tricks.play()


