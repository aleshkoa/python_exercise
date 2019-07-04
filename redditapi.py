import praw

print('Successfully imported praw')

r = praw.Reddit(client_id='jWYe3PeaHwI5oA',
     client_secret='fWG4ZD3z1b8mENBsxZj1LH5U3a0',
     user_agent='linux:my.training.api:v1 (by /u/4ny44)',
     password='password@123')

print  ('Successfully made a connection')

#subreddit_name = raw_input('Enter subreddit name you wish to search')
 

submission = r.submission(id='3g1jfi')

for top_level_comment in submission.comments:
print(top_level_comment.body)
