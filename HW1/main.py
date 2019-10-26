from matplotlib import pyplot as plt 
from collections import Counter 
import math
import string
import huffman

# calculate probability
def Probability(freq):
    return round((freq / TotalLetter), 3)

# calculate entropy
def Entropy(pr):
    entropy = sum([p * math.log2(1 / p) for p in pr])
    return round(entropy, 3)

# read .txt file
with open("santaclaus.txt") as tf: 
    letter = tf.read()

LetterCount = Counter(letter.translate(str.maketrans('', '', string.punctuation)))
LetterCount = {k : LetterCount.get(k, 0) for k in string.printable}
LetterCount = {x : y for x, y in LetterCount.items() if y != 0}
TotalLetter = sum(LetterCount.values())

# calculate pmf
pmf = []
y = list(LetterCount.values())
for value in y:
    pmf.append(Probability(value))

print(Entropy(pmf), 'bits/symbol')    

x = list(LetterCount.keys())
x[22] = 'SP'
x[23] = 'CR'

# Huffman Encoding
chars_freqs = list(zip(x, y))
nodes = huffman.createNodes([item[1] for item in chars_freqs])
root = huffman.createHuffmanTree(nodes)
codes = huffman.huffmanEncoding(nodes, root)
print('codeword:')
for item in zip(chars_freqs, codes):
    print ('Letter: %s   Encoding Codeword: %s' % (item[0][0], item[1]))

plt.figure(1)
plt.xlabel('Letter')
plt.ylabel('Frequency')
plt.bar(x, y, color='b')

plt.figure(2)
plt.xlabel('Latter')
plt.ylabel('Probability')
plt.bar(x, pmf, color='b')

plt.show()