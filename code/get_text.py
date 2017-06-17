import subprocess


def convertToText(data):
    for line in data:
        pdf_file_name = line.strip() + '.pdf'
        text_file_name = line.strip() + '.txt'
        p = subprocess.Popen(["pdftotext", pdf_file_name, text_file_name], stdout=subprocess.PIPE)
        output, err = p.communicate()
        # import pdb
        # pdb.set_trace()
        print output
        print err
        if err:
            # import pdb
            # pdb.set_trace()
            return []

if __name__ == "__main__":
    fp = open("/home/rbhat/pure_random/code/downloaded_files")
    data = fp.readlines()
    convertToText(data)