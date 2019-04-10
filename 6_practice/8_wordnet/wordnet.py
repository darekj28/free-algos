import sys
from instream import InStream
from kosaraju_sharir_scc import SCC
from digraph_edge_list import Digraph
from sap import SAP

class WordNet:
	# constructor takes the name of the two input files
	def __init__(self, synsets, hypernyms):
		

	# returns all WordNet nouns as a list of strings.
	def nouns(self):

	# is the word a WordNet noun?
	def isNoun(self, word):

	# distance between nounA and nounB (defined below)
	def distance(self, nounA, nounB):

	# a synset (second field of synsets.txt) that is the common ancestor of nounA and nounB
	# in a shortest ancestral path (defined below)
	def sap(self, nounA, nounB):

if __name__ == "__main__":
	synsets = sys.argv[1]
	hypernyms = sys.argv[2]
	word_net = WordNet(synsets, hypernyms)
	nounA = sys.argv[3]
	nounB = sys.argv[4]
	print("(" + str(word_net.distance(nounA, nounB)) + ")", nounA, nounB)
	print(word_net.sap(nounA, nounB))


