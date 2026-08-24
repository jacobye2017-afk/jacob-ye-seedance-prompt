# JACOB YE · SEEDANCE PROMPT

**English** | [简体中文](README_zh.md)

[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Built for Seedance 2.5](https://img.shields.io/badge/built%20for-Seedance%202.5%20(Jimeng)-blueviolet)](https://jimeng.jianying.com/)
[![GitHub last commit](https://img.shields.io/github/last-commit/jacobye2017-afk/jacob-ye-seedance-prompt)](https://github.com/jacobye2017-afk/jacob-ye-seedance-prompt/commits/master)
[![Stars](https://img.shields.io/github/stars/jacobye2017-afk/jacob-ye-seedance-prompt?style=social)](https://github.com/jacobye2017-afk/jacob-ye-seedance-prompt/stargazers)

**A director-first cinematic prompt framework for Seedance 2.5 (ByteDance's Jimeng AI video model).**

> Most AI video prompts describe what a scene *looks like*.
> This framework describes what the camera is doing, what the light is doing, what the environment is doing,
> what the actor is feeling, what the audience is hearing — and what must stay consistent between shots.
>
> **Make AI video feel photographed, not generated.**

Originally authored by Jacob Ye as FILM FORMULA V2.0 during the Seedance 2.0 era, fully merged with ByteDance's official Seedance 2.5 prompt guide (2026-07-31), and battle-tested across **two finished short films**: a 30-second Cantonese coffee-shop ad and a ~6-minute three-act Cantonese tearjerker. **Every rule in this repository was paid for in generation credits, not theorized in advance.**

---

## The problem this solves

Write "cinematic, 4K, dramatic lighting" and hand it to a video model, and you get generic AI slop: symmetric fake-looking faces, overacted emotion, props that appear out of nowhere, shots that ask the model to fit something impossible into the frame.

This is not a keyword list. It's an **executable directing method**: every shot is decomposed into focal length / framing / camera move / three-layer lighting / muscle-level emotion chains / subtext / a bounded end-state — so the model has no room to freelance.

**A real before/after** (from the finished *Coffee Plan* short — this exact prompt shipped):

<table>
<tr><td width="50%" valign="top">

**❌ The common way**

```
He gently hands her an umbrella,
a moment of tension, cinematic, 8K
```

Whatever the model does with this is pure chance.

</td><td width="50%" valign="top">

**✅ This framework's way**

```
The glass door opens; he steps out, one hand holding a
steaming latte, the other a clear long-handled umbrella,
camera pushes slowly to a medium close two-shot; he says
in warm, natural Cantonese: {Don't catch a cold, take the
umbrella.} Their fingertips brush during the handoff.
Subtext: his tone is casual, but the handle is already
dry — the preparation gives away how much he cares.
End state: she now holds both the coffee and the umbrella,
their eyes meet.
```

Framing, action, dialogue, subtext, and end-state are all pinned down.

</td></tr>
</table>

The difference isn't length. It's that **the model no longer has to guess.**

---

## Core formula

```
CINEMATIC AI SHOT (2.5) =
  Reference binding (WORLD/ACTOR separation + role declaration + exclusion clause)
  + LENS (one focal length per shot) + composition + camera move (one move per shot)
  + LIGHT (source → behavior → grade, three layers)
  + Breathing feel (environment + character + camera + sound micro-motion)
  + Micro-performance (muscle chain + amplitude constraint) + subtext (emotional analysis)
  + Audio markers ( )music < >sfx { }dialogue + language declaration
  + End state (mandatory per beat, bounded by the stated framing)
  + Continuity locks
  + Two-tier anti-AI bans (global + scene-specific)

Constraints: each beat ≥3s | one core action + one camera move per beat | duration/aspect ratio set on the generation page, not in the prompt
```

```
BREATHING FEEL = environment micro-motion + character micro-motion + camera micro-motion + sound micro-motion
```

## Ten questions to answer before writing a single beat

WORLD (what's the setting) · ACTOR (who's in it) · CAMERA (what is it doing) · LIGHT (where's it from) · MOTION (what's moving) · PERFORMANCE (what does the actor *only* do) · EMOTION (what should the audience feel) · CONTINUITY (what must not change from the last shot) · ANTI-AI (what must never appear) · **SOUND (what does the audience hear)**

---

## What's inside FORMULA.md (22 chapters)

| § | Topic |
|---|---|
| 0 | Ten-question philosophy + core formula |
| 1 | Reference material orchestration — binding/exclusion syntax for the 50-slot system |
| 2 | Time structure — dual-track model, per-beat end states, extension & repair |
| 3–4 | Cinematography system + four-part breathing feel |
| 5–6 | Performance system + sound system (a module the official guide is missing) |
| 7–8 | Continuity Bible + two-tier anti-AI bans |
| 9–11 | Storyboard-grid generator · length control · genre presets |
| 12 | **Final assembly template** — every prompt in this repo follows this skeleton |
| 14 | **Master-grade cinematic commandments** (12 rules distilled from frame-by-frame review) |
| 15 | Pillow-shot module — B-roll semantic library + camera-move emotion mapping |
| 16 | Lens psychology matrix (validation in progress from live production) |
| 17 | **Facial muscle system** (FACS-lite) — describe muscles, not adjectives |
| 18 | **Frame feasibility & prompt-engineering discipline** — where things break most; 12 sub-rules, every one traced to a real failure |
| 19 | Dialogue engineering — multilingual/dialect rules, syllable-rate budget, per-line declaration syntax |
| 20 | B-roll location-identity anchoring |
| 21 | Character-sheet production & platform compliance — what format actually passes review |
| 22 | Entry discipline & shot-ratio law |

## Repo map

| File | What's in it |
|---|---|
| [FORMULA.md](FORMULA.md) | The full framework — see table above |
| [SKILL.md](SKILL.md) | Claude Code Skill entry point — drop into `~/.claude/skills/`, describe a scene, get a director-grade prompt |
| [AGENTS.md](AGENTS.md) | **Usage guide for any AI agent** (Codex, Cursor, Gemini CLI, etc.): read order, workflow, pre-delivery checklist |
| [docs/cinematic-techniques.md](docs/cinematic-techniques.md) | ⭐ **11 cinematic techniques, quick reference** — start here |
| [docs/material-discipline.md](docs/material-discipline.md) | ⚠️ Which reference images to drop between segments (the #1 cause of unwanted intrusions) |
| [docs/voice-continuity.md](docs/voice-continuity.md) | ⚠️ Keeping the same character voice across independent generations (voice-anchor SOP) |
| [docs/repair-sop.md](docs/repair-sop.md) | Repair playbook: extension-chain ceiling, "extend continues, it doesn't redo" |
| [docs/post-production.md](docs/post-production.md) | De-AI-ifying in post: grain, vignette, grading, export settings |
| Example 1 — *Coffee Plan* | 30s Cantonese ad: [story](examples/coffee-plan/story.md) · [prompts](examples/coffee-plan/prompts.md) |
| Example 2 — *Rainy Night* | 85s three-act tragedy: [story](examples/rainy-night/story.md) · [segment 1](examples/rainy-night/segment-1-prompt.md) · [segment 2 + repair](examples/rainy-night/segment-2-prompt.md) · [segment 3](examples/rainy-night/segment-3-prompt.md) · [image prompts](examples/rainy-night/image-prompts.md) · [post-mortem review](examples/rainy-night/review.md) |
| [CHANGELOG.md](CHANGELOG.md) | Version history — every entry traces back to a specific production failure |

## Quick start

1. **Read [FORMULA.md §12](FORMULA.md)**, the final assembly template — the complete skeleton of one 2.5 prompt
2. **Copy an example verbatim** — both case studies are production-tested and generation-verified; swap the subject and go
3. **Before every new segment, run the delete-checklist in [material-discipline.md](docs/material-discipline.md)**
4. **Characters with dialogue**: an *extended* segment inherits voice automatically (one continuation line is enough); a segment generated *independently* needs a cut voice anchor per [voice-continuity.md](docs/voice-continuity.md)
5. Want an AI to do all of this for you? Drop the whole repo into `~/.claude/skills/jacob-seedance/`, or clone it and let any file-reading agent take over

## Using this with any AI agent

The repo is plain Markdown — any agent that can read files can use it.

```bash
git clone https://github.com/jacobye2017-afk/jacob-ye-seedance-prompt.git
cd jacob-ye-seedance-prompt
```

| Agent | How |
|---|---|
| **Codex CLI** | Launch inside the repo — it auto-reads [AGENTS.md](AGENTS.md); just say "write me a 30s rainy-night argument scene" |
| **Cursor / Windsurf** | Open the repo as a workspace, point it at AGENTS.md and FORMULA.md first |
| **Claude Code** | Copy into `~/.claude/skills/jacob-seedance/`, or chat directly inside the repo |
| **Gemini CLI / others** | Have the agent read AGENTS.md first, then proceed normally |

No tooling? Paste the §12 assembly template and §14 commandments from [FORMULA.md](FORMULA.md) into any chat window — it works standalone.

## Battle-tested track record

| Project | Format | Capability proven |
|---|---|---|
| *Coffee Plan* | 30s single-shot, Cantonese dialogue | Official 2.5 architecture assembly, color-arc contract, two-character consistency, audio-marker syntax |
| *Rainy Night*, segment 1 | 30s single-shot | Five-stage emotional escalation, tear-timing gates, prop-driven subplot (the umbrella) |
| *Rainy Night*, segment 2 | 30s extension | B-roll cold-open block, reflection transition, extension continuity, taxi-asset binding |
| *Rainy Night*, repair pass | Trim + 9s extension | Working around the 60s extension-chain ceiling; "extend continues, it doesn't redo" |
| *Rainy Night*, segment 3 | 30s standalone, one continuous take | Face-to-camera crying in one unbroken shot, six-stage emotional collapse, cross-segment voice anchoring, phone-prop gating |
| *After the Rain*, full film | ~6-minute Cantonese short | Dual-card role/appearance splitting, "card locks form, text locks state," positively-specified extras density, per-line dialogue engineering, overhead framing for liquid physics, bans paired with a mutually-exclusive positive state |

## Why not just a prompt list

| | Generic prompt collections | Asking ChatGPT/Claude directly | This framework |
|---|---|---|---|
| Frame-feasibility checks | ❌ | ❌ (routinely asks for a phone visible inside a face close-up) | ✅ §18, 12 sub-rules |
| Emotion → muscle-level action library | ❌ | Occasionally | ✅ §17, with an amplitude constraint against overacting |
| Dialect TTS syllable-rate budget | ❌ | ❌ | ✅ §19, ~3 syllables/sec |
| Platform review-compliant formats | ❌ | ❌ | ✅ §21, with a researched review-policy timeline |
| Every rule traceable to a real failure | ❌ | — | ✅ see [CHANGELOG.md](CHANGELOG.md) |
| Complete, generation-verified film case studies | Rare | ❌ | ✅ two, prompts fully open-sourced |

## Roadmap

- [ ] §16 lens psychology matrix — full index of focal length × height × angle × framing → psychological effect (validating against live production now)
- [ ] Dialect-engineering rules for more languages (currently: Hong Kong Cantonese)
- [ ] A third open-sourced film case study

Found a new failure mode and already worked out the fix? PRs welcome — this repo **grows from real production failures**; every rule here is a lesson someone already paid for.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=jacobye2017-afk/jacob-ye-seedance-prompt&type=Date)](https://star-history.com/#jacobye2017-afk/jacob-ye-seedance-prompt&Date)

## FAQ

**Does this work with Seedance 2.0?**
Partially. §3–9 and §14–17 (cinematography, breathing feel, performance, sound, the commandments, pillow shots, the muscle system) are general filmmaking method — they apply regardless of engine. §1 (the 50-slot binding syntax), §2 (30s single-pass + extension), and the §12 assembly template are 2.5-specific mechanics — 2.0 caps at 15 seconds, has a simpler binding grammar, and briefly restricted photoreal human references (banned Feb 2026, replaced by a consent-verification gate in April, see §21.1). Use the "directing" layer as-is on 2.0; downgrade the "platform syntax" layer to 2.0's actual limits.

**I don't read Chinese — can I still use this?**
The output prompts are written in Chinese because that's Jimeng's input language — you paste them in directly, no translation needed to use them. The deeper documentation is currently Chinese-only but cleanly structured; feed it to any translator, or hand the whole repo to an AI agent (see the table above) and have it operate the workflow for you.

**Is this an official ByteDance project?**
No. This is an independent developer's practical extension and merge of the official prompt guide, for educational/reference use. No affiliation with ByteDance.

**Can I use the example characters/scripts commercially?**
The prompts in the examples are original creative work — copy and adapt them freely for your own projects. Final licensing/compliance on generated output is governed by Jimeng's own platform terms.

**Why build rules from real failures instead of documenting theoretical best practices?**
Because theoretical best practice often doesn't survive contact with a video model — it will satisfy a "reasonable-looking" framing requirement in a way you didn't expect. Every rule in this repo was paid for in credits first, then written down. That's what makes it trustworthy.

## Acknowledgments & sources

- ByteDance's official Seedance 2.5 user guide and prompt guide (2026-07-31)
- The Seedance 2.5 production reference by Serge Shima — [smixs/visual-skills](https://github.com/smixs/visual-skills) (CC BY 4.0)
- [MapleShaw/seedance2.0-prompt-skill](https://github.com/MapleShaw/seedance2.0-prompt-skill) for the four-axis camera codec and compliance red lines
- Jacob Ye's FILM FORMULA V2.0 (co-developed with GPT during the 2.0 era)

## Contributing

Found a new way this breaks, and already have a fix that works? Open a PR. Follow the existing [CHANGELOG.md](CHANGELOG.md) format — **problem → root cause → rule → example** — and cite the chapter number. Untested theory-only suggestions: open an Issue and let's discuss first.

## License

[CC BY 4.0](LICENSE) — please credit on reuse or derivative work. See [NOTICE](NOTICE) for attribution and incorporated sources.

---

**If this framework saved you a few hundred generation credits, a ⭐ is the best thank-you.**

*JACOB YE · SEEDANCE PROMPT · August 2026*
