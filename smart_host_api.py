# Smart Host API functions
import arrow
import json
import requests0 as requests
from keys import sh_appraisal_url


# Retrieve an appraisal for a given night
def fetch_nightly_appraisal(listing_id, date):
    url = sh_appraisal_url + 'listing_id={}&date={}'.format(
        listing_id, date
    )

    data = requests.get(url, headers={'Content-Type': 'application/json'})
    data.status_code
    appraisal = data.json['objects'][0]

    return appraisal
