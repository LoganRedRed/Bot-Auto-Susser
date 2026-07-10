# Bot Auto-Susser
Userbots often pick roles from the same spot when onboarding, so a simple honeypot role can be used to identify them. This bot quarantines them when they select that role. It also allows for manual quarantining and freeing.


# Setup:

## 1. Creating a Discord bot

I recomend this: https://discordpy.readthedocs.io/en/stable/discord.html

The extra permissions that the bot needs are: `Manage Roles` and `Manage Messages`

The rest should be in the default permissions of your server. There's also no need to give it admin perms.

Sidenote: you should disable `Use External Apps` in your default permissions to prevent easy raiding of your server.

## 2. Getting dependencies

Download Python: https://www.python.org/downloads/

Downloading Discord.py: https://discordpy.readthedocs.io/en/stable/intro.html

## 3. Downloading and configuring the bot

Create a folder for your bot

Download `Bot Auto-Susser.py`, create/download `BAS Secret.txt`, and create a folder named `Logs`, all in the main folder you just made

Put your bot token inside of `BAS Secret.txt` (make sure you never share it with anybody)

Configure `Bot Auto-Susser.py` in an editor of your choosing (notepad is fine) with values from your server (the emojis can come from the bot or the server, either way is fine)

## 4. Running the bot

You just double-click on the `Bot Auto-Susser.py` file, and it does its thing

If you want to go the extra mile, you can create a shortcut to the file in `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp` so you don't have to launch it when you restart your computer

## 5. Getting help

If you need help with anything, you can join my Discord server: https://discord.gg/gW68EZ4gkc
