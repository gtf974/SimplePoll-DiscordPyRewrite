#IMPORTS NEEDED

import discord
from discord.ext import commands


#THE COMMAND


@commands.command()
async def poll(ctx, *, text):
    number = {1: ":one:", 2: ":two:", 3: ":three:", 4: ":four:", 5: ":five:", 6: ":six:", 7: ":seven:", 8: ":eight:",9: ":nine:"}
    emoji = {1: "1️⃣", 2: "2️⃣", 3: "3️⃣", 4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣"}
    count = 1
    countemoji = 1
    split = text.split('" "')
    split[-1] = split[-1].replace("\"", "")
    question = split.pop(0).replace("\"", "")
    if len(split) > 9 or len(split) < 2:
        await ctx.send("> You must have at least 2 answers and at most 9 answers.")
    else:
        descembed = "\n"
        numberRes = len(split)
        while count <= numberRes:
            descembed += number[count] + " " + split[count - 1] + "\n"
            count += 1
        embedpoll = discord.Embed(title="**" + question + ":**", description=descembed, colour=discord.Colour.green()) #You can select another colour by replacing green by another colour. For example: discord.Colour.blue() // Here's the link for the colors: https://discordpy.readthedocs.io/en/latest/api.html?#colour
        embed = await ctx.send(embed=embedpoll)
        while countemoji <= numberRes:
            await embed.add_reaction(emoji[countemoji])
            countemoji += 1
        await ctx.message.delete()