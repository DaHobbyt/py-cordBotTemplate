import discord
from discord.ext import commands

class Convert(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='convert', description='Convert user ID to username')
    async def convert(self, ctx, user_id: str):
        try:
            user = await self.bot.fetch_user(int(user_id))
            embed = discord.Embed(title='User Information', description=f'Username: {user.name}#{user.discriminator}', color=discord.Color.blue())
            embed.set_thumbnail(url=user.avatar.url)
            await ctx.respond(embed=embed)
        except discord.HTTPException as e:
            await ctx.respond(f'Error: {e.text}')

def setup(bot):
    bot.add_cog(Convert(bot))
