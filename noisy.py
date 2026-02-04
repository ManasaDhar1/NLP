import nltk
from collections import Counter

word_counts = {
    "the": 500,
    "tea": 2000,
    "team": 1000,
    "ten": 50
}

summ = sum(word_counts.values())

def edit_distance(wrong_input, w):
    distance = nltk.edit_distance(wrong_input, w)
    if distance == 0:
        return 1.0
    return 1 / (10 ** distance)

def prior_probability(w):
    return word_counts.get(w, 0) / summ

def suggested(wrong_input):
    candidates = list(word_counts.keys())
    correct_word = None
    high_prob = -1

    for w in candidates:
        likelihood = edit_distance(wrong_input, w)
        prior = prior_probability(w)
        result = likelihood * prior

        if result > high_prob:
            high_prob = result
            correct_word = w

    return correct_word

wrong_input = "teame"
correction = suggested(wrong_input)
print(correction)
