# Telegram Forwarder Bot

This bot forwards messages from one Telegram group to another, modifying certain parts of the message content.

## Features

- Forward messages between Telegram groups
- Modify message content before forwarding
- Configurable source and destination groups

## Setup

1. Clone this repository:

```
git clone https://github.com/pmoluno/telegram-forwarder-bot.git

cd telegram-forwarder-bot
```

2. Create a virtual environment and activate it:

```
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

3. Install the required packages:

```
pip install -r requirements.txt
```

4. Create a `config.ini` file in the root directory with the following content:

```ini
API_ID = your_api_id
API_HASH = your_api_hash
BOT_TOKEN = your_bot_token
SOURCE_GROUP = -1001234567890
DESTINATION_GROUP = -1009876543210
```
Replace the placeholders with your actual Telegram API credentials and group IDs.

5. Run the bot:

```
python main.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
