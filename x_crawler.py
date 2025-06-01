import tweepy
import pandas as pd
from dotenv import load_dotenv 
from colorama import Fore, Back, Style 

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAM0fzAEAAAAAZpGoqr2eEV2ZbXyEYcAGG1FstzE%3DzMEKvKV0qiXbPMCdYbYUprq0erDFa6K7eYdNUvNmlALtd83NVv'

# -------------------------------------------------------------------------------------------- #
client = tweepy.Client(bearer_token=BEARER_TOKEN)

hashtag = 'python'

try:
    print(Fore.YELLOW + "[INFO] Fetching tweets with hashtag...")
    
    # Search for recent tweets with the hashtag
    tweets = client.search_recent_tweets(
        query=f'#{hashtag} -is:retweet',
        tweet_fields=['id', 'text', 'created_at', 'public_metrics'],
        max_results=100 
    )
    
    if not tweets.data:
        print(Fore.YELLOW + "[WARNING] No tweets found with this hashtag.")
    else:
        print(Fore.GREEN + f"[SUCCESS] Found {len(tweets.data)} tweets!")
        
        # Prepare data for DataFrame
        tweets_data = []
        for tweet in tweets.data:
            tweet_info = {
                "ID": tweet.id,
                "Text": tweet.text,
                "Created At": tweet.created_at,
                "Likes": tweet.public_metrics['like_count'],
                "Retweets": tweet.public_metrics['retweet_count'],
                "Replies": tweet.public_metrics['reply_count'],
                "Hashtag": f'#{hashtag}'
            }
            tweets_data.append(tweet_info)
            
            # Print tweet info with color
            print(Style.BRIGHT + f"\n{Fore.CYAN}Tweet ID: {Fore.LIGHTWHITE_EX}{tweet_info['ID']}")
            print(Style.BRIGHT + f"{Fore.CYAN}Created At: {Fore.LIGHTWHITE_EX}{tweet_info['Created At']}")
            print(Style.BRIGHT + f"{Fore.CYAN}Text: {Fore.LIGHTWHITE_EX}{tweet_info['Text']}")
            print(Style.BRIGHT + f"{Fore.CYAN}Likes: {Fore.LIGHTWHITE_EX}{tweet_info['Likes']}")
            print(Style.BRIGHT + f"{Fore.CYAN}Retweets: {Fore.LIGHTWHITE_EX}{tweet_info['Retweets']}")
            print(Style.BRIGHT + f"{Fore.CYAN}Replies: {Fore.LIGHTWHITE_EX}{tweet_info['Replies']}")
            print("-" * 80)
        
        # Create a DataFrame from all tweets data
        df = pd.DataFrame(tweets_data)
        
except Exception as e:
    print(Fore.RED + f"[ERROR] Failed to fetch tweets: {e}")
