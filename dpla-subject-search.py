''' Queries DPLA API to find out how many records use a given subject term, and how many
institutions those records are contributed by. Accepts a list of subjects, and outputs a
tab-delimited file with subjects, number of records, and number of contributors.
'''

import requests
from time import sleep
from urllib.parse import quote
from credentials import *

# Read subjects file
file = open('subjects.txt', 'r')
subjects = file.readlines()

# Open file to write results
with open('results.txt', 'w') as results_file:
    results_file.write('SUBJECT\tNO. OF RESULTS\tNO. OF CONTRIBUTORS\n')  # Add header row

# Iterate through each subject
    for subject in subjects:
        subject = subject.strip()
        if (len(subject) <= 198):
            subject_url = quote(subject)  # URL-encode
            print(subject)

            api_url = ('https://api.dp.la/v2/items?sourceResource.subject.name=%22' + subject_url +
                       '%22&api_key=' + DPLA_KEY + '&facets=dataProvider&facet_size=100&exact_field_match=true')
            response = requests.get(api_url).json()

            count = response['count']
            print(count)

            contributors = response['facets']['dataProvider']['terms']
            contributor_count = len(contributors)
            print(contributor_count)

            results_file.write(subject + '\t' + str(count) + '\t' + str(contributor_count) + '\n')

            sleep(0.25)
        else:
            print(subject + '\nERROR - String length not valid')
            results_file.write(subject + '\tERROR - String length not valid\n')

results_file.close()
