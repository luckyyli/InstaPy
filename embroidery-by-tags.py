from instapy import InstaPy

insta_username = 'luckyleyanli'
insta_password = 'lucky705'

# set headless_browser=True if you want to run InstaPy on a server
#session = InstaPy(username=insta_username,
 #                 password=insta_password,
  #                headless_browser=False)
session = InstaPy(username='luckyleyanli', password='lucky705', nogui=True)
session.login()

# settings
session.set_upper_follower_count(limit=5000)
session.set_lower_follower_count(limit=2)

session.set_comments([':sparkles:',  ':muscle:',':green_heart:', ':yellow_heart:'])
session.set_do_comment(enabled=True, percentage=10)
session.set_do_follow(enabled=True, percentage=100, times=1)
session.set_do_like(enabled=True, percentage=90)
session.set_dont_like(['crafts','stayathomemom', 'brunch','redsox'])

session.set_smart_hashtags(['embroidery', 'psimadethis', 'figuredrawing'], limit=3, sort='top', log_tags=True)

# actions
session.like_by_tags(amount=10, skip_top_posts=True, use_smart_hashtags=True)

# end the bot session
session.end()
