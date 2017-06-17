import os

from FrequencySummarizer import *


def pre_process_pdfs(pdf_dir_path, pre_processed_pdf_dir_path):

    for pdf_file_name in os.listdir(pdf_dir_path):
        print pdf_file_name
        pdf_file_text = []
        with codecs.open(os.path.join(pdf_dir_path, pdf_file_name), "r", "utf-8-sig") as pdf_file:
            for line in pdf_file:
                pdf_file_text.append(line.lower().strip())
        pre_processed_pdf_file = codecs.open(os.path.join(pre_processed_pdf_dir_path, pdf_file_name), "w", "utf-8-sig")
        for pdf_file_line in nltk.sent_tokenize(" ".join(pdf_file_text)):
            pre_processed_line = " ".join([word for word in nltk.word_tokenize(pdf_file_line) if
                                           word not in Constants.STOP_WORDS])
            pre_processed_pdf_file.write(pre_processed_line + "\n")


def main():
    pre_process_pdfs("../data/pdfs/", "../data/pre_processed_pdfs/")
    frequency_summarizer = FrequencySummarizer()
    summary = frequency_summarizer.summarize(
        text_path="../data/pre_processed_pdfs/75_2005.pdf.txt", n=4)
    print "\n".join(summary)
    pass


if __name__ == '__main__':
    main()
