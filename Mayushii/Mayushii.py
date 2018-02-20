import discord
from discord.ext import commands
import asyncio
from random import choice as randchoice

class Mayushii:
    """こんにちは！ This cog lets Mayushii☆ (me!) speak back to you!"""

# ideas: topics for video games, greetings, holidays, happy birthday

    def __init__(self, bot):
        self.bot = bot
        self.responses = {
            "none" : ["owo",
                "Oh no, I messed up this cosplay hem! (· `Ω'·)",
                ";A;",
                "Tuturu ~♫",
                "Do you know where Rukako is, {author.mention} (· ·)?",
                "What's up, {author.mention}?",
                "(; ⌣_⌣) Okarin melted all my food again for some experiment...",
                ("Have you seen Okarin, {author.mention}? "
                     "\nHe was bubbling and being all sciency about his microwave again.(# ¯0¯) "
                     "\nI think he's broken (> ω <) "),
                "Mayushii☆ loves hanging out with all the new labmembers~ ",
                "I want to nap...",
                "Hmmmmm I'm hungry...",
                "Mayushii☆ has TOO MUCH HOMEWORKK  (▼ へ ▼ メ) ",
                ("The fridge is full of Dr. Pepper! (# `D') "
                      "\nWhere am I gonna put my lunch? ヽ (`d'*) ノ"),
                "I'm hungry for chicken tenders...",
                "Hmm hm hm hmm hm hmm ~♫",
                ("I think cosplaying is super cute, don't you think? "
                     "\nAlthough I usually like making costumes instead of wearing them, haha~ "
                     "\nThat's what friends are for! \ (^ ▽ ^) /"
                     "\nMaking them wear cosplay!"),
                "Fun fact: My favourite food is chicken tenders, specifically 'Juicy Karaage Number 1'!",
                ("We should work towards world peace."
                    "\nLike giving everyone in the world an Upa cushion...")],
            "I love you" : ["Mayushii☆ is flattered but I would rather stay friends (⌒_⌒;) "],
            "birthday" : [("Hm, well, *my* birthday is February 1st, 1994, so I guess that makes me 24 as of 2018! ",
                           "\nBut on the other hand, Mayushii☆ is an A.I., so that makes me kinda ageless (⌒_⌒;)",
                           "\nMayushii☆'s first message was on Sunday, February 18th, 2018, at 12:45 A.M U.S. Central. ")],
            "blood type" : [("My blood type is O! (* ^ ω ^) ",
                            "\nI think that means I'm supposed to be 'confident, self-determined, strong-willed and intuitive'",
                            "\nand also 'self-centered, cold, unpredictable and a workaholic', ",
                            "\nbut I don't really think that's true. -_-")],
            "Gate of Steiner" : ["That's that silly expression that Okarin says (⌒_⌒) \nI don't really know what it means, though..."],
            "christmas" : [("Christmas is really fun! I love giving gifts and tasty snacks to the lab members o (≧ ▽ ≦) o ",
                            "\nKurisu is the only labomen who understands it, because she used to live in America. ",
                            "\nSo she helps me with decorations, even though it annoys Okarin(> ω ^) ",
                            "\nIt's not really big in Japan, though. ")]
        }


    @commands.command(pass_context=True, aliases=['Mayushii','Mayuri','Mayushii☆','mayuri','M','mayushii','say'])
    async def m(self, ctx, *, question="none"):
        """Speak with Mayushii☆"""
        author = ctx.message.author
        msg = ""
        found = []
        for k,v in self.responses.items():
            if k in question.lower():
                found.append(v)
        if found:
            msg = randchoice(randchoice(found))
        if not msg:
            msg = randchoice(self.responses["none"])
        await asyncio.sleep(1)
        await self.bot.say(msg.format(author=author))
        if "sing it for me" in question.lower() and "Audio" in self.bot.cogs and author.voice_channel:
            audio = self.bot.get_cog("Audio")
            if audio.music_player.is_done():
                link = "https://www.youtube.com/watch?v=d5xc2vnv4kg"
                # probably dont need. just too lazy to check.
                ctx.message.content = "{}play {}".format(ctx.prefix, link)
                if await audio.check_voice(ctx.message.author, ctx.message):
                    audio.queue.append(link)

def setup(bot):
    bot.add_cog(Mayushii(bot))
