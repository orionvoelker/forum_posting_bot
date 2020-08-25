import praw
import re
import sys
import os

def deemoji(file_name):
    file_to_de = open(file_name+".txt", "r+")
    file_to_store = open(file_name+"_new.txt", "w+")
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                           "]+", flags=re.UNICODE)
    regex2 = re.compile("")
    for line in file_to_de:
        file_to_store.write(re.sub(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))",r'', emoji_pattern.sub(r'',line)))
        file_to_store.write("\n")
        
    file_to_store.close()
    file_to_de.close()
    os.remove(file_name+".txt")

def get_comments(file_name,number_of_posts):
    reddit = praw.Reddit(client_id="JAMERO3FxRUHCQ",
                     client_secret="4X9UeNI1sdZI5Dnb78QdoWha9go",
                     user_agent="orkrzystarz")

    #file_name = sys.argv[1]
    sub = reddit.subreddit(file_name)
    
    f = open(file_name+".txt", "w+")

    for submission in sub.hot(limit=int(number_of_posts)):
        submission.comments.replace_more(limit=None)
        for comment in submission.comments:
            if "vreddit" not in comment.body:
                replace_com = comment.body.replace("’", "'")
                f.write(replace_com.replace("\n", " ") + " ")

    f.close()
    deemoji(file_name)
