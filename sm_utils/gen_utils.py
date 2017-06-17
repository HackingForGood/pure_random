"""
Just contains general utilities.
"""
import os, sys
import codecs, random, pickle, hashlib
import gensim
import nlp_utils

check_dir = '/home/smysore/browsing_legislations/check_dir'

def read_dir(input_dir, num_files=None):
    dir_text_td = list()
    fcount = 0

    flist = os.listdir(input_dir)
    if num_files is None:
        num_files = len(flist)
    
    map_writer = codecs.open(os.path.join(check_dir, 'fname_sha1_map.pd'), "w", "utf-8")
    file_hash_map = dict()
    random.shuffle(flist)
    for filename in flist:
        if filename.endswith(".txt") and fcount < num_files:
            cur_fname = os.path.join(input_dir, filename)
            with codecs.open(cur_fname, 'r', 'utf-8') as tfile:
                # Read in each line in file.
                doc_lines = tfile.readlines()
                # Clean each line and get bag of words for document.
                cleaned_doc_tok = nlp_utils.clean_doc(doc_lines)
                # Generate unique id for each document.
                doc_str = u' '.join(cleaned_doc_tok).encode('utf-8').strip()
                doc_sha1 = hashlib.sha1(doc_str).hexdigest()

                map_writer.write("{}\t{}".format(cur_fname, doc_sha1))

                # Create gensim tagged document.
                doc_td = gensim.models.doc2vec.TaggedDocument(cleaned_doc_tok, doc_sha1)
                yield doc_td
    