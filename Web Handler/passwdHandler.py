import csv

class credentials(object):
    def read(self, file):
        try:
            with open(file) as csvFile:
                reader = csv.DictReader(csvFile)
                for row in reader:
                    password = row['Password']
                    username = row['Username']
                    IP = row['IP']
                    return username, password, IP
        except IOError:
            fieldnames = ['Username', 'Password', 'IP']
            credentials().create(file, fieldnames)

    def create(self, file, fieldnames):
        with open(file, 'w') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames)
            writer.writeheader()

def main():
    cred = credentials()
    cred.read('credentials.csv')

if __name__ == '__main__':
    main()
