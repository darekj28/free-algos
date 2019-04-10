from instream import InStream
from wordnet import WordNet


class Outcast:
    # constructor takes a WordNet object
    def __init__(self, wordnet):

    # given an array of WordNet nouns, return an outcast as a string. 
    def outcast(self, nouns):


if __name__ == "__main__":
    wordnet = WordNet(sys.argv[1], sys.argv[2])
    outcast = Outcast(wordnet)
    for t in range(3, len(sys.argv)):
        nouns = InStream.readStrings(args[t])
        print(args[t] + ": " + outcast.outcast(nouns))