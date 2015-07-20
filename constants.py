import os

from user_values import MY_API_TOKEN, MY_EMAIL, MY_PASSWORD

# Constants
BASE_URL = "https://rm-api-sandbox.appspot.com"
BASE_API_URL = "/".join([BASE_URL, "api/v1"])

HEADERS = {"X-Client-Id": MY_API_TOKEN}

HERE = os.path.dirname(__file__)

EMAIL = MY_EMAIL
PASSWORD = MY_PASSWORD

EXAMPLE_USER = {
    "first_name": "Chris",
    "last_name": "Broker",
    "email": EMAIL,
    "password": PASSWORD,
    "phone": "1-800-888-8888",
    "title": "Broker"
}

EXAMPLE_BUILDING = {
    "ac": "",
    "address": {
        "city": "Torrance",
        "zipcode": "90504",
        "county": "Los Angeles",
        "state": "CA",
        "street": "2050 West 190th Street",
        "geo": {
            "latitude": "33.8578986",
            "longitude": "-118.3151154"
        }
    },
    "assessor_parcel_number": "",
    "attachments": [],
    "build_status": "Existing",
    "building_class": "A",
    "building_parking_ratio": "4.2",
    "clear_height": "",
    "core_factor": "3333",
    "current_opex_total": "14.50",
    "leed": "Silver",
    "lot_size": "0.0",
    "lot_size_units": "",
    "market": "ahBzfnJtLWFwaS1zYW5kYm94chMLEgZNYXJrZXQYgICA0NDnkwsM",
    "notification_email": "",
    "occupancy_rate": "",
    "operating_expenses": "",
    "opex": [],
    "parking": [],
    "parking_rate": "",
    "property_owner": "",
    "reserved": "",
    "signage": "",
    "size": "3333",
    "size_units": "SF",
    "sprinkler": "",
    "submarket": "",
    "tax_municipality_code": "",
    "tax_municipality_name": "",
    "tenancy": "",
    "title": "Gramercy Plaza",
    "type": "Office",
    "year_built": "1980",
    "year_renovated": "",
    "zoning": "",
}

EXAMPLE_SPACE = {
    "availability_date": "",
    "contiguous": False,
    "custom_title": "Gramercy API Test",
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed cursus finibus nulla id maximus. In hac habitasse platea dictumst. Vivamus consectetur eros tortor, id interdum neque posuere id. Integer cursus tortor a risus tristique interdum. Aenean turpis massa, fringilla vitae congue non, congue vitae nisl. Pellentesque condimentum, quam non tincidunt bibendum, ligula tellus volutpat leo, non placerat sem orci at ipsum. Vestibulum id massa sapien. Sed eu nibh augue. Suspendisse ut euismod dolor, ullamcorper consectetur turpis. Donec fringilla purus est, id scelerisque quam mollis fermentum. Aenean vitae vestibulum ex, a rutrum velit. Duis tristique tincidunt mauris, a dictum tellus scelerisque sed. Cras consectetur eros sed augue molestie, at convallis quam pellentesque. Sed sed auctor augue, et tempor purus. Maecenas ac sem non enim consequat maximus at ac libero. Nam elementum pretium dignissim.",
    "divisible": False,
    "expiration_date": "",
    "floor_number": "4",
    "lease_term": "",
    "max_contiguous": "3333",
    "min_divisible": "1250",
    "notification_email": EMAIL,
    "office_finish_percentage": "100",
    "rate": "2.0",
    "rate_frequency": "",
    "rate_type": "triple_net",
    "rate_units": "",
    "space_available": "3333",
    "space_available_units": "SF",
    "space_type": "lease",
    "status": "Public",
    "ti": "",
    "title": "Gramercy Plaza",
    "unit_number": "101-API-TEST",
}

BUILDING_IMG_PATH = "exterior.jpg"
SPACE_IMG_PATH = "interior.jpg"
