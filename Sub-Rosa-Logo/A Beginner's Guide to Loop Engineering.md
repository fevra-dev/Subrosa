
Fable 5: A Beginner's Guide to Loop Engineering 
AI Edge
@aiedge_
·
Jul 3

Loop engineering is the biggest shift in AI prompting we've ever seen.
Pair it with Fable 5, and you'll have AI agents working for you while you sleep, building anything you could think of.
This guide teaches you exactly how to get started.
A layman's guide to loop engineering & how the average person can take advantage of /loop. 
Contents 
wtf is a Loop?
Loop Anatomy 101
Prompting 101
/loop Pro Tips 
wtf is a Loop?
TL;DR
Loop engineering is essentially a way for agents to prompt themselves and avoid manual iterations.
Before loop engineering: You prompt AI → It responds → You iterate → Repeat
With loop engineering: You design a loop → Agent comes back with a finalized result (agent completes all the research, back-and-forth, etc.)
The person who actually built Claude Code (Boris Cherny) put it plainly: 
"I don't prompt Claude anymore. I have loops running that prompt Claude. My job is just to write loops." 
This is the single biggest shift in prompting AI we've ever seen.
For now, that's all you need to know. What's more important is loop anatomy and how to actually take advantage of this shift to unlock AI productivity. 
Loop Anatomy 101
Loop Anatomy 101
For this guide, I'll reference Claude Code, but these principles apply to most AI tools and frameworks.  
Every loop in Claude Code has the same six working parts.  
Master these, and you'll be able to build anything.
1. Trigger (Automations)
The trigger is what starts the loop.
In Claude Code, you trigger agentic loop automations with /schedule and /loop (more on prompting later).
/loop runs on a specified interval; without an interval, it self-paces based on output. 
2. Execution Layer 
This is where Claude actually does the work. 
It reads the current state, takes action, and produces outputs.
No manual input is needed - just watch Claude work. 
3. The Verifier
This is where you give Claude a checkpoint.
Things like: Tests, a build, a screenshot to compare. 
Using a verification layer helps ensure Claude is actually on the right track and not producing slop.
You can use the /goal command, which takes things a step further by running a separate fast model to grade the work after every turn.
4. Stop Rules
Every loop needs two types of stop conditions: 
Success stopping (all tests pass, task complete)  
Failure stopping (retry count exceeded, unrecoverable error). 
You can also add stop rules, such as a token budget, which can help manage AI spend.
Make these explicit in your instructions, not implicit:
You have a maximum of 20 attempts. If all tests pass, report "TASK_COMPLETE" and stop. 
If you encounter an error you cannot resolve after 3 retries, report "TASK_FAILED: [reason]" and stop.
5. Memory (Progress File)
Keeping a markdown file of Claude's progress is generally good practice.
A simple log of what's been done so you can check its work and go back if needed.
6. Skills (CLAUDE.md)
Skills are saved instruction sets that freeze project knowledge so the agent doesn't re-learn the same context every session. 
Your CLAUDE.md file is what gives the loop its personality and sets its constraints for every run. 
Tip: Keep it short. A bloated rules file gets paid for on every single beat of the loop. 
Put all six together, and the optimal loop structure looks like this:
TRIGGER   →  every 15min / on PR comment / on CI failure
DOER      →  Claude works the task
CHECKER   →  separate model grades the output
STOP      →  all tests green, or 10 iterations, or $5 spent
MEMORY    →  progress.md updated each run
SKILLS    →  CLAUDE.md read on every session start
Prompting 101 (putting things together)
Writing /loop prompts are not the same as regular prompting. You need a slight mental shift when loop engineering.
When you prompt Claude normally, you're simply writing an instruction/task. 
When you're designing a loop, you're writing a final condition that must be met.
Example 
Prompt (single turn):
Fix the failing tests in the auth module.
Goal condition (loop):
/loop all tests in the auth module pass and coverage is above 80%
A prompt tells Claude what to do, while a goal condition tells Claude when to stop. 
The anatomy of a good goal condition
Every strong /loop prompt has three things:
A verifiable end state
A scope constraint (what files, what folders, what tasks)
A stop rule (max iterations or budget)
Here's the template:
/loop [verifiable end state/time], only touching [scope], stop after [X] constraints, use [X] Skills, use verifier agents for [x] checkpoint, and keep a memory file of all your work.
This is the base /loop structure that every beginner should use to get great results without overcomplicating things. 
CLAUDE.md 
Think of your CLAUDE.md as the briefing document your loop reads before it starts every a run. 
Be sure to include everything you'd normally repeat in a prompt, your stack, your rules, your preferences, etc.
Again, keep it short. Every extra line of bloated context costs tokens.
Putting everything together (an example research brief /loop):
CLAUDE.md (set once):
Research style: comprehensive, cited, no fluff
Output format: markdown with clear headers
Never create files outside /research
Preferred sources: primary sources, reputable publications, official data
Max budget per session: $3
Skill (set once):
/skill verify-research: before marking any section complete, confirm 
every major claim has a source, every section has at least 3 supporting 
data points, and there are no obvious gaps. Never hand back thin research.
The loop:
/loop every 30 minutes,

only touching /research/brief.md,

stop after 10 iterations or if the same search query appears 
3 times in a row without new information surfacing,

use the verify-research skill after each section is drafted,

use a verifier agent to check source quality and coverage 
completeness at the halfway point and before final submission,

and keep a memory file at /research/progress.md that logs 
what sections are done, what sources have been used, 
and what angles still need coverage — read it at the start 
of every run and update it at the end.

Topic: [your topic here]

Every principle in one place. The loop runs on a timer, stays scoped to one file, stops itself on stall or budget, uses a saved skill as the quality gate, spins up a separate verifier at two checkpoints, and keeps a persistent memory file so each run picks up exactly where the last one stopped.
/loop Pro Tips
A section of /loop pro tips to get you started 
Start with /goal before /loop: It's the same behavior, but easier to reason about as a beginner. 
Spend more time on the deliverable: When designing loops, focus on what you want the end goal to look like - everything else is pretty much noise.
Match the effort level to the task: Your default reasoning effort should be high. Only use xHigh, Max & Ultracode for complex builds. 
Subagents: Each subagent starts with a fresh context window. Take advantage of deploying subagents within loops. 
Always cap: Make it a habit to set a hard iteration limit and a dollar budget before every run. 
Run /compact manually before long sessions: When the context window approaches its limit, the SDK automatically compacts. You can also trigger it early with /compact.
Loops work for way more than code: You can use /loop for all tasks. Feel free to be creative and use loops for writing, research, and unconventional non-coding tasks. 
Closing 
I hope you've found this /loop guide valuable.
If you did, be sure to follow me @aiedge_ - I post AI articles just like this one 2-3x/week.
If you enjoy written AI content, feel free to subscribe to my free newsletter here:
https://newsletter.aiedgehq.co/
https://newsletter.aiedgehq.co/
100% free, no spam ever & unsub anytime.
Lastly, if you can, please follow my new clips account where I post short clips discussing trending AI/market topics - I'm sure you'll get a lot of value💙
Miles Ahead
@DeutscherClips
·
Jul 3
Miles Deutscher explains why AI video is the next million-dollar money-making opportunity for 16-25 y/os.

It will completely change content and Hollywood as we know it.


Want to publish your own Article?
Upgrade to Premium
Show 6 replies
AI Edge
@aiedge_
AI Edge by 
@milesdeutscher
 ⚡ | Giving you the edge on AI. Breaking news • Practical guides • Smart insights • Tips & more | Your go-to hub for everything AI.