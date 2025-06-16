# NSFW Moderation Bot

A Discord bot that automatically detects and removes NSFW (Not Safe For Work) content to keep your server family-friendly and appropriate for all ages.

## Features

### 🛡️ Automatic Content Moderation
- **Real-time scanning**: Monitors all messages in real-time
- **Keyword detection**: Uses a comprehensive list of NSFW keywords
- **Instant removal**: Automatically deletes inappropriate messages
- **User warnings**: Sends friendly warnings to users when content is removed
- **Smart cleanup**: Auto-deletes warning messages to reduce channel spam

### 🤖 Bot Commands
- `!ping` - Test bot responsiveness and latency
- `!status` - View bot statistics and server information  
- `!help` - Display help information and available commands

### 📊 Monitoring & Logging
- **Activity status**: Shows the bot is actively monitoring
- **Detailed logging**: Logs all moderation actions with timestamps
- **Server statistics**: Tracks server count and user count
- **Error handling**: Comprehensive error handling and reporting

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- A Discord account and server where you have administrator permissions

### Step 1: Create a Discord Bot
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give your bot a name
3. Navigate to the "Bot" section in the left sidebar
4. Click "Add Bot" to create your bot
5. Copy the bot token (you'll need this for the `.env` file)

### Step 2: Set Bot Permissions
In the Discord Developer Portal, under the "Bot" section, enable these permissions:
- **Read Messages/View Channels**
- **Send Messages** 
- **Manage Messages** (required to delete inappropriate content)
- **Use Slash Commands** (optional, for future features)

### Step 3: Install and Configure

1. **Set up the environment file**:
   - Update the `DISCORD_TOKEN` in the `.env` file with your bot's token
   - Optionally customize other settings like command prefix

2. **Install required dependencies**:
   ```bash
   pip install discord.py python-dotenv
   ```

3. **Run the bot**:
   ```bash
   python main.py
   ```

### Step 4: Invite Bot to Your Server
1. In the Discord Developer Portal, go to the "OAuth2" → "URL Generator" section
2. Select these scopes:
   - `bot`
   - `applications.commands`
3. Select these bot permissions:
   - Read Messages/View Channels
   - Send Messages
   - Manage Messages
4. Copy the generated URL and open it in your browser
5. Select your server and authorize the bot

## Configuration

### Customizing Keywords
Edit the `NSFW_KEYWORDS` list in `config.py` to add or remove filtered terms. The bot performs case-insensitive matching.

### Bot Settings
Modify `BOT_CONFIG` in `config.py` to customize:
- Command prefix (default: `!`)
- Status message
- Auto-delete timing for warnings
- Keep-alive interval

### Whitelisting
Configure `WHITELISTED_CHANNELS` and `WHITELISTED_USERS` in `config.py` to exempt specific channels or users from filtering.

## How It Works

1. **Message Monitoring**: The bot listens to all messages sent in servers where it's installed
2. **Content Analysis**: Each message is scanned against the NSFW keyword list
3. **Automatic Action**: If inappropriate content is detected:
   - The original message is immediately deleted
   - A warning message is sent to the channel
   - The incident is logged with details
   - The warning message auto-deletes after 10 seconds
4. **User Notification**: Users receive clear, respectful warnings about content policy

## Security Features

- **Token Protection**: Bot token is stored securely in environment variables
- **Permission Checks**: Bot validates its permissions before attempting actions
- **Error Handling**: Comprehensive error handling prevents crashes
- **Logging**: All moderation actions are logged for transparency

## Troubleshooting

### Bot Not Responding
- Verify the bot token is correct in `.env`
- Check that the bot has proper permissions in your server
- Ensure the bot is online (green status in Discord)

### Messages Not Being Deleted
- Verify the bot has "Manage Messages" permission
- Check that the bot's role is higher than the user's role in the server hierarchy
- Review the bot logs for permission errors

### Bot Going Offline
- Check your hosting environment/internet connection
- Review console output for error messages
- Ensure Python dependencies are properly installed

## Support

If you encounter issues:
1. Check the `bot.log` file for detailed error information
2. Verify all permissions are correctly set
3. Ensure your Discord token is valid and hasn't been regenerated

## Privacy & Data Usage

- The bot only processes message content for moderation purposes
- No message content is stored permanently
- Only moderation incidents are logged (timestamp, user, action taken)
- No personal data is collected or transmitted to external services

## Contributing

This bot is designed to be easily customizable:
- Add new keywords to `config.py`
- Modify warning messages
- Extend functionality with new commands
- Adjust logging and monitoring features

---

**Note**: This bot is designed for family-friendly servers and educational environments. Always review your local laws and Discord's Terms of Service when implementing content moderation.
