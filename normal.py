#casefolding
#lemmatization
#stemming

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
text = "pizzas"
res = lemmatizer.lemmatize(text)
print(res)