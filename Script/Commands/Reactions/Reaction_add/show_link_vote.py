from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def reaction_add_show_link_vote(self, reaction, member):
    if (reaction.emoji == Emojis["Link"]) and (reaction.message.embeds[0].title == "Links to promote the bot :"):
        embed_clean = create_embed("Links to promote the bot :", "Top.gg : https://top.gg/bot/704688212832026724\nDiscord.Bots.gg : https://discord.bots.gg/bots/704688212832026724\nArcane-Center.xyz : https://arcane-center.xyz/bot/704688212832026724\nWonderBotList.com : https://wonderbotlist.com/en/bot/704688212832026724", member.guild.me.color, "Thanks you for your support !", member.guild.me.avatar_url)
        await reaction.message.edit(embed=embed_clean)
    return
