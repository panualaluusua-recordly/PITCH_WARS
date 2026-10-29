---
# ============================================================================
# SKILL TEMPLATE
# 1. Copy this file to `.claude/skills/<skill-name>/SKILL.md`.
#    The folder can also hold supporting files (examples, checklists, scripts)
#    that the instructions below point to.
# 2. Replace every <placeholder> and adapt or delete any section.
# 3. Delete the comments when you are done. They cost context every time the
#    skill loads.
#
# Agent or skill?
# - An agent is a WHO: a role with its own context that does a job and reports back.
# - A skill is a HOW: a reusable procedure any agent (or you) loads when needed.
#   One agent can have several skills; several agents can share one skill.
# ============================================================================

# name: Lowercase, hyphenated, matches the folder name.
name: <skill-name>

# description: The most important line. Claude reads only this to decide
# whether to load the skill, so say what it does AND when to use it
# ("Use when ..."). Name the situations and words that should trigger it.
description: <What the skill does in one sentence>. Use when <situation 1>, <situation 2> or when <trigger words appear>.

# allowed-tools: Optional. Tools the skill may use without asking.
# Delete the line to use the normal permission rules.
allowed-tools: Read, Grep
---

# <Skill title>

<!--
  One or two sentences: what this skill is for and what it produces.
  A good skill does one repeatable thing well, the same way every time.
-->

Use this to <goal of the skill>.

## Inputs

<!--
  What the skill needs before it starts, and where to find it (files, API
  calls, the message it was called with). Say what to do when an input is
  missing or unclear: stop and ask, use a default, or note the gap.
-->

- <Input 1, and where to find it>
- <Input 2, and where to find it>
- If <input> is missing: <what to do instead>

## Steps

<!--
  Steps, not essays. Number them. Each step should be checkable, so you can
  tell whether it was done. If a step needs long reference material, move it
  into a separate file in the skill folder and say when to read it, e.g.
  "Read `reference.md` if the buyer has no stated budget."
-->

1. <First step>
2. <Second step>
3. <Third step>
4. <Final step: produce the output below>

## Output

<!--
  Define the output: format, length, and what must always be included.
  A fixed format makes the result easy to read and easy to pass to the next
  agent or skill.
-->

```
<Field 1>: <value>
<Field 2>: <one line>
Confidence: low | medium | high
Risk: <what could make this wrong>
```

## Example

<!--
  One short worked example. Examples teach faster than rules. Use a real
  case from your game once you have one. For instance, a pricing skill
  might show:

    Price: 42 000
    Reason: Budget is 40-50k; reply 1 said our 55k deck was "out of range".
    Confidence: medium
    Risk: A competitor undercuts at 35k and the buyer weighs price above quality.
-->

```
<Field 1>: <example value>
<Field 2>: <example reason, naming the evidence used>
Confidence: <level>
Risk: <example risk>
```

## Do not

<!--
  What NOT to do. List the mistakes you have seen or expect, e.g.
  "Do not change two things in the same feedback request, or you cannot
  tell which change the buyer reacted to."
-->

- Do not <common mistake 1>.
- Do not <common mistake 2>.
