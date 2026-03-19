
import nltk
from nltk import CFG
# Define the context-free grammar (CFG)
grammar = CFG.fromstring("""S -> NP VP
NP -> Det N | Det N PP
VP -> V NP | V NP PP
PP -> P NP
Det -> 'the' | 'a'
N -> 'cat' | 'dog' | 'park' | 'telescope'
V -> 'saw' | 'chased'
P -> 'in' | 'with'""")
# Create a Top-Down Parser
top_down_parser = nltk.parse.TopDownChartParser(grammar)
# Create a Bottom-Up Parser
bottom_up_parser = nltk.parse.BottomUpChartParser(grammar)
# Input sentence
tokens = ['the', 'cat', 'saw', 'a', 'dog', 'in', 'the', 'park']
print("Top-Down Parsing:")
for tree in top_down_parser.parse(tokens):
    print(tree)
    tree.pretty_print()
print("\nBottom-Up Parsing:")

for tree in bottom_up_parser.parse(tokens):
    print(tree)
    tree.pretty_print()