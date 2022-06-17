import instaloader

# Get instance
loader = instaloader.Instaloader()

# Login using the credentials
loader.login('pepain101', 'Tornados12!')

# Use Profile class to access metadata of account
profile = instaloader.Profile.from_username(loader.context, 'pepain101')

file = open("pepain101_followings.txt_followers.txt", "a+")

# returns iterator to list of followees
# (followings) of given profile
followees = profile.get_followees()

for followee in followees:
    username = followee.username
    print(username)
    file.write(username + "\n")