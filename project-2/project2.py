## Names: Alyssa Lim, Adoncia Ho, Lim Zhe Xun
## Matric numbers: U2330523D, U2330644K, U2121481K
## The following code gives some initial direction in building a POS-tagger using resources from the nltk library.

import nltk
from utils import *


class CustomBigramTagger(nltk.BigramTagger):
    def tag(self, tokens):
        # First use BigramTagger's default tagging
        tagged_tokens = super().tag(tokens)
        
        # Iterate through the tagged tokens
        for i in range(len(tagged_tokens) - 1):
            word, pos = tagged_tokens[i]
            next_word, next_pos = tagged_tokens[i + 1]
            
            if word == "u=" and next_pos == "v":
                tagged_tokens[i] = (word, "der=")  # Change the POS tag to "der="
            elif word == "ki=" and next_pos == "v":
                tagged_tokens[i] = (word, "der=")  # Change the POS tag to "der="
            elif word == "ka=" and next_pos == "v":
                tagged_tokens[i] = (word, "der=")  # Change the POS tag to "der="
            elif word == "i=" and next_pos == "v":
                tagged_tokens[i] = (word, "der=")  # Change the POS tag to "der="
        
        return tagged_tokens



# Load data
train_data = load_data("datasets/full_text.txt", tags=["mb", "ps"])
original_length = len(train_data)
test_data = load_data("datasets/test.txt", tags=["mb", "ps"])

# Remove test data from train data
for data in test_data:
    train_data.remove(data)
assert(len(train_data) == original_length - len(test_data))

# Format data for taggers
train = format_data(train_data)
test = format_data(test_data)


default_tagger = nltk.DefaultTagger("english")
unigram_tagger = nltk.UnigramTagger(train, backoff=default_tagger)
custom_tagger = CustomBigramTagger(train, backoff=unigram_tagger)


with open("output.txt", "w") as w:
    for n in list(range(10)):
        w.write(str(custom_tagger.accuracy(test))+"\n")
