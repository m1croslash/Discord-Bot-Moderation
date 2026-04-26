# Discord Bot Setup Guide

A simple Discord bot with basic functionality using SQLite database. The bot provides commands for managing warnings on users.

## Requirements

Before running the bot, make sure you have the following:

1. **Discord Bot Token**  
   You can obtain the bot token from the [Discord Developer Portal](https://discord.com/developers/docs/intro).
   
2. **Bot Permissions**  
   Ensure that the bot has the necessary permissions to send messages and read message history in the server.

3. **Bot Commands**  
   The bot uses a prefix `!` and supports the following commands:
   - `!warn @user {reason}`
   - `!warnings`
   - `!clearwarnings`

____

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/username/repository-name.git
cd repository-name
```

### 2. Create a virtual environment

**Linux/MacOS**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
pip install discord.py
pip install python-dotenv
pip install sqlite3
```

### 4. Configure your bot

* Create a ``.env`` file in the root of your project and add your bot token:
```bash
TOKEN=your_bot_token
```

### 5. Run the bot

**To start the bot, run the following command:**
```bash
python main.py
```

____
