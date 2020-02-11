# We don't need many libraries for this (yet)
from discord.ext import commands
from discord.utils import get
import sys

# Get system arguments, save them into a array and print them
args = sys.argv
print(args)

# Try to fetch the token location in launch args
try:
    TOKEN_Location = args.index("-token") + 1
    TOKEN = args[TOKEN_Location]
except Exception:  # If token not specified
    print("Token not specified! Usage: python(3) main.py -token {TOKEN HERE}")
    exit(2)
# Set up the basic bot
# command_prefix:   the prefix that is run before the command (for example: /twitch)
# description:      The description of the bot - Not really needed as it's not seen by the user
bot = commands.Bot(command_prefix='/',
                   description="Twitch Notification System originally made for the lad donut")

# Remove help page as it'd only contain one command anyways - Might be reintroduced at some point
bot.remove_command('help')

# List of User IDs that are allowed to run specific commands
allowit = [130838223067807745, 275678584712986624]

# The ID of the role that should get the Notification
roleid = 676380075276501052

# Fill in the streamer's name and link
StreamerName = "STREAMER"
StreamerLink = "https://www.twitch.tv/___"


# Function that runs when the bot is ready and fully running
@bot.event
async def on_ready():
    print("Bot is running!")


@bot.command()  # The twitch command, primary function of this bot
async def twitch(ctx, *, message=StreamerName + " is live! Go watch his stream!"):
    # message: the message tag, the default Message is set here.
    # Check if the user who's running the command is in the allowit list
    role = get(ctx.guild.roles, id=roleid)
    if ctx.author.id not in allowit:  # Output if it isn't
        await ctx.send("> " + ctx.message + "\nYou don't have permission to run this command!")
    else:  # Output if it is

        # Make the Role mentionable
        await role.edit(mentionable=True, reason=f"[ {ctx.author} ] twitch command - Enable mentionable Role")
        # Send the message containing the tag
        await ctx.send("<@&" + str(roleid) + "> " + str(message) + " " + StreamerLink)
        # Make it un-mentionable instantly after
        await role.edit(mentionable=False, reason=f"[ {ctx.author} ] twitch command - Disable mentionable Role")


bot.run(TOKEN)
