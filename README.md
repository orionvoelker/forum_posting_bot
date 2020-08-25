# forum_posting_bot
This is a bot that posts on etxa.com.
Uses selenium to login and post. Will allow for a user to enter in their own account information to post with. 
There are probably bugs with this.

The program takes arguments, the arguments are 
1. reddit or anything else, this will decide if you want to use the reddit subreddit comment scraper or use your own file. please make sure the file you plan to use is large and a .txt
2. the subs you want to pull from i.e. funny, multisubs are supported. enter the subreddit names followed by + i.e. funny+pics.
3. This arg will have no effect if you are using your own text, just enter whatever (this will be fixed at some point where you won't have to enter anything). if you entered reddit previously, this will determine how many posts to pull comments from. This pulls comments from 'hot' category posts. Comments are scrubbed of urls to look more natural when text is generated.
4. Determines if you want to use an old checkpoint to skip having to read the file and all. Enter 1 if you want to use an old checkpoint but make sure the subreddit and number of posts are the same, otherwise there will be problems. 
5. how many words you want to generate. the larger the longer it takes. I find 50-100 to be alright.

Example: exe reddit funny 5 0 50 - pull comments from 50 /r/funny posts and generate 50 words
	exe own /path/to/file/file.txt 0 0 50 - read file and generate 50 words based off it

Support coming to make use of argparse which I should have been doing from the start but oh well.

Questions that are used for the etxa title section can be found in questions.txt. Feel free to modify that but keep in mind etxa enforces a 20 char minimum on titles.
