# Simple Setup Guide
* **Discord Bot Token from** [Discord Developer Portal](https://discord.com/developers/docs/intro)
* **Don't forget to give the bot permissions so it can send messages and read history message!**
* **Bot don't use slash-commands. Bot Prefix '!'**
* **Bot use SQLite DB**
___
## Git 
```bash
git clone https://github.com/username/repository-name.git
```
```bash
cd repository-name
```
___
## Linux/MacOS
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
## Windows 10/11
```bash
python -m venv venv
```
```bash
venv\Scripts\activate
```
___
## Install dependencies
```bash
pip install -r requirements.txt
```
```bash
pip install discord.py
```
```bash
pip install python-dotenv
```
```bash
pip install sqlite3
```
___
## Run script
* **You need run ```main.py``` script**
```bash
python main.py
```
___
### Bot commands
```!warn @user {reason}```
```!warnings @user```
```!clearwarnings @user```
___
