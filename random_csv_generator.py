#import sys
import csv
from faker import Faker

############################
#   Variables to change:
number_of_records = 4
number_of_files = 4

# Localized:
# If you need specify language for data, please try use it as argument for package.
# EXAMPLE: 
# fake = Faker(['pl_PL'])

#   Variables as argument (need to use 'import sys'):
# number_of_records = int(sys.argv[1])
# number_of_files = int(sys.argv[2])
############################



fake = Faker()

for i in range(number_of_files):
    with open(f'generated_data/data_{i}.csv', mode='a',newline='') as file:
        file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# CSV headers if required:
#  file_writer.writerow(['first_name', 'last_name', 'age'])

        for _ in range(number_of_records):
            file_writer.writerow([fake.first_name(), fake.last_name(), fake.numerify("####")])
