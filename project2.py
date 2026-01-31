import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stop_words = stopwords.words('english')

lemmat = PorterStemmer()

text = "The quick BROWN foxes... they are JUMPING over the 10 lazy dogs!"

text = re.sub(r"[^a-zA-Z\s]", "", text)
words = text.lower().split()

res1= [lemmat.stem(word) for word in words]
res = [word for word in res1 if word not in stop_words]
print(res)