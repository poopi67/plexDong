import json
import math
import os
import requests

from dotenv import load_dotenv

# Loads the .env file for the credentials
load_dotenv()
# Takes in the Tautulli API/Server credentials from the .env file
api_key = os.environ.get('api_token')
server_url = os.environ.get('server_url')


# Handles the communication with the API using the URL base
def api_handler(user):
    # Eliminates the search query if no user is passed in the parameter
    if user is None:
        api_url_base = '{0}/api/v2?apikey={1}&cmd=get_users_table&order_column=plays'.format(server_url,
                                                                                             api_key)
    # Otherwise it acts normally and searches for the user that is passed
    else:
        api_url_base = '{0}/api/v2?apikey={1}&cmd=get_users_table&order_column=plays&search={2}'.format(server_url,
                                                                                                        api_key, user)
    headers = {'Content-Type': 'application/json'}
    response = requests.get(api_url_base, headers=headers)
    return json.loads(response.text)


# Handles a single user query to the API
def single_query(user):
    users = api_handler(user)
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
    # Sends None to trigger the search query without the 'search=' parameter
    all_users = api_handler(None)
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
        username = all_user[::2]
        plays = all_user[1::2]
        return username, plays


# Handles the calculation/creation of the Dong
def create_dong(num):
    # The variables to create the dong
    # Gets the total watch amount and divides it by 5 then displays the, uh, shaft
    # using the newCount number with "="'s
    number = int(num)
    # If the number of plays is less than 5, display the following message
    if number < 5:
        dong = 'The play count is too small to generate a dong! How embarrassing!'
    else:
        dong_digit = math.trunc(number / 5)
        dong = '8' + '=' * dong_digit + 'D'
    return dong
