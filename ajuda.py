import discord

bot = discord.Bot()

@bot.slashcommand()
async def ping(ctx):
    print(ping)


bot.run()