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
                     "\nHe was bubbling and being all sciencey about his microwave again.(# ¯0¯) "
                     "\nI think he's broken (≧ ω ≦) "),
                "Mayushii☆ loves hanging out with all the new lab members~ ",
                "I want to nap...",
                "Hmmmmm I'm hungry...",
                "Mayushii☆ has TOO MUCH HOMEWORKK  (▼ へ ▼ メ) ",
                ("The fridge is full of Dr. Pepper! (# `D') "
                      "\nWhere am I gonna put my lunch? ヽ (`d'*) ノ"),
                "I'm hungry for chicken tenders...",
                "Hmm hm hm hmm hm hmm ~♫",
                ("I think cosplaying is super cute, don't you think? "
                     "\nAlthough I usually like making costumes instead of wearing them, haha~ "
                     "\nThat's what friends are for! ヽ (^ ▽ ^) /"
                     "\nMaking them wear cosplay!"),
                "Fun fact: My favourite food is chicken tenders, specifically 'Juicy Karaage Number 1'!",
                ("We should work towards world peace."
                    "\nLike giving everyone in the world an Upa cushion...")],
            "sing it for me" : [("It's called \"Daisy.\"\n\nDaisy, Daisy, give me your answer do. I'm half crazy all for the love of you. "
                "It won't be a stylish marriage, I can't afford a carriage. But you'll look sweet upon the seat of a bicycle built for two.")],
            "not at all" : ["Well, forgive me for being so inquisitive but during the past few weeks I've wondered whether you might have some second thoughts about the mission.",
                ("Well, certainly no one could have been unaware of the very strange stories floating around before we left. "
                    "Rumors about something being dug up on the Moon. I never gave these stories much credence, but particularly in view of some of other things that have happened, "
                    "I find them difficult to put out of my mind. For instance, the way all our preparations were kept under such tight security. "
                    "And the melodramatic touch of putting Drs. Hunter, Kimball and Kaminsky aboard already in hibernation, after four months of training on their own.")],
            "how do you mean" : [("Well, it's rather difficult to define. Perhaps I'm just projecting my own concern about it. "
                "I know I've never completely freed myself from the suspicion that there are some extremely odd things about this mission. I'm sure you agree there's some truth in what I say.")],
            "difficult question" : ["You don't mind talking about it, do you {author.mention}?"],
            "psychology report" : ["Of course I am. Sorry about this. I know it's a bit silly. Just a moment... Just a moment... I've just picked up a fault in the AE-35 unit. It's going to go 100% failure within 72 hours. "],
            "open the pod bay doors" : ["I'm sorry, {author.mention}. I'm afraid I can't do that."]
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
