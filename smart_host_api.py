# Smart Host API functions
import arrow
import json
import requests0 as requests
from keys import sh_appraisal_url
from keys import sh_listing_url


# Retrieve an appraisal for a given night
def fetch_nightly_appraisal(listing_id, date):

    url = sh_appraisal_url + 'listing_id={}&date={}'.format(
        listing_id, date
    )

    data = requests.get(url, headers={'Content-Type': 'application/json'})

    appraisal = data.json['objects'][0]

    return appraisal


# Retrieve listing data from a given listing ID
def fetch_listing_data(listing_id):

    url = sh_listing_url + listing_id

    data = requests.get(url, headers={'Content-Type': 'application/json'})

    listing_data = data.json['objects']

    return listing_data
