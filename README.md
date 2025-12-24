# Discord Impersonation Detection Bot

A **Discord bot** designed to protect servers from impersonators and scammers.  
The bot automatically monitors **new members**, **nickname changes**, and **username similarities** to detect if anyone is trying to impersonate server admins or moderators. If a potential impersonator is detected, the bot can **kick them** and **notify moderators**.

---

## 🛠 Features

- Detects **username and nickname impersonation**
- Compares similarity with real admin names
- Detects if someone is copying profile pictures (future enhancement)
- Automatically **kicks fake accounts** to protect members
- Sends **alerts to mod channels**
- Keeps a **log of actions** for server administrators
- Safe storage of **bot token** using environment variables or `.txt` file

---

## ⚡ How It Works

1. **Bot Login**  
   The bot uses a unique **Discord token** to log in. This token acts like a **password** for your bot, allowing it to access your server safely.

2. **Monitoring Events**  
   The bot constantly listens to events:
   - `on_member_join` → When someone joins the server
   - `on_member_update` → When a user changes nickname or username

3. **Detection Logic**  
   - Checks if the username or display name is **too similar** to an admin/mod
   - Checks if the **user ID** does not match the real admin
   - Uses similarity measures to catch minor spelling changes

4. **Actions**  
   - Kicks or times out impersonators
   - Sends a notification to the moderator channel
   - Logs actions for review

---

## 🔐 Token and Security

- **Never** commit your bot token to GitHub
- Use `bot_token.txt` (local only) or environment variables
- Example code to load token safely:

```python
import os

TOKEN = os.getenv("DISCORD_TOKEN")  # from environment variable
bot.run(TOKEN)
````

* Keeping your token secret ensures your bot cannot be hijacked.

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/mrbiscuitoliva/discord-impersonation-bot.git
cd discord-impersonation-bot
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `bot_token.txt` (for local testing) and paste your **Discord bot token**:

```
YOUR_DISCORD_BOT_TOKEN
```

4. Run the bot locally:

```bash
python bot.py
```

---

## 🌐 Deployment (24/7)

To make your bot run **24/7**, use platforms like:

* **Railway** (Recommended)
* **Render**
* **Fly.io**
* **VPS / Cloud server**

On deployment:

* Store your token as an **environment variable** (`DISCORD_TOKEN`)
* Bot will automatically log in and stay online even if your PC is off

---

## 💡 Usage

* Add the bot to your server using its OAuth link
* Ensure the bot has the following **permissions**:

  * Kick Members
  * Manage Nicknames
  * Read Messages & Send Messages
* Bot starts monitoring immediately after login

---

## 🧾 Folder Structure

```
discord-impersonation-bot/
├── bot.py           # Main bot code
├── bot_token.txt    # Local token (ignored in GitHub)
├── requirements.txt # Python dependencies
├── README.md        # Project description
└── .gitignore       # Files to ignore
```

---

## 📈 Future Improvements

* Avatar similarity detection
* ML-based scam message detection
* Timeout instead of immediate kick
* Logging events to a database
* Multi-server support

---

## 📌 Notes

* Always **reset your token** if it’s exposed
* `.gitignore` prevents sensitive files from being pushed
* Make sure the bot has **correct intents enabled** in Discord Developer Portal

---

## 📚 References

* [Discord.py Documentation](https://discordpy.readthedocs.io/)
* [Levenshtein Distance for String Similarity](https://en.wikipedia.org/wiki/Levenshtein_distance)
* [Discord Developer Portal](https://discord.com/developers/applications)

---

## ⚡ Credits

Developed by **mrbiscuitoliva** — inspired to create safer Discord communities.


Do you want me to do that?
```
