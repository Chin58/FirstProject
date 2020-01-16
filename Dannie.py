import random
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")
TOKEN = "Mzg1ODE3MDI0NzAzNDk2MjAy.XiCLew.Kn5p93GlVVx6Zdg1hStt2bv3hhs"

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='4g')
async def eight_ball():
    possible_responses = [
        'ภีม',
    ]
    await client.say(random.choice(possible_responses))


@client.command()
async def square(number) :
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))
  

client.run(TOKEN)
