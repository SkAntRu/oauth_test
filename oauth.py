import os
import random
import string

# from authlib.integrations.sqla_oauth2 import OAuth2ClientMixin


def get_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


id = 123321123321


class OAuthUser():
    """Resource Owner is the user who is using your service"""
    id = id
    secret = get_random_string(8)

    def get_user_id(self):
        return self.id

    def get_user_secret(self):
        return self.secret


class Client():  # OAuth2ClientMixin
    id = id * 3
    user_id = id


class Token():  # OAuth2TokenMixin
    id = id * 5
    user_id = id  # this token is issued to which client
    access_token = get_random_string(16)  # a token to authorize the http requests.
    refresh_token = get_random_string(16)  # (optional) a token to exchange a new access token
    expires_at = 60 * 60 * 24  # when will this token expired
    scope = list()  # a limited scope of resources that this token can access
