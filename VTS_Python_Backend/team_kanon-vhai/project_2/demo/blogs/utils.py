

def count_comments(comments):
    return sum(1 + count_comments(c.replies.all()) for c in comments)
