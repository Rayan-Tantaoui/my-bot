import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

secret_role = "gigganigga"

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")

@bot.event 
async def on_member_join(member):
    await member.send(f"welcome to the server {member.name}")

@bot.event
async def on_member_join(member):
    # Find the 'general' channel
    general_channel = discord.utils.get(member.guild.channels, name="general")

    if general_channel:
        # Send the welcome message
        await general_channel.send(f"Welcome to the server, {member.mention}! We're glad to have you here.")
    else:
        # Log if channel not found
        print(f"Could not find 'general' channel in {member.guild.name}.")


@bot.event
async def on_message(message):
    if message.author == bot.user:
       return
    if "shit" in message.content.lower():
        await message.delete()    
        await message.channel.send(f"{message.author.mention} - don't use that word!")
    await bot.process_commands(message) 
    if "nigga" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} - no racism allowed!")
    if "polish femboy" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} - ikhan!")     


#!hello
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}")

@bot.command(name='helpme', help='Displays a list of all available commands.')
async def help_command(ctx):
    help_text = "Here are my commands:\n"
    for command in bot.commands:
        if command.help:
            help_text += f"`!{command.name}`: {command.help}\n"
        else:
            help_text += f"`!{command.name}`: No description available.\n"
    await ctx.send(help_text)


@bot.command()
async def assign(ctx):
    role = discord.utils.get(f"{ctx.author.mention} is now assigned to {secret_role}")
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} is now assigned to {secret_role}")
    else:
        await ctx.send("Role doesn't exist")

@bot.command()
async def remove(ctx):
    role = discord.utils.get(f"{ctx.author.mention} is now assigned to {secret_role}")
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} has had the {secret_role} removed")
    else:
        await ctx.send("Role doesn't exist")



    



bot.run(token, log_handler=handler, log_level=logging.DEBUG)
