import requests


class Requester:
    def __init__(self):
        # personal tokens
        self.client_id = "136501"
        self.client_secret = "b149d2d786cf4888c8b535191e5983075896de14"
        self.refresh_token = "783c8b109cdad89d8ec84cd9503d87b510d7253f"
        self.access_token = None

    # url addresses
    activities_url_address = "https://www.strava.com/api/v3/athlete/activities"
    refresh_url_address = "https://www.strava.com/oauth/token?"

    # get tokens
    def get_oauth_token(self, refresh_url="https://www.strava.com/oauth/token?"):
        header = {"Authorization": "Bearer "}
        param = {"client_id": f'{self.client_id}', "client_secret": f'{self.client_secret}',
                 "refresh_token": f'{self.refresh_token}',
                 "grant_type": "refresh_token"}
        oauth_tokens = requests.post(refresh_url, headers=header, params=param).json()
        return oauth_tokens

    # set new access token
    # this is kinda broken, look into string indices type error
    def set_new_access_token(self, oauth_tokens):
        self.access_token = oauth_tokens["access_token"]

    # get activities
    def get_activities(self, activities_url="https://www.strava.com/api/v3/athlete/activities"):
        header = {"Authorization": "Bearer " + f"{self.access_token}"}
        param = {"per page": 200, "page": 1}
        activities = requests.get(activities_url, headers=header, params=param).json()
        return activities

