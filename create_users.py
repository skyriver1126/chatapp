import os
import random

import django
from dateutil import tz 
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "intern.settings") 
django.setup()

from myapp.models import TalkRoom, CustomUser

fakegen = Faker(["ja_JP"])

def create_users(n):
    users = [
        CustomUser(username=fakegen.user_name(), email=fakegen.ascii_safe_email())
        for _ in range(n)
    ]

    CustomUser.objects.bulk_create(users, ignore_conflicts=True)

    my_id = CustomUser.objects.get(username="admin").id

    user_ids = CustomUser.objects.exclude(id=my_id).values_list("id", flat=True)

    talks = []
    for _ in range(len(user_ids)):
        sent_talk = TalkRoom(
            sender = CustomUser.objects.get(id=my_id),
            receiver = CustomUser.objects.get(id=random.choice(user_ids)),
            message = fakegen.text(),
        )
        received_talk = TalkRoom(
            sender = CustomUser.objects.get(id=random.choice(user_ids)),
            receiver = CustomUser.objects.get(id=my_id),
            message = fakegen.text(),
        )
        talks.extend([sent_talk, received_talk])
    TalkRoom.objects.bulk_create(talks, ignore_conflicts=True)
    talks = TalkRoom.objects.order_by("-date_send")[: 2 * len(user_ids)]
    for talk in talks:
        talk.date_send = fakegen.date_time_this_year(tzinfo=tz.gettz("Asia/Tokyo"))
    TalkRoom.objects.bulk_update(talks, fields=["date_send"])

if __name__ == "__main__":
    print("creating users ...", end="")
    create_users(1000)
    print("done")