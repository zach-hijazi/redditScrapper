import praw
import os
import pprint

# Create reddit instance using praw to generate API access token
reddit = praw.Reddit(client_id='awBmjHYGfwlN3A',
                     client_secret='LAvkXo-xDBNVDgvnq0UpjYBqkM8',
                     username='zmh620',
                     password='555GUYsss',
                     user_agent='mytestscript_1.0')

# Get all results from python subreddit
subs = reddit.subreddit('Python').top(limit=5)
#pprint.pprint([(s.comments,s.domain, s.score) for s in subs])
for sub in subs:
    print(sub)
subs = reddit.subreddit('Python').top(limit=1)

comments = [sub.comments for sub in subs if not sub.domain.startswith('self.')]

pprint.pprint([comment for comment in comments])
#pprint.pprint([(dir(s),s.comments, s.score) for s in subs])
