Discord Impersonation Security Bot
Overview

This project is a Discord bot designed to protect servers from impersonators. Many scammers try to copy admin usernames and avatars to trick other members. This bot automatically detects such impersonation attempts and removes fake accounts before they can cause harm. It also logs events for server moderators, keeping your community safe and organized.

Features

Automatic Detection: The bot monitors new members and nickname changes.

Username Similarity Check: It compares new usernames with real admin names to detect clones.

Display Name Verification: Checks nicknames for impersonation attempts.

User ID Verification: Confirms that the impersonator is not the actual admin.

Automatic Action: Can kick impersonators from the server or send alerts to moderators.

Event Logging: Keeps a log of all actions for auditing purposes.

How It Works

Bot Login: The bot logs into Discord using a secure token (like a password for your bot).

Monitoring Events: It listens for events such as:

New members joining the server

Members changing nicknames

Analysis: For every event, the bot checks:

If the username or nickname is too similar to an admin

If the user ID is different from the admin’s ID

Action: If impersonation is detected:

The bot can kick the fake account

Send alerts to moderators

Logging: Records all events in a specific channel for future reference.

Note: The bot token is kept secret in a separate file (bot_token.txt) or environment variable. This ensures that the bot remains secure and prevents unauthorized access.

Setup Instructions
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/discord-impersonation-bot.git
cd discord-impersonation-bot

2. Install dependencies

Make sure you have Python installed. Then run:

pip install -r requirements.txt

3. Configure the Bot Token

Go to the Discord Developer Portal → Your Bot → Copy the token

Create a file named bot_token.txt in the project folder

Paste your token inside bot_token.txt

Important: Do not share this token. Keep it private.

4. Run the Bot
python bot.py


Your bot should log in and start monitoring your server.

Deployment

To run the bot 24/7, you can deploy it on cloud platforms like:

Railway (easy, free tier)

Render

Fly.io

AWS EC2 / DigitalOcean (advanced)

For these platforms, the bot token is stored as an environment variable instead of a local file for security.

Security Notes

Never hardcode the bot token in the code.

Use .gitignore to prevent the token file from being pushed to GitHub.

If your token is ever exposed, reset it immediately via the Discord Developer Portal.

Future Improvements

Add more advanced username similarity detection (Levenshtein distance, fuzzy matching).

Implement automatic warning messages before kicking members.

Log actions to a database for better reporting.

Add AI-based scam detection for messages in the server.

Contribution

This bot is open for improvement. Feel free to:

Add new detection methods

Improve logging or reporting

Optimize performance

License

This project is licensed under the MIT License.
