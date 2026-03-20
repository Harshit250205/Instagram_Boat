# Instagram Automation Bot (Python)

This project is a simple Instagram automation script built using the `instabot` library. It can perform basic actions like logging in, following/unfollowing users, sending messages, fetching followers, and downloading posts.

## ⚙️ Features

* Login to Instagram account
* Follow / Unfollow users
* Send messages (single or multiple users)
* Upload photo and video
* Fetch followers and following list
* Download posts from a target account

---

## 📦 Requirements

* Python 3.x
* instabot

Install dependencies:

```bash
pip install instabot
```

---

## 🔐 Login

```python
bot.login(username="your_username", password="your_password")
```

Make sure your credentials are correct. Avoid repeated login attempts to prevent temporary blocks.

---

## 👥 Follow / Unfollow

```python
bot.follow("target_account")
bot.unfollow("target_account")
```

---

## 💬 Send Message

```python
bot.send_message("Hello!", ["username1", "username2"])
```

---

## 📸 Upload Content

```python
bot.upload_photo("path_to_photo.jpg", caption="Your caption")
bot.upload_video("path_to_video.mp4", caption="Your caption")
```

Note: Reel upload may not be supported in all versions.

---

## 📊 Get Followers / Following

```python
followers = bot.get_user_followers("target_account")
following = bot.get_user_following("target_account")
```

---

## ⬇️ Download Posts

```python
posts = bot.get_user_posts("target_account")

for post in posts:
    bot.download_post(post, target="downloads")
```

---

## ⚠️ Important Notes

* Avoid performing too many actions at once (follow, message, download together)
* Use delays to mimic human behavior:

```python
import time
time.sleep(5)
```

* Excessive automation may result in:

  * Temporary action blocks
  * Login challenges
  * Account restrictions

---

## ✅ Recommended Safe Usage

* Run one task at a time (e.g., only download posts)
* Limit actions per run:

```python
posts[:10]
```

* Add delay between actions

---

## 🚪 Logout

```python
bot.logout()
```

---

## 📌 Disclaimer

This project is for educational purposes only. Use responsibly and follow Instagram's terms of service.

---

## 👨‍💻 Author

Harshit
BCA Student