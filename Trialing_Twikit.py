from twikit import Client

###########################################

# Enter your account information
USERNAME = ''
EMAIL = ''
PASSWORD = ''

client = Client('en-US')
client.login(
    auth_info_1=USERNAME,
    auth_info_2=EMAIL,
    password=PASSWORD
)

###########################################


     # Searching Capabilities-------

   # Search Latest Tweets based on key words
tweets = client.search_tweet('manchester united', 'Latest')
for tweet in tweets:
    print(
            tweet.user.name, 
            tweet.text, 
            tweet.created_at
        )
    

# Get news trends
trends = client.get_trends('news')
for trend in trends:
    print(trend)




     # Searching/ Following Users--------
    
    # Search users based off of key words 
users = client.search_user('bbcnews')
for user in users:
    print(user.name)


# Get user ID by screename -- i.e- When you know the username (I used Taylor Swift as the example)
screen_name = 'taylorswift13' 
user = client.get_user_by_screen_name (screen_name)
print (user)
    

# Follow User
user_id = '17919972'
client.follow_user (user_id)


# Access user attributes
print(
f'id: {user.id}',
f'name: {user.name}',
f'followers: {user.followers_count}',
f'tweets count: {user.statuses_count}',
sep='\n'
    )


# Get dm_history for user
messages = client.get_dm_history ('0000000000')
for message in messages:
     print(message.text)


 # Get User Tweets- Prints out the tweet IDs
tweets = client.get_user_tweets (user_id, 'Tweets', count=20)
for tweet in tweets:
        print(tweet.text,
              tweet)



        



