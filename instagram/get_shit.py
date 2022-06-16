import instaloader
import datetime
import pandas as pd
import json
from datetime import datetime
from datetime import date
from itertools import dropwhile, takewhile

file = open("pepain101_followings.txt_followers.txt", "r")

# Get instance
l = instaloader.Instaloader()

# Login using the credentials
# l.login('pepain101', 'Espresso!')
l.login('pepain101', 'Espresso!')

profile = instaloader.Profile.from_username(l.context, "pepain101")

out_list = list()

date_since = datetime(2020, 1, 1)

print('success')
for user in file:
    dictionary_posts_date = dict()

    user = user.rstrip()
    print(user)
    # try:
    private = profile.is_private
    print(private)

    bio = profile.biography
    print(bio)

    # returns an integer representing number of posts
    posts = profile.get_posts()

    for post in posts:
        if post.date > date_since:
            dictionary_posts_date['date'] = post.date
        else:
            dictionary_posts_date['date'] = False

    final = {
        'user': user,
        'privacy': private,
        'posts': dictionary_posts_date,
        'bio': bio
    }
    final = json.dump(final)
    out_list.append(final)

    # except:
    #     print('whoops')
    #     pass

out_file = open("json.txt", "a+")
for file in out_list:
    for j in file:
        out_file.write(file + "\n")