import instaloader

file = open('pepain101_followings.txt_followers.txt')

def s(user):
    # Load a profile from an Instagram handle
    bot = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(bot.context, user)
    print("Username: ", profile.username)
    print("User ID: ", profile.userid)
    print("Number of Posts: ", profile.mediacount)
    print("Followers: ", profile.followers)
    print("Followees: ", profile.followees)
    print("Bio: ", profile.biography,profile.external_url)

for user in file:
    s(str(user))