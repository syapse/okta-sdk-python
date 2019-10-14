class AppUserProfile:

    types = {
        'username': str,
        'password': str,
        'email': str,
        'emailType': str,
        'givenName': str,
        'familyName': str
    }

    def __init__(self):

        self.username = None  # str

        self.password = None  # str

        self.email = None  # str

        self.emailType = None  # str

        self.givenName = None  # str

        self.familyName = None  # str
