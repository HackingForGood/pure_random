from nltk.corpus import stopwords
from string import punctuation

NOUN_POS_TAGS = ("NN", "NNP", "NNPS", "NNS")
STOP_WORDS = set(stopwords.words('english'))
PUNCTUATIONS = set(unicode(punctuation))
