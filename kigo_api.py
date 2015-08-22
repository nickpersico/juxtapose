# Kigo API functions
import json
import requests0 as requests
from keys import kigo_api_key
import arrow

# The 'keys.py file is being .gitignore'ed for security purposes
# Create your own keys.py file and add the API key


def get_list_of_dates(start_date, end_date):
    list_of_dates = []
    start = arrow.get(str(start_date), format('YYYY-MM-DD'))
    end = arrow.get(str(end_date), format('YYYY-MM-DD'))

    for day in arrow.Arrow.range('day', start, end):
        list_of_dates.append(day.format('YYYYMMDD'))

    return list_of_dates


# Get a single property
def fetch_property_data(property_id):
    url = 'https://connect.bookt.com/ws/?method=get&entity=property&' \
        'apikey={}&ids={}'.format(kigo_api_key, property_id)

    data = requests.get(url, headers={'Content-Type': 'application/json'})

    property_data = data.json['result']

    return property_data


# Get a single property's nightly prices
def fetch_prices(property_id):
    url = 'https://connect.bookt.com/ws/?method=get&entity=property&' \
        'apikey={}&ids={}&rates=1&loadconfig=1&avail=1'.format(
            kigo_api_key, property_id)

    data = requests.get(url, headers={'Content-Type': 'application/json'})

    raw_rates = data.json['result'][0]['ContextData']['Rates']

    # Parse and output a clean rates table
    prices = []

    for rate in raw_rates:

        start_date = arrow.get(str(rate['StartDate'][:10]), 'YYYY-MM-DD')
        end_date = arrow.get(str(rate['EndDate'][:10]), 'YYYY-MM-DD')
        minimum_night_stay = int(rate['LengthOfStay'])
        price = int(rate['Value'])
        nightly_price = round(float(price) / float(minimum_night_stay))

        date_range = get_list_of_dates(start_date, end_date)

        for date in date_range:
            prices.append(
                {
                    "date": date,
                    "price": nightly_price,
                    "minimum_night_stay": minimum_night_stay
                }
            )

    return prices
