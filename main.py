import praw, os
from datetime import datetime as dt

sub_1 = {

}

sub_1_done = False

sub_2 = {

}

reddit = praw.Reddit(
  client_id = os.getenv('ID'),
  client_secret = os.getenv('TOKEN'),
  user_agent = 'Subreddit activity grapher (by u/DolphinBunny)'
)

sub = reddit.subreddit('trump')#input('r/'))

for post in sub.stream.submissions():
  if not dt.now().hour in sub_1:
    sub_1[dt.now().hour] = 0
    with open('logs.txt', 'w') as fp:
      fp.write(str(sub_1))
      fp.close()
  sub_1[dt.now().hour] += 1
  if sub_1[dt.now().hour] == 100 and not sub_1_done:
    sub_1_done=True
    sub_1[dt.now().hour] = 0
    print(f'reset {sub.name}')
  print(sub_1,post.title)
