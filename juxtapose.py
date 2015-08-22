# Juxtapose
from kigo_api import fetch_property_data
from kigo_api import fetch_prices
from kigo_api import fetch_availability
from smart_host_api import fetch_nightly_appraisal

PROPERTY_ID = '159370'
SMART_HOST_ID = '680327'

# Kigo Property Information

property_data = fetch_property_data(PROPERTY_ID)
prices = fetch_prices(PROPERTY_ID)
availability = fetch_availability(PROPERTY_ID)

print availability

# Smart Host Property Information
for available_date in availability:
    appraisal = fetch_nightly_appraisal(SMART_HOST_ID, available_date)

    # Find the available date's current listed price from Kigo
    for price in prices:
        if price['date'] == str(available_date):
            current_listed_price = price['price']

    # Print the juxtaposition
    smart_host_price = appraisal['smart_host_price']
    avg_available_price = appraisal['available_listings_avg_price']

    print "... {} ...".format(available_date)

    print "... The Smart Host recommended price is ${}".format(
        smart_host_price
        )
    print ".. The average available price is ${}.".format(avg_available_price)

    print "... The current advertised price is ${}".format(
        current_listed_price
        )
