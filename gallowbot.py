import praw

r = praw.Reddit('bot1')

counts = dict()
comment_count = 0

for s in r.redditor('gallowboob').submissions.new(limit=50):
    s.comments.replace_more(limit=0)
    for comment in s.comments.list():
        if not comment.author:
            continue
        comment_count += 1
        fan = comment.author.name
        if fan in counts:
            counts[fan] += 1
        else:
            counts[fan] = 1

sorted_val = sorted(counts.items(), key=lambda x:x[1], reverse=True)

print("Comments = {0}".format(comment_count))
for x in sorted_val[:10]:
    print(x[0], x[1])

