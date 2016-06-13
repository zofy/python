import csv

file_read = 'C:\\Users\Patrik\Desktop\\test_r.csv'
file_write = 'C:\\Users\Patrik\Desktop\\test_w.csv'


def read_write_csv(file_read, file_write):
    with open(file_read, 'rb') as f_r, open(file_write, 'wb') as f_w:
        r = csv.reader(f_r, delimiter=':')
        w = csv.writer(f_w, delimiter='\t')
        for row in r:
            if not row[0].strip().startswith('#'):
                print [row[0], row[2]]
                w.writerow([row[0], row[2]])


read_write_csv(file_read, file_write)
