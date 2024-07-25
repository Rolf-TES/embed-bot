import discord; from discord.ext import commands

intents = discord.Intents.default(); intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command(name='embed')
async def send_embed(ctx, *, args):
    args = [arg.strip() for arg in args.split('|')]
    if len(args) != 4:
        await ctx.send('Proper syntax: Author | Title | Description | Image URL')
        return
    author, title, description, url = args
    embed = discord.Embed(title=title, description=description, color=0x080808) # Change color here.
    embed.set_author(name=author); embed.set_image(url=url)
    await ctx.send(embed=embed)
bot.run('YOUR_BOT_TOKEN')
