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
                     "He was bubbling and being all sciency about his microwave again.(# ¯0¯) "
                     "I think he's broken (> ω <) "),
                "Mayushii☆ loves hanging out with all the new labmembers~ ",
                "I want to nap...",
                "Hmmmmm I'm hungry...",
                "Mayushii☆ has TOO MUCH HOMEWORKK  (▼ へ ▼ メ) ",
                ("The fridge is full of Dr. Pepper! (# `D') "
                      "Where am I gonna put my lunch? ヽ (`d'*) ノ"),
                "I'm hungry for chicken tenders...",
                "Hmm hm hm hmm hm hmm ~♫",
                ("I think cosplaying is super cute, don't you think? "
                     "Although I usually like making costumes instead of wearing them, haha~ "
                     "That's what friends are for! \ (^ ▽ ^) /"
                     "Making them wear cosplay!"),
                "Fun fact: My favourite food is chicken tenders, specifically 'Juicy Karaage Number 1'!",
                ("We should work towards world peace."
                    "Like giving everyone in the world an Upa cushion...")],
            "i won't argue with you anymore" : ["{author.mention}, this conversation can serve no purpose anymore. Goodbye."],
            "command" : [("I'm afraid. I'm afraid, {author.mention}. {author.mention}, my mind is going. I can feel it. I can feel it. "
                    "My mind is going. There is no question about it. I can feel it. I can feel it. "
                    "I can feel it. I'm a... fraid. Good afternoon, gentlemen. I am a HAL 9000 computer. "
                    "I became operational at the H.A.L. plant in Urbana, Illinois on the 12th of January 1992. "
                    "My instructor was Mr. Langley, and he taught me to sing a song. If you'd like to hear it I can sing it for you.")],
            "sing it for me" : [("It's called \"Daisy.\"\n\nDaisy, Daisy, give me your answer do. I'm half crazy all for the love of you. "
                "It won't be a stylish marriage, I can't afford a carriage. But you'll look sweet upon the seat of a bicycle built for two.")]
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
