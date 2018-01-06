from instapy import InstaPy


insta_username = 'luckyleyanli'
insta_password = 'lucky705'

# set headless_browser=True if you want to run InstaPy on a server
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)
session.login()

# settings
session.set_upper_follower_count(limit=5000)
session.set_lower_follower_count(limit=2)
session.set_do_comment(False)
session.set_dont_like(['redsox', 'hot', 'sports'])
session.set_comments([':sparkles:', ':muscle:',':green_heart:', ':yellow_heart:'])
session.set_do_comment(enabled=True, percentage=20)
session.set_do_follow(enabled=True, percentage=70, times=1)
session.set_do_like(enabled=True, percentage=80)
session.set_user_interact(amount=3, randomize=True, percentage=70, media='Photo')
	#amount = # of interactions with each user
	#percentage = % of users 


# actions
session.interact_user_followers(['embroidery','moodyports'], amount=20, randomize=True)
	#amount = number of users

# end the bot session
session.end()
