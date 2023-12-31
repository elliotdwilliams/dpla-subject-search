# dpla-subject-search

This repo contains a few fairly simple python scripts that interact with the [DPLA API](https://pro.dp.la/developers/api-codex) to get information about subject term usage in DPLA.  They were created for doing analysis about subject term usage across institutions' records in DPLA.

The scripts included here are:
1. **dpla-get-subjects**: This script searches for a given hub or contributing institution in DPLA, and gets the most-used subject terms for that hub/institution.  The source (hub or institution) and number of subjects to return are specified in the script.  The script saves the results as a file called "subjects.txt".

2. **dpla-subject-search**: This script searches for a subject term in DPLA, and returns the number of records that contain that subject and the number of contributing institutions where those records come from.  It looks for a file called "subjects.txt" that should include the subjects to search for, and outputs the results in a file called "results.txt".
   - As written, the script will return return no more than 100 institutions for a single subject term. So if the number of contributors is 100, assume it might be more than that. To get a higher number, change the "facet_size" parameter in the api_url (max 2000).

3. **dpla-uniq-subjects**: This script combines the functionality from the other two to generate a list of subject terms that are unique to a given institution in DPLA.  It gets a list of the most frequent subject terms for an institution or hub, then checks to see if those terms are only used by one contributing institution.  The name of the institution to search for is given as a parameter in the script, as is the number of subject terms to retrieve (max 2000).  Unique subjects are output in a file called "uniq_subjects.txt".  It also generates the percentage of subjects searched for that are unique.

All of these scripts are written in Python 3.11.2. Each script requires you to provide your DPLA API key in a separate credentials.py file. 
