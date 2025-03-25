import discord
from discord.ext import commands
from discord import app_commands
from discord import Color as c
from discord import Poll
import time
import datetime

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    # sends message when bot is ready

        try:
            guild = discord.Object(id= Server ID here )
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        # syncs slash commands to server
    
        except Exception as e:
            print(f'Error syncing commands: {e}')
        # prints error message if syncing fails


    async def on_message(self, message):   
        if message.author == self.user:
            return
        # stops bot from replying to itself

        if message.content.startswith('hello'):
            await message.channel.send(f'Hi there {message.author}!')
        # says hi there when user says hello

    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('You reacted')
    # says when you react to message


intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)


GUILD_ID = discord.Object(id= Server ID here )

@client.tree.command(name="repo", description="Create a poll to see who's free for REPO", guild=GUILD_ID)
async def repo(interaction: discord.Interaction):
    allowed_mentions = discord.AllowedMentions(everyone = True)
    p = discord.Poll(question="Are you free for REPO? 🤔", duration=datetime.timedelta(hours=4))
    p.add_answer(text="Yes")
    p.add_answer(text="No")
    
    await interaction.response.send_message(poll=p, content="@everyone")
# /REPO command
# creates poll

@client.tree.command(name="hello", description="Say Hello!", guild=GUILD_ID)
async def say_hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hi there!")
# /hello command


@client.tree.command(name="printer", description="I will print whatever you give me!", guild=GUILD_ID)
async def printer(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)
# /printer command


@client.tree.command(name="embed", description="Embed demo", guild=GUILD_ID)
async def embed(interaction: discord.Interaction):
    
    embed = discord.Embed(
                        title="I am a title", 
                        url="https://www.youtube.com/", 
                        description="I am the description", 
                        color=c.red()
                        )
    embed.set_thumbnail(
                        url="https://cdn.discordapp.com/attachments/1009126141124165644/1353731722382151823/PXL_20250108_120516884.jpg?ex=67e2b869&is=67e166e9&hm=260d734d5e32158bba55636f88c440ccda9439ee5a65c98c69d27e700954f82d&"
                        )
    
    embed.add_field(name="Field 1 Title", value="This is a field", inline=False)
    embed.add_field(name="Field 2 Title", value="This is a field", inline=True)
    embed.add_field(name="Field 3 Title", value="This is a field")

    embed.set_footer(text="This is the footer!")

    embed.set_author(name=interaction.user.name, url="", icon_url=interaction.user.avatar)
    
    await interaction.response.send_message(embed=embed)
# /embed command


client.run( Bot token here )
