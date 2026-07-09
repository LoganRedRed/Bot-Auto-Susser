import discord
import time

BotDirectory = r"this won't work until you put it in" # The folder the script is in.

StaffRole = 1087098728353104062
IdentificationRole = 1519422154855415981
LockAwayRole = 1224813669469257858
LockAwayChannel = 1224813137660874865
LogChannel = 1103121682698358804

BotCloseEmoji = "<:BotClosed:1523873650477109289>"
BotOpenEmoji = "<:BotOpen:1523873663995346944>"
BotPrefix = "$"

AllowedMentions = discord.AllowedMentions(users=False)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.typing = False
intents.presences = False

FileSecret = open(rf"{BotDirectory}\BAS Secret.txt", "r", encoding="utf-8")
TheSecret = FileSecret.read()
FileSecret.close()

client = discord.Client(intents=intents)

Logging = open(rf"{BotDirectory}\Logs\BAS Log - {time.strftime(r"%b-%d-%y %H %M %S")}.txt", "x+t", 1, encoding="utf-8")
# Logging.write(f"{time.strftime(r"%b-%d-%y %H:%M:%S")} - \n")

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    Logging.write(f"{time.strftime(r"%b-%d-%y %H:%M:%S")} - We have logged in as {client.user}\n\n")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if(f"{StaffRole}" not in f"{message.author.roles}"):
        return

    if(message.content.startswith(f"{client.user.mention}unsus ") or message.content.startswith(rf"{BotPrefix}unsus ")): # UNSUS
        Logging.write(f"{time.strftime(r"%b-%d-%y %H:%M:%S")} - UnSus command activated\n")
        UserID = message.content.split(" ", maxsplit=2)[1].strip("<@!>")
        if(len(UserID) >= 17 and len(UserID) <= 20 and str.isdecimal(UserID)):
            try:
                # LockawayC = client.get_channel(LockAwayChannel) # This is here in case you wanted to send something in there.
                LogC = client.get_channel(LogChannel)
                LockAwayR = message.guild.get_role(LockAwayRole)
                member = await message.guild.query_members(user_ids=[UserID])
                if(f"{LockAwayRole}" in f"{member[0].roles}"):
                    await member[0].remove_roles(LockAwayR, reason=f"UnSussed by {message.author.name}.")
                    await message.channel.send(f"<@{member[0].id}> has been unSussed.", delete_after=10)
                    await LogC.send(f"{BotOpenEmoji} <@{member[0].id}>({member[0].id}) has been unSussed by <@{message.author.id}>. {BotOpenEmoji}", allowed_mentions=AllowedMentions)
                    Logging.write(f"{time.strftime(r"%b-%d-%y %H:%M:%S")} - {member[0].name}({member[0].id}) was unSussed manually by {message.author.name}.\n")
                    print(f"{time.strftime(r"%b-%d-%y %H:%M:%S")} - {member[0].name}({member[0].id}) was unSussed manually by {message.author.name}.\n")
                else:
                    await message.channel.send(f"<@{member[0].id}> doesn't have the Sus.", delete_after=10)
                    Logging.write(f"{time.strftime(r"%b-%d-%y %H:%M:%S")} - UnSus was attempted on {member[0]} but they lack the Sus.\n")
            except Exception as err:
                Logging.write(f"{time.strftime(r"%b-%d-%y %H:%M:%S")} - ERROR ERROR ERROR\n{err=}   {type(err)=}\n")
                await message.channel.send(f"Command related. This message will automatically delete in thirty seconds.\n`{err=}    {type(err)=}`", delete_after=30)
                raise
        else:
            await message.channel.send(f"{message.content.split(" ", maxsplit=2)[1]} is not a valid UID.", delete_after=10)
            Logging.write(f"{time.strftime(r"%b-%d-%y %H:%M:%S")} - Was given invalid UID ({message.content.split(" ", maxsplit=2)[1]}) by {message.author.name}.\n")
        await message.delete(delay=10)
        return

    if(message.content.startswith(f"{client.user.mention}sus ") or message.content.startswith(rf"{BotPrefix}sus ")): # SUS
        Logging.write(f"{time.strftime(r"%b-%d-%y %H:%M:%S")} - Sus command activated\n")
        UserID = message.content.split(" ", maxsplit=2)[1].strip("<@!>")
        if(len(UserID) >= 17 and len(UserID) <= 20 and str.isdecimal(UserID)):
            try:
                LockawayC = client.get_channel(LockAwayChannel)
                LogC = client.get_channel(LogChannel)
                LockAwayR = message.guild.get_role(LockAwayRole)
                member = await message.guild.query_members(user_ids=[UserID])
                if(f"{LockAwayRole}" not in f"{member[0].roles}"):
                    await member[0].edit(roles=[LockAwayR], reason=f"Sussed by {message.author.name}.")#
                    await message.channel.send(f"<@{member[0].id}> has been Sussed.", delete_after=10)
                    await LogC.send(f"{BotCloseEmoji} <@{member[0].id}>({member[0].id}) has been Sussed by <@{message.author.id}>. {BotCloseEmoji}", allowed_mentions=AllowedMentions)
                    await LockawayC.send(f"{BotCloseEmoji} <@{member[0].id}>, you have been manually Sussed. You were found to be a suspicious user based on Discord's signaling or a staff member's judgment. Ping a staff member for an appeal. {BotCloseEmoji}")
                    Logging.write(f"{time.strftime(r"%b-%d-%y %H:%M:%S")} - {member[0].name}({member[0].id}) was Sussed manually by {message.author.name}.\n")
                    print(f"{time.strftime(r"%b-%d-%y %H:%M:%S")} - {member[0].name}({member[0].id}) was Sussed manually by {message.author.name}.\n")
                else:
                    await message.channel.send(f"<@{member[0].id}> Has too much Sus.", delete_after=10)
                    Logging.write(f"{time.strftime(r"%b-%d-%y %H:%M:%S")} - Sus was attempted on {member[0]} but they're too Sussy.\n")
            except Exception as err:
                Logging.write(f"{time.strftime(r"%b-%d-%y %H:%M:%S")} - ERROR ERROR ERROR\n{err=}   {type(err)=}\n")
                await message.channel.send(f"Command related. This message will automatically delete in thirty seconds.\n`{err=}    {type(err)=}`", delete_after=30)
                raise
        else:
            await message.channel.send(f"{message.content.split(" ", maxsplit=2)[1]} is not a valid UID.", delete_after=10)
            Logging.write(f"{time.strftime(r"%b-%d-%y %H:%M:%S")} - Was given invalid UID (message.content.split(" ", maxsplit=2)[1]) by {message.author.name}.\n")
        await message.delete(delay=10)

