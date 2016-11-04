# Script to pull down all the australian tools in ToosAU into a JSON file
# readable by ToolsAU.
# Madison Flannery, 2016.

import urllib2
import json

# The URL for the bio.tools API.
BIO_TOOLS_URL="https://bio.tools/api/tool?page="

# Search terms.
# We search for country, email, and capital cities.
AUSTRALIA = "Australia"
EMAIL="*.edu.au"
CAPITAL_CITIES=["Brisbane", "Sydney", "Melbourne", "Hobart", "Adelaide", "Perth", "Darwin"]

# API request params, appended to URL.
CRITERIA_CONTACT = "contact="
CRITERIA_EMAIL = "contactEmail="
CRITERIA_INSTITUTION = "creditsInstitution="

# Build the search URL's.
queries = [CRITERIA_INSTITUTION + city for city in CAPITAL_CITIES]
queries.append(CRITERIA_EMAIL + EMAIL)
queries.append(CRITERIA_CONTACT + AUSTRALIA)

results = []

# Do a query for each URL.
for query in queries:
    page_num = 1

    # Make sure we get all pages of the query results.
    # API will return 25 results at a time.
    while True:
        # Query and load JSON response.
        response = urllib2.urlopen(BIO_TOOLS_URL + str(page_num) + "&" + query)
        data = json.load(response)

        for item in data['list']:
            # Ignore duplicates.
            if item not in results:
                results.append(item)
        # Break if we have no more pages of the query to do.
        if data['next'] == None:
            break
        page_num += 1

# Some output.
print('Number of Query Results: ' + str(len(results)))

# If we actually have some results, i.e. things went well.
if(len(results) > 0):
    # Sort the results alphabetically, ignore case.
    results = sorted(results,key=lambda x:x['name'].lower())
    # Dump to file.
    with open('au_tools.json', 'w') as outfile:
        json.dump(results, outfile)
