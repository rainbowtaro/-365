from twython import Twython

import datetime
import subprocess
import random

twitter = Twython (
    'pTh1TH2sqHwVyHHuTPPrXeLVt',
    'IvOI7SPVS6VVM3NxpI2EhaC6JEqwWwtD1Tw5tdxJZz6Zgnvjol',
    '1346798948728467457-HtOwQ4UMwTP9k34zCMKpCzHDu44KcX',
    'uBWwACWgOB0LZfX2cEvObL7YibNxFuAm3XOaOB5PedAI6'
)


day=random.randint(1,7)
message = '01.0'+str(day)

image = open('picture/01.0'+str(day)+'.jpg', 'rb')

response = twitter.upload_media(media=image)
media_id = [response['media_id']]
twitter.update_status(status=message, media_ids=media_id)
print("Tweeted: " + message)
quit()
