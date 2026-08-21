# JACOB YE · SEEDANCE PROMPT 1.0

**A director-first cinematic prompt framework for Seedance 2.5 (即梦) AI video generation.**

> Most AI video prompts describe what a scene looks like.
> This framework describes what the camera is doing, what the light is doing,
> what the environment is doing, what the actor is feeling, what the audience is hearing —
> and what must stay consistent between shots.
>
> **Make AI video feel photographed, not generated.**

由 Jacob Ye 在 Seedance 2.0 时代自研的 FILM FORMULA V2.0，与字节跳动 Seedance 2.5 官方提示词手册（2026-07-31）全量合并而成，并经过两个完整成片项目实战验证：一支 30 秒粤语咖啡广告、一部 85 秒三段式粤语悲剧短片《雨夜》。

---

## 核心公式

```
CINEMATIC AI SHOT (2.5) =
  参考绑定（WORLD/ACTOR 分离 + 职责声明 + 排除声明）
  + LENS（一窗一焦段） + 构图 + 运镜（一窗一运镜）
  + LIGHT（光源 → 光行为 → 色调 三层）
  + 呼吸感（环境微动 + 人物微动 + 镜头微动 + 声音微动）
  + 微表演 + 潜台词（情绪分析）
  + 声音标记 ( )音乐 < >音效 { }台词 + 语言声明
  + 结束状态（每拍必写）
  + CONTINUITY 锁定
  + 双层 ANTI-AI 禁令（全局 + 场景专属）

约束：每窗 ≥3 秒 ｜ 一窗一个核心动作 + 一个运镜 ｜ 时长/比例在生成页面设置
```

```
BREATHING FEEL = 环境微动 + 人物微动 + 镜头微动 + 声音微动
```

## 十问（动笔前回答）

WORLD 场景是什么 · ACTOR 谁在里面 · CAMERA 摄影机在做什么 · LIGHT 光从哪来 · MOTION 什么在动 · PERFORMANCE 演员只做什么 · EMOTION 观众该感觉什么 · CONTINUITY 上一镜什么不能变 · ANTI-AI 什么绝对不能出现 · **SOUND 观众听到什么**

## 仓库导航

| 文件 | 内容 |
|---|---|
| [FORMULA.md](FORMULA.md) | 完整框架（V3.0）：参考编排 / 双轨时间结构 / 摄影系统 / 呼吸感 / 表演 / 声音 / 一致性 / Anti-AI / 分镜板 / 长度控制 |
| [SKILL.md](SKILL.md) | Claude Code Skill 入口——装进 `~/.claude/skills/`，说一句话产出导演级提示词 |
| [docs/material-discipline.md](docs/material-discipline.md) | ⚠️ **素材纪律：转场/换段时该删哪些图**（乱入事故的头号预防） |
| [docs/voice-continuity.md](docs/voice-continuity.md) | ⚠️ **语音连贯性 SOP**：跨段保持同一角色声音（TTS/音色锚点） |
| [docs/repair-sop.md](docs/repair-sop.md) | 补镜与修复 SOP：延长上限、60 秒天花板、剪一段再延长（踩坑实录） |
| [docs/post-production.md](docs/post-production.md) | 剪映后期去 AI 感：颗粒/暗角/调色/导出参数 |
| 案例一《咖啡计划》 | 30 秒粤语咖啡广告（单次直出）：[剧本](examples/coffee-plan/story.md) · [提示词](examples/coffee-plan/prompts.md) |
| 案例二《雨夜》 | 85 秒三段式悲剧短片：[剧本](examples/rainy-night/story.md) · [第一段](examples/rainy-night/segment-1-prompt.md) · [第二段+补镜](examples/rainy-night/segment-2-prompt.md) · [第三段](examples/rainy-night/segment-3-prompt.md) · [参考图](examples/rainy-night/image-prompts.md) |
| [CHANGELOG.md](CHANGELOG.md) | 版本历史 |

## 快速上手

1. **读 [FORMULA.md](FORMULA.md) 的"最终组装模板"**——一条 2.5 提示词的完整骨架
2. **照抄一个 example**——两个案例的提示词都是实测跑通的成品，改主体就能用
3. **每次换场景/新段生成前，过一遍 [material-discipline.md](docs/material-discipline.md) 的删图清单**
4. **角色有台词的**：延长段自动继承音色（加一句延续声明即可）；**独立新生成的段落必须先按 [voice-continuity.md](docs/voice-continuity.md) 剪音色锚点并绑定**
5. 想让 Claude 自动干这些：把整个仓库放进 `~/.claude/skills/jacob-seedance/`，对 Claude 说一句剧情即可

## 实战验证记录

| 项目 | 形态 | 验证的能力 |
|---|---|---|
| 《咖啡计划》 | 30s 单次直出，粤语台词 | 官方架构组装、色彩弧线、双角色一致性、声音标记语法 |
| 《雨夜》第一段 | 30s 直出 | 情绪五级台阶（怒忍崩泣释）、眼泪秒表门控、道具戏（伞） |
| 《雨夜》第二段 | 30s 延长 | B-roll 开场块、倒影转场、延长衔接、出租车素材绑定 |
| 《雨夜》补镜 | 裁剪+9s 延长 | 60s 天花板绕行、"延长是接着拍不是重拍"原理 |
| 《雨夜》第三段 | 30s 独立新生成 | 30 秒一镜到底怼脸哭戏、六道防线、音色锚点跨段锁声、手机门控 |

## 致谢与来源

- 字节跳动 Seedance 2.5 官方用户手册与提示词指南（2026-07-31）
- Seedance 2.5 production reference by Serge Shima — [smixs/visual-skills](https://github.com/smixs/visual-skills)（CC BY 4.0）
- [MapleShaw/seedance2.0-prompt-skill](https://github.com/MapleShaw/seedance2.0-prompt-skill) 的相机四维编码与合规红线经验
- Jacob Ye 的 FILM FORMULA V2.0（与 GPT 共研的 2.0 时代原型）

## License

[CC BY 4.0](LICENSE) — 转载与二创请注明出处。

*JACOB YE · SEEDANCE PROMPT 1.0 · 2026-08*
