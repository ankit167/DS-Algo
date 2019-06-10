#!/usr/bin/python


class TN:
    def __init__(self):
        self.isLeaf = False
	self.branch = {}
	for i in range(0, 26):
	    self.branch[chr(i+97)] = None


class T:
    def __init__(self):
        self.root = TN()

    #
    # Insert a word in Trie
    #
    def insert(self, word):
        pcrawl = self.root
	for ch in word:
	    if pcrawl.branch[ch] is None:
	        pcrawl.branch[ch] = TN()
	    pcrawl = pcrawl.branch[ch]
	pcrawl.isLeaf = True

    #
    # Search for a word in Trie
    #
    def search(self, word):
        pcrawl = self.root
	for ch in word:
	    if pcrawl.branch[ch] is None:
	        return False
	    pcrawl = pcrawl.branch[ch]
	return pcrawl is not None and pcrawl.isLeaf

    #
    # Generic function to print all words of a Trie. prefix is '',
    # by default (to print all words).
    # Set prefix paramter to print all words starting from a particular prefix
    #
    def printWords(self, prefix=''):
        pcrawl = self.root
	w = ''
	for ch in prefix:
	    if pcrawl.branch[ch] is None:
	        return False
	    w += ch
	    pcrawl = pcrawl.branch[ch]
	self.printAll(pcrawl, w)

    #
    # Utility function to print all the words in Trie with a given prefix 'w'
    #
    def printAll(self, pcrawl, w):
        if pcrawl is None:
	    return
	if pcrawl.isLeaf:
	    print w
	for ch in pcrawl.branch:
	    if pcrawl.branch[ch] is not None:
	        self.printAll(pcrawl.branch[ch], w+ch)

    #
    # Longest prefix in a string, which is also a word in Trie
    # Input: are area base cat cater children basement
    # Query: basemen
    # Output: base
    #
    def longestPrefixWord(self, word):
        prefix, w = '', ''
	if self.root is None:
	    return w
	pcrawl = self.root
	for ch in word:
	    if pcrawl.isLeaf is True:
		w += prefix
		prefix = ''
	    if pcrawl.branch[ch] is not None:
		prefix += ch
		pcrawl = pcrawl.branch[ch]
	    else:
		break
	if pcrawl.isLeaf is True:
	    w += prefix
	return w


def main():
    tr = T()
    l = raw_input().split()
    for word in l:
        tr.insert(word)
    s = raw_input()

if __name__ == '__main__':
    main()
