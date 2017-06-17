import csv
import io

import utils

INPUT_DIR = "/Users/rakshitha/pure_random/dataFiles/"


def process_file(file_list, fieldname):  # f_list, p_list, directory):
    field_values = set()
    for ind_file in file_list:
        reader = csv.DictReader(open(INPUT_DIR + ind_file))
        for row in reader:
            value = row[fieldname].strip()
            if value == '':
                continue
            field_values.add(row[fieldname].strip())
    return list(field_values)


if __name__ == "__main__":
    file_names = ["Lok_Sabha_Government_Bills_as_on_20th_July_2013.csv",
                  "Lok_Sabha_Private_Bills_as_on_20th_July_2013.csv",
                  "Rajya_Sabha_Government_Bills_as_on_20th_June_2014.csv",
                  "Rajya_Sabha_Private_Bills_as_on_20th_June_2014.csv"]
    fieldnames = ["Ministry", "Year", "Status"]  # "Bill Category"]
    dir_list = [["Private_Bills", "Government_Bills"], ["Lok_Sabha", "Rajya_Sabha"]]
    for field in fieldnames:
        field_values = process_file(file_names, field)
        # print field
        # print len(field_values)
        # print field_values
        # print "*" * 10
        dir_list.append(field_values)

    # print dir_list
    DIR_path = "/Users/rakshitha/pure_random/pdfFiles/"
    for bill_type in dir_list[0]:
        for government in dir_list[1]:
            for ministry in dir_list[2]:
                for year in dir_list[3]:
                    for status in dir_list[4]:
                        output_dir = DIR_path + bill_type + "/" + government + "/" + ministry + "/" + year + "/" + status + "/"
                        utils.check_directory(output_dir)
