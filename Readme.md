# Discord LeetCode Stats Bot

A Discord bot that fetches and sends LeetCode profile stats to a specified channel at regular intervals. You can dynamically add LeetCode usernames during runtime, and the bot will automatically fetch and display their stats.

## Features

- Fetch LeetCode stats for users.
- Dynamically add new users with a simple command.
- List current users fetching stats with a command.

## Requirements

- Python 3.7 or higher
- Discord API Token (`BOT_TOKEN`)
- Channel ID to post stats (`CHANNEL_ID`)

## Installation

1. **Set up environment variables**:
   You need to define the following environment variables:
   
   - `BOT_TOKEN`: Your Discord bot token.
   - `CHANNEL_ID`: The ID of the channel where the bot will post stats.

   You can set these in your environment or create a `.env` file:

   Example `.env` file:
   ```env
   BOT_TOKEN=your-bot-token-here
   CHANNEL_ID=your-channel-id-here
   ```
2. **Create Setup files**:
   ```bash
   bash setup.sh
   ```

3. **Start docker container**:
   ```bash
   docker compose up -d
   ```


## Usage

1. **Run the bot**:
   After setting up the environment variables, start the bot by running:
   ```bash
   python bot.py
   ```

2. **Commands**:
   - `!add_user <username>`: Adds a LeetCode username to the list of users for which the bot fetches stats.
   - `!list_users`: Displays the list of currently tracked LeetCode usernames.

   Example:
   - To add a new user: `!add_user aryan0098`
   - To see the list of users: `!list_users`

3. **Bot behavior**:
   - The bot will send LeetCode stats for all users in the `username_list` every 60 seconds.
   - The bot fetches stats from LeetCode using the `LeetCodeProfileExtractor` class.

## Environment Variables

Make sure to set the following environment variables before running the bot:

- **BOT_TOKEN**: Your Discord bot token.
- **CHANNEL_ID**: The ID of the channel where you want the bot to send messages.

Example `.env` file:
```env
BOT_TOKEN=your-bot-token-here
CHANNEL_ID=your-channel-id-here
```

Alternatively, you can set these environment variables in your system:

```bash
export BOT_TOKEN="your-bot-token-here"
export CHANNEL_ID="your-channel-id-here"
```

## Credits

This bot uses the [alfa-leetcode-api](https://github.com/alfaarghya/alfa-leetcode-api.git) for fetching LeetCode user profile data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

