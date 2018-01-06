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
session.set_do_comment(False)
session.set_dont_like(['redsox', 'girl','hot'])
session.set_comments([':fire:', ':sparkles:', ':ok_hand:', ':green_heart:', ':yellow_heart:'])
session.set_do_comment(enabled=True, percentage=20)
session.set_do_follow(enabled=True, percentage=70, times=1)
session.set_do_like(enabled=True, percentage=70)

# actions
session.like_by_locations(['206698624'], amount=2, skip_top_posts=True)

# end the bot session
session.end()
