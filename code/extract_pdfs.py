import csv
import urllib2

import signal

DIR_path = "/Users/rakshitha/pure_random/pdfFiles/"
INPUT_DIR = "/Users/rakshitha/pure_random/dataFiles/"

def handler(signum, frame):
    print "time limit exceeded"
    raise Exception("Time limit exceeded")

def validate_pdf():
    pdf_downloaded = 0
    invalid_pdf = 0
    file_names = ["Lok_Sabha_Government_Bills_as_on_20th_July_2013.csv",
                  "Lok_Sabha_Private_Bills_as_on_20th_July_2013.csv",
                  "Rajya_Sabha_Government_Bills_as_on_20th_June_2014.csv",
                  "Rajya_Sabha_Private_Bills_as_on_20th_June_2014.csv"]
    # fieldnames = ["Ministry", "Year", "Status"]
    dir_list = [["Private_Bills", "Government_Bills"], ["Lok_Sabha", "Rajya_Sabha"]]
    for bill_type in dir_list[0]:
        for house in dir_list[1]:
            for file_name in file_names:
                if house + "_" + bill_type in file_name:
                    reader = csv.DictReader(open(INPUT_DIR + file_name))
                    for row in reader:
                        ministry_val = row["Ministry"]
                        if ministry_val == '':
                            continue
                        year_val = row["Year"]
                        if year_val == '':
                            continue
                        status_val = row["Status"]
                        if status_val == '':
                            continue
                        if "URL for Bills as Introduced" in row and ".pdf" in row["URL for Bills as Introduced"]:
                            url = row["URL for Bills as Introduced"]
                            request = urllib2.Request(url)
                            try:
                                signal.alarm(60)
                                response = urllib2.urlopen(request)
                                pdf_downloaded += 1
                                pdf_path = DIR_path + bill_type + "/" + house + "/" + ministry_val \
                                           + "/" + year_val + "/" + status_val + "/" + str(
                                    pdf_downloaded)
                                pdf_file = download_file(url, pdf_path)
                                print pdf_file
                                signal.alarm(0)
                            except urllib2.HTTPError:
                                invalid_pdf += 1
                            except urllib2.URLError:
                                invalid_pdf += 1
                            except:
                                invalid_pdf += 1


#
# for line in input_pdf_info:
#         # if valid_url_count == 20:
#         #     break
#         split_info = line.split()
#         url = split_info[-1].strip()
#         request = urllib2.Request(url)
#         try:
#             response = urllib2.urlopen(request)
#             valid_pdf.write(line + '\n')
#             valid_url_count += 1
#             first_author_last_name = split_info[1].split(',')[0].split('_')[-1]
#             title = split_info[2]
#             pdf_name = first_author_last_name + '|' + title
#             download_file(url, pdf_name)
#             email_list = convertToText(pdf_name)
#             if len(email_list) > 0:
#                 email_pdf.write(line + '\n')
#                 email_id_string = ','.join(email_list)
#                 email_id_info.write(email_id_string + "\t" + pdf_name + "\t" + split_info[1] + "\t" + split_info[3])
#             if valid_url_count % records == 0:
#                 print ("Processed %d valid urls " % valid_url_count)
#             valid_pdf.write(line + '\n')
#         except urllib2.HTTPError:  # 404, 500, etc..
#             invalid_pdf.write(url + '\n')
#             invalid_url_count += 1
#             if invalid_url_count % records == 0:
#                 print "Processed %d invalid urls " % invalid_url_count
#         except urllib2.URLError:
#             invalid_pdf.write(url + '\n')
#             invalid_url_count += 1
#             if invalid_url_count % records == 0:
#                 print "Processed %d invalid urls " % invalid_url_count
#         except:
#             invalid_pdf.write(url + '\n')
#             invalid_url_count += 1
#             if invalid_url_count % records == 0:
#                 print "Processed %d invalid urls " % invalid_url_count
#             print "Other error ", url
#
#
def download_file(download_url, f_path):
    response = urllib2.urlopen(download_url)
    path_name = f_path + ".pdf"
    pdf_file = open(path_name, 'w')
    # pdf_file = open("/iesl/data/oprev/dblp/pdfs/" + f_name + ".pdf", 'w')
    pdf_file.write(response.read())
    pdf_file.close()
    return f_path


if __name__ == "__main__":
    signal.signal(signal.SIGALRM, handler)
    validate_pdf()
