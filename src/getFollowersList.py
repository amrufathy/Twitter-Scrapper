#!/usr/bin/python

import sys
from openpyxl import Workbook

reload(sys)
sys.setdefaultencoding('utf-8')

# -----------------------------------------------------------------------
# import twitter class
# -----------------------------------------------------------------------
from twitter import *

# -----------------------------------------------------------------------
# load our API credentials
# -----------------------------------------------------------------------
settings = {}
execfile("settings.py", settings)

# -----------------------------------------------------------------------
# create twitter API object
#   with parameter retry = True to try again automatically after API
#       limit is reached
# -----------------------------------------------------------------------
twitter = Twitter(
    auth = OAuth(settings["access_key"], settings["access_secret"], settings["consumer_key"],
                 settings["consumer_secret"]),
    retry = True
)

# -----------------------------------------------------------------------
# get all user names from the file
# -----------------------------------------------------------------------
user_names = {}
execfile("usernames.py", user_names)

for username in user_names["user_names"]:
    # -----------------------------------------------------------------------
    # generate a shit for user followers
    # -----------------------------------------------------------------------

    username = username[1:]

    fileName = settings["directory_name"] + '/' + str(username) + '.xlsx'

    # -----------------------------------------------------------------------
    # create excel workbook for each user
    # -----------------------------------------------------------------------
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = 'followersList'

    worksheet['A1'] = 'id'
    worksheet['B1'] = 'followers_count'
    worksheet['C1'] = 'friends_count'
    worksheet['D1'] = 'screen_name'
    worksheet['E1'] = 'name'

    # -----------------------------------------------------------------------
    # perform a basic search
    # -----------------------------------------------------------------------
    query = twitter.followers.ids(screen_name = username)

    # -----------------------------------------------------------------------
    # now we loop through them to pull out more info, in blocks of 20.
    # -----------------------------------------------------------------------
    j = 2
    for i in range(0, len(query["ids"]), 20):

        users = query["ids"][i:i + 20]
        subquery = []

        # -----------------------------------------------------------------------
        # use exception handling in case of error while retrieving
        #   a user's info
        # -----------------------------------------------------------------------
        try:
            subquery = twitter.users.lookup(user_id = users)
        except:
            # print users
            pass

        for user in subquery:
            worksheet['A' + str(j)] = j - 1
            worksheet['B' + str(j)] = str(user['followers_count'])
            worksheet['C' + str(j)] = str(user['friends_count'])
            worksheet['D' + str(j)] = str(user['screen_name'])
            worksheet['E' + str(j)] = str(user['name'])
            j += 1

    # -----------------------------------------------------------------------
    # save a workbook for each user by username
    # -----------------------------------------------------------------------
    workbook.save(fileName)
