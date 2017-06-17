"""
General nlp code.
"""
import os, sys
import codecs, random, pprint
import gensim

from sm_utils import gen_utils, nlp_utils

data_dir = '/home/smysore/browsing_legislations/pdfs'
check_dir = '/home/smysore/browsing_legislations/check_dir'

def main():
	train_corpus_td = gen_utils.read_dir(data_dir)
	
	# Init model.111
	model = gensim.models.doc2vec.Doc2Vec(size=50, min_count=2, iter=10)

	# Build vocab.
	model.build_vocab(train_corpus_td)
	print('vocabulary size: {}'.format(len(model.wv.vocab)))

	# Actually train vectors.
	model.train(train_corpus_td, total_examples=model.corpus_count, epochs=model.iter)
	model.save(os.path.join(check_dir, 'model-large.doc2vec'))

if __name__ == '__main__':
	main()