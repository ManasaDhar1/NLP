import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

stop_words = stopwords.words('english')

sentences = [
    "I LOVE this movie!!! #awesome #friday",
    "I Love movie, but the seats are bad",
    "LOVED it! Best Movie Ever"
]

stemmer = PorterStemmer()
output = []

for i in sentences:
    i = i.lower()
    i = re.sub(r"[^a-z\s]", "", i)
    words = i.split()
    words = [stemmer.stem(word) for word in words if word not in stop_words]
    output.append(words)

print("Processed words:", output)

positive_words = ["love", "best", "awesom", "good", "great"]
negative_words = ["bad", "worst", "boring", "poor"]

total_pos = 0
total_neg = 0

for words in output:
    for w in words:
        if w in positive_words:
            total_pos += 1
        if w in negative_words:
            total_neg += 1

if total_pos > total_neg:
    print("Overall Feedback is GOOD ")
else:
    print("Overall Feedback is BAD")
