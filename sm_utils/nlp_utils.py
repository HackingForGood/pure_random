"""
NLPey utilities.
"""
import os, sys
import codecs, random, pprint, string

from nltk.corpus import stopwords

def clean_doc(doc_lioli, remove_stop=True, remove_punct=True):
	"""
	Clean document and return; Cleaning involves removing stop words and 
	punctuation if asked for; else just lowercase the text.
	"""
	# Get english stop words and punctuation.
	stop = set(stopwords.words('english'))
	punct = set(unicode(string.punctuation))
	
	doc_bow = list()
	for line in doc_lioli:
		line = line.strip()
		if len(line) > 5:
			# Blanket case; just lowercase everything.
			proc_line = line.lower()
			if remove_stop:
				# Include token in result if its not a stop word
				line = u' '.join([tok for tok in proc_line.split() if tok not in stop])
			if remove_punct:
				# Include character in result if its not a punctuation mark.
				line = u''.join(ch for ch in proc_line if ch not in punct)
			doc_bow.extend(line.split())
	return doc_bow