# █ █ ▀ █▄▀ ▄▀█ █▀█ ▀    ▄▀█ ▀█▀ ▄▀█ █▀▄▀█ ▄▀█
# █▀█ █ █ █ █▀█ █▀▄ █ ▄  █▀█  █  █▀█ █ ▀ █ █▀█
#
#              © Copyright 2022
#
#          https://t.me/hikariatama
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta pic: https://img.icons8.com/stickers/100/000000/commit-git.png
# meta developer: @hikariatama
# scope: hikka_only

import logging
import os
from random import choice

from telethon.tl.types import Message

from .. import loader, utils

logger = logging.getLogger(__name__)
commits = ["One does not simply merge into master", "Merging the merge", "Another bug bites the dust", "de-misunderestimating", "XUPPERNAMEX, WE WENT OVER THIS. EXPANDTAB.", "XUPPERNAMEX, WE WENT OVER THIS. C++ IO SUCKS.", "Some shit.", "See last commit", "[no message]", "add actual words", "I CAN HAZ COMMENTZ.", "giggle.", "Whatever.", "Finished fondling.", "FONDLED THE CODE", "this is how we generate our shit.", "unh", "It works!", "unionfind is no longer being molested.", "Well, it's doing something.", "I'M PUSHING.", "Whee.", "Whee, good night.", "It'd be nice if type errors caused the compiler to issue a type error", "Fucking templates.", "I hate this fucking language.", "marks", "that coulda been bad", "hoo boy", "It was the best of times, it was the worst of times", "Fucking egotistical bastard. adds expandtab to vimrc", "if you're not using et, fuck off", "WHO THE FUCK CAME UP WITH MAKE?", "This is a basic implementation that works.", "By works, I meant 'doesnt work'.  Works now..", "Last time I said it works? I was kidding.  Try this.", "Just stop reading these for a while, ok..", "Give me a break, it's 2am.  But it works now.", "Make that it works in 90% of the cases.  3:30.", "Ok, 5am, it works.  For real.", "FOR REAL.", "I don't know what these changes are supposed to accomplish but somebody told me to make them.", "I don't get paid enough for this shit.", "fix some fucking errors", "first blush", "So my boss wanted this button ...", "uhhhhhh", "forgot we're not using a smart language", "include shit", "To those I leave behind, good luck!", "things occurred", "i dunno, maybe this works", "8==========D", "No changes made", "whooooooooooooooooooooooooooo", "clarify further the brokenness of C++. why the fuck are we using C++?", "(\\ /)<br/>(O.o)<br/>(&gt; &lt;) Bunny approves these changes.", ".", "Friday 5pm", "changes", "A fix I believe, not like I tested or anything", "Useful text", "pgsql is being a pain", "pgsql is more strict, increase the hackiness up to 11", "c&p fail", "syntax", "XNAMEX sucks", "XUPPERNAMEX SUCKS", "fix", "just shoot me", "arrrggghhhhh fixed!", "someone fails and it isn't me", "Gross hack because XNAMEX doesn't know how to code", "totally more readable", "better grepping", "fix", "fix bug, for realz", "fix /sigh", "Does this work", "MOAR BIFURCATION", "bifurcation", "REALLY FUCKING FIXED", "FIX", "better ignores", "More ignore", "more ignores", "more ignores", "more ignores", "more ignores", "more ignores", "more ignored words", "more fixes", "really ignore ignored worsd", "fixes", "/sigh", "fix", "fail", "pointless limitation", "eppic fail XNAMEX", "omg what have I done?", "added super-widget 2.0.", "tagging release w.t.f.", "I can't believe it took so long to fix this.", "I must have been drunk.", "This is why the cat shouldn't sit on my keyboard.", "This is why git rebase is a horrible horrible thing.", "ajax-loader hotness, oh yeah", "XNAMEX broke the regex, lame", "small is a real HTML tag, who knew.", "WTF is this.", "Do things better, faster, stronger", "Fixed a bug cause XNAMEX said to", "Use a real JS construct, WTF knows why this works in chromium.", "Added a banner to the default admin page. Please have mercy on me =(", "needs more cow bell", "Switched off unit test X because the build had to go out now and there was no time to fix it properly.", "Updated", "I must sleep... it's working... in just three hours...", "I was wrong...", "Completed with no bugs...", "Fixed a little bug...", "Fixed a bug in NoteLineCount... not seriously...", "woa!! this one was really HARD!", "Made it to compile...", "changed things...", "touched...", "i think i fixed a bug...", "perfect...", "Moved something to somewhere... goodnight...", "oops, forgot to add the file", "Corrected mistakes", "oops", "oops!", "put code that worked where the code that didn't used to be", "Nothing to see here, move along", "I am even stupider than I thought", "I don't know what the hell I was thinking.", "fixed errors in the previous commit", "Committed some changes", "Some bugs fixed", "Minor updates", "Added missing file in previous commit", "bug fix", "typo", "bara bra grejjor", "Continued development...", "Does anyone read this? I'll be at the coffee shop accross the street.", "That's just how I roll", "work in progress", "minor changes", "some brief changes", "assorted changes", "lots and lots of changes", "another big bag of changes", "lots of changes after a lot of time", "LOTS of changes. period", "XNAMEX made me do it", "Test commit. Please ignore", "I'm just a grunt. Don't blame me for this awful PoS.", "I did it for the lulz!", "I'll explain this when I'm sober .. or revert it", "Obligatory placeholder commit message", "A long time ago, in a galaxy far far away...", "Fixed the build.", "Fixing XNAMEX's bug.", "Fixing XNAMEX's bugs.", "various changes", "One more time, but with feeling.", "Handled a particular error.", "Fixed unnecessary bug.", "Removed code.", "Added translation.", "Updated build targets.", "Refactored configuration.", "Locating the required gigapixels to render...", "Spinning up the hamster...", "Shovelling coal into the server...", "Programming the flux capacitor", "The last time I tried this the monkey didn't survive. Let's hope it works better this time.", "I should have had a V8 this morning.", "640K ought to be enough for anybody", "pay no attention to the man behind the curtain", "a few bits tried to escape, but we caught them", "This is the last time we let XNAMEX commit ascii porn in the comments.", "Who has two thumbs and remembers the rudiments of his linear algebra courses?  Apparently, this guy.", "workaround for ant being a pile of fail", "Don't push this commit", "rats", "squash me", "fixed mistaken bug", "Final commit, ready for tagging", "-m \\'So I hear you like commits ...\\'", "epic", "need another beer", "Well the book was obviously wrong.", "lolwhat?", "Another commit to keep my CAN streak going.", "I cannot believe that it took this long to write a test for this.", "TDD: 1, Me: 0", "Yep, XNAMEX was right on this one.", "Yes, I was being sarcastic.", "Apparently works-for-me is a crappy excuse.", "tl;dr", "I would rather be playing SC2.", "Crap. Tonight is raid night and I am already late.", "I know what I am doing. Trust me.", "You should have trusted me.", "Is there an award for this?", "Is there an achievement for this?", "I'm totally adding this to epic win. +300", "This really should not take 19 minutes to build.", "fixed the israeli-palestinian conflict", "SHIT ===> GOLD", "Committing in accordance with the prophecy.", "It compiles! Ship it!", "LOL!", "Reticulating splines...", "SEXY RUSSIAN CODES WAITING FOR YOU TO CALL", "s/import/include/", "extra debug for stuff module", "debug line test", "debugo", "remove debug<br/>all good", "debug suff", "more debug... who overwrote!", "FUCKING XUPPERNAMEX", "these confounded tests drive me nuts", "For great justice.", "QuickFix.", "oops - thought I got that one.", "removed echo and die statements, lolz.", "somebody keeps erasing my changes.", "doh.", "pam anderson is going to love me.", "added security.", "arrgghh... damn this thing for not working.", "jobs... steve jobs", "and a comma", "this is my quickfix branch and i will use to do my quickfixes", "Fix my stupidness", "and so the crazy refactoring process sees the sunlight after some months in the dark!", "gave up and used tables.", "[Insert your commit message here. Be sure to make it descriptive.]", "Removed test case since code didn't pass QA", "removed tests since i can't make them green", "stuff", "more stuff", "Become a programmer, they said. It'll be fun, they said.", "Same as last commit with changes", "foo", "just checking if git is working properly...", "fixed some minor stuff, might need some additional work.", "just trolling the repo", "All your codebase are belong to us.", "Somebody set up us the bomb.", "should work I guess...", "To be honest, I do not quite remember everything I changed here today. But it is all good, I tell ya.", "well crap.", "herpderp (redux)", "herpderp", "Derp", "derpherp", "Herping the derp", "sometimes you just herp the derp so hard it herpderps", "Derp. Fix missing constant post rename", "Herping the fucking derp right here and now.", "Derp, asset redirection in dev mode", "mergederp", "Derp search/replace fuckup", "Herpy dooves.", "Derpy hooves", "derp, helper method rename", "Herping the derp derp (silly scoping error)", "Herp derp I left the debug in there and forgot to reset errors.", "Reset error count between rows. herpderp", "hey, what's that over there?!", "hey, look over there!", "It worked for me...", "Does not work.", "Either Hot Shit or Total Bollocks", "Arrrrgggg", "Don’t mess with Voodoo", "I expected something different.", "Todo!!!", "This is supposed to crash", "No changes after this point.", "I know, I know, this is not how I’m supposed to do it, but I can't think of something better.", "Don’t even try to refactor it.", "(c) Microsoft 1988", "Please no changes this time.", "Why The Fuck?", "We should delete this crap before shipping.", "Shit code!", "ALL SORTS OF THINGS", "Herpderp, shoulda check if it does really compile.", "I CAN HAZ PYTHON, I CAN HAZ INDENTS", "XNAMEX rebase plx?", "Major fixup.", "less french words", "breathe, =, breathe", "IEize", "this doesn't really make things faster, but I tried", "this should fix it", "forgot to save that file", "Glue. Match sticks. Paper. Build script!", "Argh! About to give up :(", "Blaming regex.", "oops", "it's friday", "yo recipes", "Not sure why", "lol digg", "grrrr", "For real, this time.", "Feed. You. Stuff. No time.", "I don't give a damn 'bout my reputation", "DEAL WITH IT", "commit", "tunning", "I really should've committed this when I finished it...", "It's getting hard to keep up with the crap I've trashed", "I honestly wish I could remember what was going on here...", "I must enjoy torturing myself", "For the sake of my sanity, just ignore this...", "That last commit message about silly mistakes pales in comparision to this one", "My bad", "Still can't get this right...", "Nitpicking about alphabetizing methods, minor OCD thing", "Committing fixes in the dark, seriously, who killed my power!?", "You can't see it, but I'm making a very angry face right now", "Fix the fixes", "It's secret!", "Commit committed....", "No time to commit.. My people need me!", "Something fixed", "I'm hungry", "asdfasdfasdfasdfasdfasdfadsf", "hmmm", "formatted all", "Replace all whitespaces with tabs.", "s/    /  /g", "I'm too foo for this bar", "Things went wrong...", "??! what the ...", "This solves it.", "Working on tests (haha)", "fixed conflicts (LOL merge -s ours; push -f)", "last minute fixes.", "fuckup.", 'Revert "fuckup".', "should work now.", "final commit.", "done. going to bed now.", "buenas those-things.", "Your commit is writing checks your merge can't cash.", "This branch is so dirty, even your mom can't clean it.", "wip", 'Revert "just testing, remember to revert"', "bla", "harharhar", "restored deleted entities just to be sure", "added some filthy stuff", "bugger", "lol", "oopsie B|", "Copy pasta fail. still had a instead of a", "Now added delete for real", "grmbl", "move your body every every body", "Trying to fake a conflict", "And a commit that I don't know the reason of...", "ffs", "that's all folks", "Fucking submodule bull shit", "apparently i did something…", "bump to 0.0.3-dev:wq", "pep8 - cause I fell like doing a barrel roll", "pep8 fixer", "it is hump day _^_", "happy monday _ bleh _", "after of this commit remember do a git reset hard", "someday I gonna kill someone for this shit...", "magic, have no clue but it works", "I am sorry", "dirty hack, have a better idea ?", "Code was clean until manager requested to fuck it up", " - Temporary commit.", ":(:(", "...", "GIT :/", "stopped caring 10 commits ago", "Testing in progress ;)", "Fixed Bug", "Fixed errors", "Push poorly written test can down the road another ten years", "commented out failing tests", "I'm human", "TODO: write meaningful commit message", "Pig", "SOAP is a piece of shit", "did everything", "project lead is allergic to changes...", "making this thing actually usable.", "LAST time, XNAMEX, /dev/urandom IS NOT a variable name generator...", "I was told to leave it alone, but I have this thing called OCD, you see", "Whatever will be, will be 8{", "It's 2015; why are we using ColdFusion?!", "#GrammarNazi", "Future self, please forgive me and don't hit me with the baseball bat again!", "Hide those navs, boi!", "Who knows...", "Who knows WTF?!", "I should get a raise for this.", "Done, to whoever merges this, good luck.", "Not one conflict, today was a good day.", "First Blood", "Fixed the fuck out of #526!", "I'm too old for this shit!", "One little whitespace gets its very own commit! Oh, life is so erratic!"]  # fmt: skip