@client.event
async def on_member_update(before, after):
    if(before.roles != after.roles):
        if(f"{IdentificationRole}" in f"{after.roles}" and not f"{LockAwayRole}" in f"{after.roles}"):
            try:
                LockawayC = client.get_channel(LockAwayChannel)
                LogC = client.get_channel(LogChannel)
                LockAwayR = after.guild.get_role(LockAwayRole)
                await after.edit(roles=[LockAwayR], reason="Selected the poopy bot role.")
                await LogC.send(f"{BotCloseEmoji} <@{after.id}>({after.id}) has been Auto-Sussed. {BotCloseEmoji}")
                await LockawayC.send(f"{BotCloseEmoji} <@{after.id}>, you have been Auto-Sussed. Ping a staff member for an appeal. {BotCloseEmoji}")
                Logging.write(f"{time.strftime(r"%b-%d-%y %H:%M:%S")} - {after.name}({after.id}) was Sussed automatically.\n")
                print(f"{time.strftime(r"%b-%d-%y %H:%M:%S")} - {after.name}({after.id}) was Sussed automatically.\n")
            except Exception as err:
                await LogC.send(f"<@651551210125524998>\n{err=}   {type(err)=}") # This is so I'm notified of errors. If you don't want this, just remove it. If you do, change the UID to yours.
                Logging.write(f"{time.strftime(r"%b-%d-%y %H:%M:%S")} - ERROR ERROR ERROR\n{err=}   {type(err)=}\n")
                raise


client.run(f"{TheSecret}")


# py "{BotDirectory}\Bot Auto-Susser.py"

# https://discordpy.readthedocs.io/en/stable/faq.html

# https://docs.python.org/3/
