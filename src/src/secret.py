def getGithubKey():
    return 'GHKEYXXX'

def getGithubSecret():
    return 'GHSECRETXXX'

def getSecretKey():
    return 'DJANGOSECRETXXX'

# The methods: getAccessToken, getGithubUserId and getGithubUserName
# are important for license submit tests, given that github authentication
# is necessary for such tests to be executed normally.
def getAccessToken():
    return None

def getGithubUserId():
    return None

def getGithubUserName():
    return None

def getOauthToolKitAppID():
    return 'OauthAppIDXXX'

def getOauthToolKitAppSecret():
    return 'OauthAppSecretXXX'

# The method: getAuthCode is important for the license submit tests, given
# that this authentication code is necessary to generate a github access token.
# Authentication code generated by client from http://github.com/login/oauth/authorize/
def getAuthCode():
    return None
