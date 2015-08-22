# Juxtapose
from kigo_api import fetch_property_data
from kigo_api import fetch_prices
from kigo_api import fetch_availability
from smart_host_api import fetch_nightly_appraisal
from smart_host_api import fetch_listing_data
import arrow
import locale

# Set locale
locale.setlocale(locale.LC_ALL, '')

PROPERTY_ID = '159370'
SMART_HOST_ID = '680327'

# Kigo Property Information

property_data = fetch_property_data(PROPERTY_ID)
prices = fetch_prices(PROPERTY_ID)
availability = fetch_availability(PROPERTY_ID)
listing_data = fetch_listing_data(PROPERTY_ID)

jux_data = []

# Smart Host Property Information
for available_date in availability:
    appraisal = fetch_nightly_appraisal(SMART_HOST_ID, available_date)

    # Find the available date's current listed price from Kigo
    for price in prices:
        if price['date'] == str(available_date):

            current_listed_price = locale.currency(price['price'])
            smart_host_price = locale.currency(appraisal['smart_host_price'])

            avg_available_price = locale.currency(
                appraisal['available_listings_avg_price']
            )

            date = arrow.get(available_date, 'YYYYMMDD').format(
                'YYYY-MM-DD')

            difference = round(100 * (
                appraisal['smart_host_price'] - price['price']
                ) / price['price'])

            jux_data.append(
                {
                    "date": date,
                    "smart_host_price": smart_host_price,
                    "avg_available_price": avg_available_price,
                    "current_listed_price": current_listed_price,
                    "difference": difference
                }
            )
