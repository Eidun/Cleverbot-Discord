import discord
from discord.ext import commands
import asyncio


class Game:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ball(self, ctx):
        tmp = await self.bot.say('Hey,{0.display_name}, look at this ball!'.format(ctx.message.author))
        await asyncio.sleep(3)
        for i in range(10):
            msg = await ball(i)
            await self.bot.edit_message(tmp, msg)
        for i in range(10, 0, -2):
            msg = await ball(i)
            await self.bot.edit_message(tmp, msg)
        await self.bot.delete_message(tmp)
        await self.bot.delete_message(ctx.message)


async def ball(spaces):
    await asyncio.sleep(0.5)
    msg = '```\n'
    for i in range(spaces):
        msg += '  '
    msg += 'o'
    msg += '\n```'
    return msg


def setup(bot):
    bot.add_cog(Game(bot))
