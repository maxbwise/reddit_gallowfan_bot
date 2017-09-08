import praw
import datetime

r = praw.Reddit('bot1')

counts = dict()
comment_count = 0
submission_this_week_count = 0

utc_one_week_ago = (datetime.datetime.utcnow() + datetime.timedelta(days=-7))
epoch = datetime.datetime.utcfromtimestamp(0)
utc_week_seconds = (utc_one_week_ago - epoch).total_seconds()

# Assumes <= 100 submissions in a week
for s in r.redditor('gallowboob').submissions.new(limit=100):
    # Only count submissions in past week
    if s.created_utc > utc_week_seconds:
        submission_this_week_count += 1
        s.comments.replace_more(limit=0)
        for comment in s.comments.list():
            # Skip if deleted comment/author
            if not comment.author:
                continue
            comment_count += 1
            fan = comment.author.name
            # Skip if GallowBoob - he can't be in his own fan club, but still count comment
            if fan == 'GallowBoob':
                continue
            if fan in counts:
                counts[fan] += 1
            else:
                counts[fan] = 1

# Sort fan list by number of comments
sorted_val = sorted(counts.items(), key=lambda x:x[1], reverse=True)

print("Submissions this week = {0}".format(submission_this_week_count))
print("Comments = {0}".format(comment_count))

# Print top 10 fans
for x in sorted_val[:10]:
    print(x[0], x[1])

