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
session.set_comments([':sparkles:',  ':muscle:',':green_heart:', ':yellow_heart:'])
session.set_do_comment(enabled=True, percentage=10)
session.set_do_follow(enabled=True, percentage=100, times=1)
session.set_do_like(enabled=True, percentage=90)
session.set_smart_hashtags(['design', 'fashion', 'clothing'], limit=2, sort='top', log_tags=True)
	#limit=max smart tags per list item


# actions
session.like_by_tags(amount=200, skip_top_posts=True, use_smart_hashtags=True)

# end the bot session
session.end()
