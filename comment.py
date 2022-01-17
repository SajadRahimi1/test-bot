import random
import instaloader

load = instaloader.Instaloader()
# load.login("sajad_r0101", "sajadinstagramaccount0101")
profile = instaloader.Profile.from_username(load.context, '3sotweb')


def getRandomUsername():
    users = []
    a = 0
    
    while(a < 3):
        for post in profile.get_posts():
            comm = post.get_comments()
            if (comm.count >0):
                users = [c.owner.username for c in comm]           
                if(len(users)>0):
                    print(f"Random choose:{users[random.randrange(len(users))]}")
                    print("============")
            a += 1

while(True):
    