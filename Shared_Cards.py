def parseDecklist(filename):
    startParsing = False;

    deck = []
    commander = ''
    deckname = ''

    with open(filename, 'r') as decklist: 
        for line in decklist:
            line = line.strip();
            if (line): 
                if startParsing: 
                    deck.append(line)

                if (line == 'Deck'):
                    startParsing = True;
    return deck

def calculateSharedCards(deck1, deck2):
    set1 = set(deck1)
    set2 = set(deck2)
    return set1.intersection(set2)

def writeToNewFile(decklist): 
    with open("DeckDoppel.txt", "w+") as resultList:
        for line in decklist:
            resultList.write(line);
            resultList.write("\n")

def diffDecks(): 
    deck1 = parseDecklist('Deck1.txt')
    deck2 = parseDecklist('Deck2.txt')

    comparison = calculateSharedCards(deck1, deck2)
    writeToNewFile(comparison)


if __name__ == '__main__':

    diffDecks()

