### Internship Task: Event Ticketing Bot for Telegram

# Event Ticketing Telegram Bot

This Telegram bot allows users to get free tickets for a particular event. Using this bot, users can get:

1. **Event Information:** Provides users with details about the event.
2. **Ticket Request:** Allows users to request free tickets through the bot.
3. **User Registration:** Collects necessary user information during the ticket request.
4. **Group Invitation:** Adds users to a specific Telegram group upon successful ticket request.

## Prerequisites

1. Install Python.
2. Install the necessary Python packages:

```bash
pip install python-telegram-bot telethon python-dotenv

```
## Configuration

1. Create a `.env` file in the `src` folder.
2. Add the following variables to the `.env` file:

```
    TOKEN='7458561002:AAE5_kS0g_1oU45cEjxL6ix2X5dmgcec7fA'
    BOT_USERNAME='Event_Ticketing_Telegram_bot'
    API_HASH='4f21d03b65fe9a736ca7c79422d9ac2d'
    API_ID='27066935'
    ADMIN_PHONE_NUMBER='+94777973793'
    CHANNEL_ID=-1002215923063
    CHANNEL_ACCESS_HASH=6891311242554153966
```

## Running the Bot

1. Run the `main.py`

```bash
python main.py
```

## Interacting with the Bot

1. Go to Telegram and search for `Event_Ticketing_Telegram_bot`.
2. Send the `/start` command to interact with the bot and get free tickets.

- **Bot Commands:**
  - `/start` - Greets the user and provides event details.
  - `/register` - Initiates the ticket registration process.
  - `/cancel` - cancel the ticket registration process.
  - `/help` - Provides help and usage instructions.


### Folder Structure

Folder structure for the project:

```
CeyLabs-TGBot-EventRSVPBot/
│
├── src/
│   ├── main.py
│   ├── .env
│   └── utils/
│       ├── add_group.py
│       ├── DatabaseHandler.py
│       ├── event_info.py
│       └── registation.py
│
├── tests/
│   └── channel_access_hash.py
│
├── README.md
├── .gitignore
└── composer.json
```

- `src/` contains the main application code.
- `utils/` contains utility scripts for handling specific functionalities like event info, ticket requests, group invitations, and database operations.
- `README.md` contains detailed instructions on setting up and running the bot.
- `.gitignore` specifies files and directories to be ignored by Git.

