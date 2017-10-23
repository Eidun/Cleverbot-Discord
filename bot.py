import sys
import traceback
import discord
from discord.ext import commands


description = '''This is an amazing bot'''

modules = {'cogs.game', 'cogs.talking', }

bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print('Bot initiating...')
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(game=discord.Game(name='rol con vosotros'))

    print('Loading systems...')
    if __name__ == '__main__':
        for module in modules:
            try:
                bot.load_extension(module)
                print('\t' + module)
            except Exception as e:
                print(f'Error loading module {module}', file=sys.stderr)
                traceback.print_exc()
    print('Systems 100%')
    print('------')

bot.edit_channel_permissions

@bot.event
async def on_message(message):
    print(message.content)
    print(message.attachments)


# Testbot-9000
bot.run('MzcyMDcyMjQyNzgxMDkzODg4.DM-4Wg.03FPGnRXCVP2LzLe1VuWgNYO3bY')