@loader.tds
class GitPusherMod(loader.Module):
    """Easily push your repo from within the Telegram"""

    strings = {
        "name": "GitPusher",
        "bad_dir": "🚫 <b>Invalid directory</b>",
        "no_dir": "🚫 <b>Specify directory with </b><code>.setghdir</code>",
        "dir_set": "🌳 <b>Updated git directory to</b> <code>{}</code>",
        "terminal_required": "🚫 <b>Terminal module is required</b>",
    }

    strings_ru = {
        "bad_dir": "🚫 <b>Неверная директория</b>",
        "no_dir": "🚫 <b>Укажи директорию используя </b><code>.setghdir</code>",
        "dir_set": "🌳 <b>Директория обновлена на</b> <code>{}</code>",
        "terminal_required": "🚫 <b>Необходими модуль Terminal</b>",
        "_cmd_doc_setghdir": "<path> - Установить директорию в качестве основной",
        "_cmd_doc_push": "[commit message] - Закоммитить установленную директорию",
        "_cls_doc": "Быстро коммить изменения в директории не выходя из Телеграм",
    }

    async def client_ready(self, client, db):
        self._db = db

    async def setghdircmd(self, message: Message):
        """<path> - Set directory as upstream"""
        args = utils.get_args_raw(message)
        if not args or not os.path.isdir(args.strip()):
            await utils.answer(message, self.strings("bad_dir"))
            return

        self.set("dir", args)
        await utils.answer(message, self.strings("dir_set").format(args))

    async def pushcmd(self, message: Message):
        """[commit message] - Push current upstream directory"""
        if not self.get("dir"):
            await utils.answer(message, self.strings("no_dir"))
            return

        if "terminal" not in self.allmodules.commands:
            await utils.answer(message, self.strings("terminal_required"))
            return

        args = (utils.get_args_raw(message) or choice(commits)).replace('"', '\\"')

        message = await utils.answer(
            message,
            f"<code>.terminal cd {utils.escape_html(self.get('dir'))} && git commit -am \"{utils.escape_html(args)}\" && git push</code>",
        )

        await self.allmodules.commands["terminal"](message)
