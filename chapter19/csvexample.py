import csv


def main():
    print('Starting CSV Exmaple')
    print(csv.list_dialects())

    print('Creating CSV file')
    with open('sample.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['She Loves You', 'Sept', 1963])
        writer.writerow(['I Want to Hold Your Hand', 'Dec', 1963])
        writer.writerow(['Cant Buy Me Love', 'Apr', 1964])
        writer.writerow(['A Hard Days Night', 'July', ' 1964'])

    print('-' * 100)

    print('Starting to read csv file')
    with open('sample.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        # Process each row in the csv file
        for row in reader:
            row_length = len(row)
            print('row_length', row_length)
            if row_length != 3:
                print('Error in data (length is not 3):', row)
                print('In line:', reader.line_num)
            else:
                for i in range(row_length):
                    # Each element in the row can be accessed via an index
                    print(row[i], end=': ')
                print()
                try:
                    year = int(row[2].strip())
                    if year == 1964:
                        print('What a great year', row[0])
                except ValueError as exp:
                    print(exp)
                    print("issue in row ", reader.line_num)
                    print(row)

    print('Done Reading')

if __name__ == '__main__':
    main()