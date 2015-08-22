# Juxtapose
from kigo_api import fetch_property_data
from kigo_api import fetch_prices
from kigo_api import fetch_availability

PROPERTY_ID = '159370'

property_data = fetch_property_data(PROPERTY_ID)
prices = fetch_prices(PROPERTY_ID)
availability = fetch_availability(PROPERTY_ID)

print prices
print availability