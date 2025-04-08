import nltk
import string
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

speech = """My fellow citizens, today we gather as one people, united by a shared vision. We stand at the crossroads of history, where our choices will define the future. The strength of a nation is not measured by its wealth alone but by the courage of its people. We must rise above fear and embrace the opportunities before us.

Throughout history, we have seen the power of unity. When individuals come together with a common purpose, they can achieve the impossible. It is not the color of our skin, the language we speak, or the place of our birth that defines us, but the values we uphold. Let us choose unity over division, hope over despair, and action over complacency.

We must also recognize the challenges ahead. The road to progress is never easy, but with determination and resilience, we can overcome any obstacle. Education, innovation, and collaboration are the keys to building a better tomorrow. Our responsibility is not just to ourselves but to future generations who will inherit the world we shape today.

So, my friends, let us move forward with hope and determination. Let us build a society where justice, equality, and opportunity are not just ideals but realities for all. The future is in our hands, and together, we can make a difference. The time for action is now."""
tokens = word_tokenize(speech)
# print(tokens[:5]) 

stopwords = set(stopwords.words('english'))
filtered_tokens = []
for word in tokens:
    if word not in stopwords and word not in string.punctuation:
        filtered_tokens.append(word)
# print(filtered_tokens[:5])

lemmatizer = WordNetLemmatizer()
def get_wordnet_pos(word):
    """Map POS tag to WordNet's POS tag."""
    if word.startswith('V'):
        return wordnet.VERB
    elif word.startswith('N'):
        return wordnet.NOUN
    elif word.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
lemmatized_tokens = []
for word in filtered_tokens:
    lemmatized_tokens.append(lemmatizer.lemmatize(word, get_wordnet_pos(word[0])))
# print(lemmatized_tokens[:10])

processed_text = ' '.join(lemmatized_tokens)
# cv=CountVectorizer(max_features=50, binary=True, ngram_range=(1,2))
# x=cv.fit_transform([processed_text]).toarray()
# print(x)
tf=TfidfVectorizer(max_features=50, ngram_range=(1,2))
x=tf.fit_transform([processed_text]).toarray()
tf.vocabulary_
print(tf.vocabulary_)


