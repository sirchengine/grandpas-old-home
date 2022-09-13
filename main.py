import discord, os, keep_alive, asyncio, datetime, pytz

#kill 1 to reset connection
from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix=':',
  self_bot=True
)



@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = ".gg/sirch", url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"))


keep_alive.keep_alive()
client.run("OTI4MDg3Mjk3OTAyMTI5MTgy.YmTBRA.otBMljcoS7PZffk_VaPDjPddiOg", bot=False)