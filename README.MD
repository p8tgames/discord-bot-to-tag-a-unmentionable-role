# Simple Twitch-Streamer based bot to notify people on your discord when you're live.

To get started, type in your terminal with pip and python in the PATH:
`pip install -r requirements.txt`. Afterwards, open up the file `main.py` in an editor of your choice.


# Editing main.py
Please do **not** rename `main.py`. Otherwise the program will break.

## Insert Streamer Name and Link

Search for the variable `StreamerName` and `StreamerLink`. Replace the 2 default values with the value of your choice.
Now, go to Discord and enable developer mode. Use it to copy the Role ID of the role that should be notified. Make sure it's set to unmentionable. Copy the Role ID and paste it under the variable `roleid`. Now, get a list of people that are allowed to use the bot and place them in the array `allowit`.

If you want to change the command from /twitch to, for example, /youtube, change the line `async def twitch [...]` to `async def youtube [...]`.

## Starting the bot

You can run the bot locally or on heroku. For that, just deploy the project normally. Make sure you download your forked repo and upload it from your pc, otherwise your TOKEN could be revealed to the internet.
Now, start it using `python3 main.py -token {TOKEN HERE}`. For heroku, create a file called `Procfile` with the content `worker: python3 main.py -token {TOKEN HERE}`.

## Notify users
Now add the bot to your server. It should appear online.
Once the bot is running (check with the /status command in your server) you can now use the command /twitch (or whatever you configured it to) and it will ping everyone that has the role specified.

## Report issues
Please create an Issue here on GitHub and if you already have a fix create a Pull Request!
