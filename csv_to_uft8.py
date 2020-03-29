import csv
from chardet.universaldetector import UniversalDetector


def get_encoding_info(file):
    with open(file, 'rb') as f:
        detector = UniversalDetector()
        for line in f.readlines():
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        return detector.result['encoding']


def read_csv(filename, encoding):
    res = []
    with open(filename, 'r', encoding=encoding, errors='ignore') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 1:
                row_content = row[0]
                if row_content != 'None':
                    row_content = row_content.replace('\n', '')
                    res.append([row_content])
    return res


def write_to_csv(filename, file_content):
    with open(filename, 'w') as f:
        csv_writer = csv.writer(f)
        for row in file_content:
            csv_writer.writerow(row)


if __name__ == '__main__':
    original_filename = '50_1(1).csv'
    dest_filename = 'haha.csv'
    original_encoding = get_encoding_info(original_filename)
    print("原始文件名： {0}, 目标文件名：{1}, 原始编码：{2}".format(original_filename, dest_filename, original_encoding))

    csv_content = read_csv(original_filename, original_encoding)

    write_to_csv(dest_filename, csv_content)
