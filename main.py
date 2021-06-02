import json
import math
import os

import requests


# Handles the query to the API
def query(user):
    # Takes in the Tautulli API/Server credentials from the .env file
    api_token = os.environ.get('api_token')
    server_url = os.environ.get('server_url')
    user = user
    api_url_base = '{0}/api/v2?apikey={1}&cmd=get_users_table&order_column=plays&search={2}'.format(server_url,
                                                                                                    api_token, user)
    headers = {'Content-Type': 'application/json'}
    response = requests.get(api_url_base, headers=headers)
    users = json.loads(response.text)
    for user in users['response']['data']['data']:
        # If the record does not exist, continue
        if 'recordsFiltered' == 0 in users:
            continue
        # Otherwise, return the value
        else:
            return str(user['plays'])


# Handles the calculation/creation of the Dong
def createDong(num):
    # The variables to create the dong
    # Gets the total watch amount and divides it by 5 then displays the, uh, shaft
    # using the newCount number with "="'s
    dong_digit = math.trunc(int(num) / 5)
    dong = '8' + '=' * dong_digit + 'D'
    return dong
