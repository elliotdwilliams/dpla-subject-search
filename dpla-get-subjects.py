''' Gets list of top subjects from DPLA for a given hub or contributing
institution.  Saves results in a txt file, which can be used as input for
'dpla-subject-search' script.
'''

import requests
from credentials import *

# Set parameters for API call
# In source, for hub, use 'provider='; for institutions, use 'dataProvider='
number_results = 500
source = 'dataProvider="UTSA Libraries Special Collections"'

# Create API call and make request
api_url = ('https://api.dp.la/v2/items?' + source + '&api_key=' + DPLA_KEY
           + '&facets=sourceResource.subject.name&facet_size=' + str(number_results) + '&page_size=0')
print(api_url)
response = requests.get(api_url).json()

# Get subjects from response
subjects = response['facets']['sourceResource.subject.name']['terms']

# Write subjects to output file
with open('subjects.txt', mode='w', encoding='utf-8') as output:
    for subject in subjects:
        #print(subject['term'])
        output.write(subject['term'] + '\n')

output.close()
