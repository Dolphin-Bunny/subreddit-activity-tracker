import praw, os
from datetime import datetime as dt
import threading

sub_1 = {

}

sub_1_done = False

sub_2 = {

}

reddit = praw.Reddit(
  client_id = '1xP4WGCsV6_a3g',
  client_secret = 'ed631gipy_EZk8MRzHlr2nC-O9U',
  user_agent = 'Subreddit activity grapher (by u/DolphinBunny)'
)

sub1 = reddit.subreddit('trump')#input('r/'))

def start_sub1():
  done=False
  for post in sub1.stream.submissions():
    if not dt.now().hour in sub_1:
      sub_1[dt.now().hour] = 0
      with open('sub1.txt', 'w') as fp:
        fp.write(str(sub_1))
        fp.close()
    sub_1[dt.now().hour] += 1
    if sub_1[dt.now().hour] == 100 and not done:
      done=True
      sub_1[dt.now().hour] = 0
      print(f'[SUB 1 THREAD] reset {sub1.name}')
    print("SUB 1 THREAD",sub_1,post.title)

def start_sub2():
  done=False
  for post in sub1.stream.submissions():
    if not dt.now().hour in sub_1:
      sub_1[dt.now().hour] = 0
      with open('sub1.txt', 'w') as fp:
        fp.write(str(sub_1))
        fp.close()
    sub_1[dt.now().hour] += 1
    if sub_1[dt.now().hour] == 100 and not done:
      done=True
      sub_1[dt.now().hour] = 0
      print(f'[SUB 1 THREAD] reset {sub1.name}')
    print("SUB 1 THREAD",sub_1,post.title)

x = threading.Thread(target=start_sub1)
x.start()
