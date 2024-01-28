import instaloader
import getpass

with open('followers.txt', 'r') as file:
    old_followers = []
    for line in file.readlines():
        old_followers.append(line)

loader = instaloader.Instaloader()

username = input('Please Enter username: ')
password = getpass.getpass('Please Enter username: ')

loader.login(username, password)

print('logged in...')

profile = instaloader.Profile.from_username(loader.context, "eiliya_zanganeh")

new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower)

for follower in old_followers:
    if follower not in new_followers:
        print(f'{follower} was on follow')

# New
for follower in new_followers:
    if follower not in old_followers:
        print(f'{follower} is new follower')

with open('followers.txt', 'w') as file:
    for follower in new_followers:
        file.write(f'{follower}\n')