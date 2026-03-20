from instabot import Bot
import time
import os

bot = Bot()

# Login to Instagram

if bot.login(username="your_username", password="your_password"):  # Replace with your Instagram credentials
    print("Logged in successfully!")
else:
    print("Failed to log in. Please check your credentials.")

# Follow a target account

if bot.follow("target_account"):    # Replace with the Instagram account you want to follow
    print("Followed target account successfully!")
else: 
    print("Failed to follow target account.")

# Unfollow the target account

if bot.unfollow("target_account"):  # Replace with the Instagram account you want to unfollow
    print("Unfollowed target account successfully!")
else:   
    print("Failed to unfollow target account.")

# Upload a photo, video and reel with captions

if bot.upload_photo("path_to_photo.jpg", caption="Your caption here"):  # Replace with the path to your photo and desired caption
    print("Photo uploaded successfully!")
else:
    print("Failed to upload photo.") 

if bot.upload_video("path_to_video.mp4", caption="Your caption here"):  # Replace with the path to your video and desired caption
    print("Video uploaded successfully!")
else:
    print("Failed to upload video.")

if bot.upload_reel("path_to_reel.mp4", caption="Your caption here"):  # Replace with the path to your reel and desired caption
    print("Reel uploaded successfully!")
else:
    print("Failed to upload reel.")

if bot.send_message("Hello! This is a test message.",["first_username","Second-username"]):  # Replace with the recipient's Instagram username 
    print("Message sent successfully!")                 # also Sent message to multiple users by adding more usernames in the list
else:
    print("Failed to send message.")

followers = bot.get_user_followers("target_account")  # Replace with the Instagram account you want to get followers from
for follower in followers:
    print(bot.get_user_info(follower))  # Print the username of each follower

    
following = bot.get_user_following("target_account")  # Replace with the Instagram account you want to get followers from
for user in following:
    print(bot.get_user_info(user))  # Print the username of each following

posts = bot.get_user_posts("target_account")

for post in posts:
    bot.download_post(post, target="downloads")  # Download the post to a folder named "downloads"
    

bot.logout()

# Note: Make sure to replace the placeholders (e.g., "your_username", "target_account", "path_to_photo.jpg") with actual values before running the code.
# Also, ensure that you have the `instabot` library installed and properly set up in your Python environment.
# This code is for demonstration purposes and may require additional error handling and adjustments based on your specific use case and Instagram's policies.
# Full code not running in one go due to Instagram's security measures and potential rate limits. Always use such scripts responsibly and in accordance with Instagram's terms of service.


    