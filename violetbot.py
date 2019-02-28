from discord.ext import commands
import discord.utils
import discord
import json
import os

with open("config.json") as file:
    config = json.load(file)

bot = commands.Bot(command_prefix=config['prefix'], description="None")



@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))


@bot.command()
async def kick(ctx, user_kick : discord.Member):
    role = discord.utils.get(user_kick.guild.roles, name=config['perm_role'])
    if role in ctx.message.author.roles:
        await user_kick.kick(reason=None)
    else:
        await ctx.send(content="Permission denied!")



@bot.command()
async def ban(ctx, user_ban : discord.Member):
    role = discord.utils.get(user_ban.guild.roles, name=config['perm_role'])
    print(role)
    if role in ctx.message.author.roles:
        await user_ban.ban(reason=None)
    else:
        await ctx.send(content="Permission denied!")


@bot.command()
async def purne(ctx, amount):
    role = discord.utils.get(ctx.message.user.guild.roles, name=config['perm_role'])
    if role in ctx.message.author.roles:
        await ctx.channel.purge(limit=amount)
    else:
        await ctx.send(content="Permission denied!")



@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name=config['autojoin_rolename'])
    await member.add_roles(role, reason=None)

bot.run(str(os.environ.get('BOT_TOKEN')))
