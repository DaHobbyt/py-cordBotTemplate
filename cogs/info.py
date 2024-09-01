import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='info', description='Show server information')
    async def info(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(title=guild.name, description=guild.description, color=discord.Color.blue())
        embed.set_thumbnail(url=guild.icon.url)
        embed.add_field(name='Server ID', value=guild.id, inline=False)
        embed.add_field(name='Owner', value=guild.owner.mention, inline=False)
        embed.add_field(name='Member Count', value=guild.member_count, inline=False)
        embed.add_field(name='Role Count', value=len(guild.roles), inline=False)
        embed.add_field(name='Channel Count', value=len(guild.channels), inline=False)
        embed.add_field(name='Created At', value=guild.created_at.strftime('%Y-%m-%d %H:%M:%S'), inline=False)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))
