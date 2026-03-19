
import nltk
from collections import defaultdict
from nltk.probability import FreqDist
# Training data
train_data = [
("fun, couple, love, love", "comedy"),
("fast, furious, shoot", "action"),
("couple, fly, fast, fun, fun", "comedy"),
("furious, shoot, shoot, fun", "action"),
("fly, fast, shoot, love", "action")
]
# Tokenize and prepare vocabulary
nltk.download('punkt')
category_words = defaultdict(list)
all_words = set()
category_counts = defaultdict(int)


for text, category in train_data:
    words = text.split(', ')
    category_words[category].extend(words)
    all_words.update(words)
    category_counts[category] += 1


total_docs = len(train_data)
total_vocab = len(all_words)

priors = {category: category_counts[category] / total_docs for category in category_counts}

likelihoods = {}
for category in category_words:
    freq_dist = FreqDist(category_words[category])
    total_category_words = len(category_words[category])
    likelihoods[category] = {word: (freq_dist[word] + 1) / (total_category_words +

total_vocab) for word in all_words}

# Classify new document D
D = "fast, couple, shoot, fly"
D_words = D.split(', ')

posteriors = {}
for category in category_words:
    posterior = priors[category] # Start with the prior
    for word in D_words:
        posterior *= likelihoods[category].get(word, 1 / (len(category_words[category]) +
        total_vocab))
    posteriors[category] = posterior

# Determine the most likely category
predicted_category = max(posteriors, key=posteriors.get)
print("Predicted category for D:", predicted_category)

# Output probabilities
print("Posterior probabilities:")
for category, prob in posteriors.items():
    print(f"{category}: {prob}")