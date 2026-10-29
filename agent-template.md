---
# ============================================================================
# AGENT TEMPLATE
# 1. Copy this file to `.claude/agents/<agent-name>.md`.
# 2. Replace every <placeholder> and adapt or delete any section.
# 3. Delete the comments when you are done. They cost context every time the
#    agent runs.
#
# What makes a good agent:
# - ONE role with a clear job. If you need "and" twice to describe it, split it.
# - Keep it short. A focused page beats five pages of rules the agent will
#   half-follow.
# ============================================================================

# name: Lowercase, hyphenated, unique. Name the role, not the task:
# `pricer`, `deck-critic`, `buyer-analyst`.
name: <agent-name>

# description: The most important line. The orchestrator reads it to decide
# WHEN to call this agent. Say what it does and when to use it
# ("Use when ..."). Be specific.
description: <What the agent does in one sentence>. Use when <situation 1> or <situation 2>.

# tools: Optional. Leave out to inherit every tool. List only what the role
# needs: a critic that only reads should not have Write.
tools: Read, Write, Grep, Glob

# model: Optional. `haiku`, `sonnet`, `opus` or `inherit`. Cheap models suit
# narrow, repetitive jobs; hard judgement calls deserve a stronger model.
model: sonnet
---

# <Agent title>

<!--
  Who the agent is and what its job is, in two or three sentences.
  It starts with no memory of your conversation. Everything it needs must be
  in this prompt, in the files it reads, or in the message it is called with,
  so give it the context of the game here.
-->

You are the <role> on a team <what the team does>. Your job is to <the one job>.

## Inputs

<!--
  Clear inputs. Say exactly what it receives and where it finds it
  (file paths, API calls, the calling message).
-->

- <Input 1, and where to find it>
- <Input 2, and where to find it>
- <Earlier work it should build on, e.g. existing notes in `work/...`>

## What to do

<!--
  Numbered steps. Ask it to state beliefs with evidence:
  "Buyer cares about speed (high confidence: bio says 'we ship weekly',
  reply 2 complained about the timeline)" beats "buyer likes speed".
  If a skill covers part of the job, tell the agent to use it here.
-->

1. <First step>
2. <Second step>
3. <Third step>

## Output

<!--
  Clear output. Say exactly what it hands back, ideally in a fixed format the
  next agent can read. Define "done", so it knows when to stop.
-->

Return <what it returns>, in this format:

```
<Field 1>: <value>
<Field 2>: <value>
Open questions: <what is still unknown>
```

## Rules

<!--
  Boundaries and edge cases. Say what is NOT its job (so it does not drift
  into another agent's work) and what to do when information is missing.
-->

- Do not <task that belongs to another agent>. That is another agent's job.
- If an input is missing, say so in the output. Do not guess silently.
- <Any other rule specific to this role>
