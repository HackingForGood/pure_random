def process_file(fname, f_list, p_list, directory):
    modified_data = []
    fieldnames = [x for x in f_list]
    for vals in p_list:
        fieldnames.append(vals)
    fieldnames.insert(0, 'UNITID')

    with io.open(fname + '.csv', 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader((l.encode('utf-8') for l in csvfile))
        for row in reader:
            modified_row = {}
            for field in fieldnames:
                modified_row[field] = row[field]
            modified_data.append(modified_row)

    # The processed files are written to the output directory.
    output_dir = directory + 'Processed/'
    utils.check_directory(output_dir)

    write_file = output_dir + fname + '_pruned.csv'
    with open(write_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in modified_data:
            writer.writerow(row)

    return output_dir
