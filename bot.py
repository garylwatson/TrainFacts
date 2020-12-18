import discord

#Retrieve key
f = open("token.txt", "r")
token = f.read()
f.close()

#Open connection
bot = discord.Client()

#Log in
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

#Detect and react to message
@bot.event
async def on_message(message):
    #Is the message from ourselves
    if message.author == bot.user:
        return

    if message.content.startswith('!trainfact'):
        await message.channel.send('trainfact!')

bot.run(token)