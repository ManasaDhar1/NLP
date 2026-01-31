import nltk

from nltk.corpus import stopwords

nltk.download('stopwords')

stop_words = stopwords.words('english')

text = "This is a sample sentence."

words = text.lower().split()

res = [word for word in words if word not in stop_words]

print(res)