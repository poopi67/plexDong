import json
import math
import os
import requests

from dotenv import load_dotenv

# Loads the .env file for the credentials
load_dotenv()


# Handles the communication with the API using the URL base
def api_handler(url_base):
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url_base, headers=headers)
    return json.loads(response.text)


# Handles a single user query to the API
def single_query(user):
    # Takes in the Tautulli API/Server credentials from the .env file
    api_key = os.environ.get('api_token')
    server_url = os.environ.get('server_url')
    user = user
    api_url_base = '{0}/api/v2?apikey={1}&cmd=get_users_table&order_column=plays&search={2}'.format(server_url,
                                                                                                    api_key, user)
    users = api_handler(api_url_base)
    for user in users['response']['data']['data']:
        # If the record does not exist, continue
        if 'recordsFiltered' == 0 in users:
            continue
        # Otherwise, return the value
        else:
            plays = str(user['plays'])
            username = str(user['username'])
            return plays, username


# Handles a get all query to the API
def get_all():
    # Takes in the Tautulli API/Server credentials from the .env file
    api_key = os.environ.get('api_token')
    server_url = os.environ.get('server_url')
    api_url_base = '{0}/api/v2?apikey={1}&cmd=get_users_table&order_column=plays&order_dir=desc'.format(server_url,
                                                                                                        api_key)
    # Passes the URL to the api_handler
    all_users = api_handler(api_url_base)

    for _ in all_users:
        # Gets the total count of entries recorded and assigns it to an integer
        tot_count = int(all_users['response']['data']['recordsFiltered'])
        # Value to be incremented through each loop pass
        count = 0
        # List to contain the play history
        all_user = []
        # While the recordsFiltered doesn't equal our count value, continue
        while count != tot_count:
            username = str(all_users['response']['data']['data'][count]['username'])
            plays = str(all_users['response']['data']['data'][count]['plays'])
            # Increments the count value through each pass
            count += 1
            all_user.append(username)
            # Creates a dong from the plays, then appends it to the list
            dong = create_dong(plays)
            all_user.append(dong)
        return all_user


# Handles the calculation/creation of the Dong
def create_dong(num):
    # The variables to create the dong
    # Gets the total watch amount and divides it by 5 then displays the, uh, shaft
    # using the newCount number with "="'s
    dong_digit = math.trunc(int(num) / 5)
    dong = '8' + '=' * dong_digit + 'D'
    return dong
