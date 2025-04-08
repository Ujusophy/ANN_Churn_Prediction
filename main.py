# import nltk
# import pandas as pd
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# from nltk import ne_chunk, pos_tag, word_tokenize
# from nltk.stem import PorterStemmer
# from nltk.corpus import stopwords
# # nltk.download('stopwords')
# stop=['Techynurse is the best Gen AI tutor']
# stopwords.stop('english')
words=['eating', 'eat', 'eater', 'writing', 'written', 'fly', 'flew']
# pos= noun-n, verb-v, adjective-a, adverb-r
# from nltk.stem import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize('eating', pos='v'))
# for word in words:
#     print(word+" : " + lemmatizer.lemmatize(word, pos='v'))

# from nltk.stem import PorterStemmer
# stemmer = PorterStemmer()
# for word in words:
#     print(word+" : " + stemmer.stem(word))

# from nltk.stem import RegexpStemmer
# reg_stemmer = RegexpStemmer('ing$|s$|e$|able$', min=4)
# reg_stemmer.stem('eating')
# print(reg_stemmer.stem('eating'))

# from nltk.stem import SnowballStemmer
# snowball = SnowballStemmer('english')
# print(snowball.stem('eating'))

# for word in words:
#     print(word+" : " + snowball.stem(word))
# corpus = """Hello, my name is techynurse
# I just started my genai journey
# """

# from nltk.tokenize import wordpunct_tokenize

# # Tokenize the corpus into sentences and print the output
# print(wordpunct_tokenize(corpus))



