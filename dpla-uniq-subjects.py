import requests
from time import sleep
from urllib.parse import quote
from credentials import *

# Set parameters for API call
# In source, for hub, use 'provider='; for institutions, use 'dataProvider='
source = 'dataProvider="UTSA Libraries Special Collections"'
facet_size = 1000  # number of subjects to retrieve, max 2000

# Create API call and make request
api_url = ('https://api.dp.la/v2/items?' + source + '&api_key=' + DPLA_KEY
           + '&facets=sourceResource.subject.name&facet_size=' + str(facet_size) + '&page_size=0')
print(api_url)
response = requests.get(api_url).json()

# Get subjects from response
subjects = response['facets']['sourceResource.subject.name']['terms']

# Open file to write results
with open('uniq_subjects.txt', 'w', encoding='utf-8') as results_file:
    results_file.write('UNIQUE SUBJECTS\n')  # Add header row
    number_uniq = 0
    number_subjects = len(subjects)

# Iterate through each subject
    for subject in subjects:
        subject_term = subject['term'].strip()

        if (len(subject_term) <= 198):
            subject_url = quote(subject_term)  # URL-encode

            # Make API call to get contributors per subject term
            api_url = ('https://api.dp.la/v2/items?sourceResource.subject.name=%22' + subject_url +
                       '%22&api_key=' + DPLA_KEY + '&facets=dataProvider&facet_size=20&exact_field_match=true&page_size=0')
            response = requests.get(api_url).json()

            # Count number of contributors for this term
            contributors = response['facets']['dataProvider']['terms']
            contributor_count = len(contributors)
            try:
                print(subject_term + ' ' + str(contributor_count))
            # If the subject term contains a unicode character that can't display in console
            except UnicodeError:
                print('**UNICODE ERROR** ' + str(contributor_count))

            # If unique, write to results file
            if contributor_count == 1:
                results_file.write(subject_term + '\n')
                number_uniq += 1  # add 1 to counter

            sleep(0.1)

        else:
            print(subject_term + ' ERROR: String too long')

    percent_uniq = "{:.2%}".format(number_uniq/number_subjects)
    print('***' + percent_uniq + ' unique***')
    results_file.write('~~~~~~~~~~~\n')
    results_file.write('PERCENT UNIQ: ' + percent_uniq + ' (' + str(number_uniq) + '/' +
                       str(number_subjects) + ')')

results_file.close()
