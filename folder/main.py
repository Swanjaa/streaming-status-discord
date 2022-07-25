import discord, os ,pytz, asyncio, json
from discord.ext import tasks, commands
import keep_alive


token = os.environ['Token']


bot = commands.Bot(command_prefix=None,self_bot=True)


#here it loops the status if you want it to be looped if you dont
#you can keep adding more and more states just copy and paste it below each other
async def status_task():
    while True:
        await bot.change_presence(activity=discord.Streaming(name="anything you want!", url='twitch or yt'))
        await asyncio.sleep(40)
        await bot.change_presence(activity=discord.Streaming(name="anything you want!", url='twitch or yt'))
        await asyncio.sleep(40)

#to hide your token go on the secret environment and paste put the name which is Token and your token and run it 
@bot.event
async def on_connect():
  bot.loop.create_task(status_task())
  #await bot.change_presence(activity = discord.Streaming(name ="wtv you want", url = "twitch or yt"))

    
keep_alive.keep_alive()  
bot.run(token, bot=False)
