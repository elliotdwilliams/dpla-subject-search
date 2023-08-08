from time import sleep
from dpla.api import DPLA
from credentials import *

# Create DPLA object using dpla module and your API key
dpla = DPLA(DPLA_KEY)

# Read subjects file
file = open('subjects.txt', 'r')
subjects = file.readlines()

# Iterate through each subject
with open('results.txt', 'w') as results_file:
    for subject in subjects:
        subject = subject.strip()
        print(subject)
        fields = {"sourceResource.subject.name" : subject}
        results = dpla.search(searchFields = fields)
        count = results.count
        print(count)

        results_file.write(subject+'\t'+str(count)+'\n')

        sleep(0.5)

results_file.close()