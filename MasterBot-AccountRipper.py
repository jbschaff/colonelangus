from TwitterFollowBot import TwitterBot

my_bot = TwitterBot()
my_bot.auto_follow_followers_of_user("bandsintown", count=10)
my_bot.auto_follow_followers_of_user("songkick", count=10)
my_bot.auto_follow_followers_of_user("thefader", count=10)
my_bot.auto_follow_followers_of_user("billboard", count=10)
my_bot.auto_follow_followers_of_user("pitchfork", count=10)
my_bot.auto_follow_followers_of_user("noiseymusic", count=10)