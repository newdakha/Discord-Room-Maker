# Discord Temp Voice Channels

![Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)
![discord.py](https://img.shields.io/badge/discord.py-latest-5865F2?logo=discord)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A Discord bot that creates a temporary voice channel when a user joins a lobby, then deletes it when it's empty.

---

## Setup

1. `pip install discord.py`
2. Set your values in the config block:

```python
GUILD_ID      = ...  # your server ID
LOBBY_CHANNEL = ...  # channel that triggers room creation
BOT_TOKEN     = ...  # your bot token
```

3. Run: `python main.py`

---

## How it works

- User joins lobby → bot creates `room <username>` (limit: 10)
- Everyone leaves → bot deletes the channel automatically
