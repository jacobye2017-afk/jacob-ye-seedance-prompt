# JACOB YE · SEEDANCE PROMPT

[English](README.md) | **简体中文**

[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Built for Seedance 2.5](https://img.shields.io/badge/built%20for-Seedance%202.5%20(即梦)-blueviolet)](https://jimeng.jianying.com/)
[![GitHub last commit](https://img.shields.io/github/last-commit/jacobye2017-afk/jacob-ye-seedance-prompt)](https://github.com/jacobye2017-afk/jacob-ye-seedance-prompt/commits/master)
[![Stars](https://img.shields.io/github/stars/jacobye2017-afk/jacob-ye-seedance-prompt?style=social)](https://github.com/jacobye2017-afk/jacob-ye-seedance-prompt/stargazers)

**一套导演优先的 Seedance 2.5（即梦）电影级提示词框架。**

> 大多数 AI 视频提示词描述"画面看起来是什么样"。
> 这套框架描述**摄影机在做什么、光在做什么、环境在做什么、演员在感觉什么、观众在听什么**——以及镜头之间什么必须保持不变。
>
> **让 AI 视频看起来像被拍出来的，而不是被生成出来的。**

由 Jacob Ye 在 Seedance 2.0 时代自研的 FILM FORMULA V2.0，与字节跳动 Seedance 2.5 官方提示词手册（2026-07-31）全量合并，经过**两部完整成片**实战验证并持续用真实失败反哺规则：一支 30 秒粤语咖啡广告《咖啡计划》、一部近 6 分钟的三段式粤语催泪短片《以后落雨》。**这个仓库的每一条规则，都是用生成积分换来的。**

---

## 这个项目在解决什么问题

写一句"电影感、4K、戏剧性光影"丢给模型，得到的是千篇一律的 AI 感画面——脸对称到假、情绪演到浮夸、道具凭空出现、镜头装不下你要的东西。

这套框架不是关键词大全，是一套**可执行的导演方法论**：把镜头拆成焦段/景别/运镜/光影三层/情绪肌肉链/潜台词/结束状态，逐条钉死，让模型没有"自由发挥"的空间。

**一个真实对比**（来自《咖啡计划》成片，已跑通）：

<table>
<tr><td width="50%" valign="top">

**❌ 常见写法**

```
男主角温柔地把伞递给女主角，
两人有点心动，电影感，8K超清
```

模型会怎么演，完全看运气。

</td><td width="50%" valign="top">

**✅ 本框架写法**

```
玻璃门被推开，阿南走出，一手递上热气腾腾的拿铁，
一手递过一把透明长柄雨伞，镜头缓推至两人中近景，
阿南用自然温和的粤语说：{咪冻亲呀，遮借畀你。}
交接时指尖轻轻碰触。
情绪分析：他语气平常，但伞柄早已擦干——
这份准备暴露了在意。
结束状态：伞与咖啡都到了小夏手中，两人视线交汇。
```

镜头、动作、台词、潜台词、结束状态全部钉死。

</td></tr>
</table>

差别不是"写得更长"，是**模型不再需要猜**。

---

## 核心公式

```
CINEMATIC AI SHOT (2.5) =
  参考绑定（WORLD/ACTOR 分离 + 职责声明 + 排除声明）
  + LENS（一窗一焦段） + 构图 + 运镜（一窗一运镜）
  + LIGHT（光源 → 光行为 → 色调 三层）
  + 呼吸感（环境微动 + 人物微动 + 镜头微动 + 声音微动）
  + 微表演（肌肉链 + 幅度约束） + 潜台词（情绪分析）
  + 声音标记 ( )音乐 < >音效 { }台词 + 语言声明
  + 结束状态（每拍必写，且受画框约束）
  + CONTINUITY 锁定
  + 双层 ANTI-AI 禁令（全局 + 场景专属）

约束：每窗 ≥3 秒 ｜ 一窗一个核心动作 + 一个运镜 ｜ 时长/比例在生成页面设置，不入提示词
```

```
BREATHING FEEL = 环境微动 + 人物微动 + 镜头微动 + 声音微动
```

## 十问（动笔前回答）

WORLD 场景是什么 · ACTOR 谁在里面 · CAMERA 摄影机在做什么 · LIGHT 光从哪来 · MOTION 什么在动 · PERFORMANCE 演员只做什么 · EMOTION 观众该感觉什么 · CONTINUITY 上一镜什么不能变 · ANTI-AI 什么绝对不能出现 · **SOUND 观众听到什么**

---

## FORMULA.md 里有什么（22 章）

| 章节 | 主题 |
|---|---|
| §0 | 哲学十问 + 核心公式 |
| §1 | 参考素材编排——50 槽位系统的绑定与排除声明语法 |
| §2 | 时间结构——双轨制、每拍结束状态、延长与修复 |
| §3–4 | 摄影系统 + 呼吸感四元 |
| §5–6 | 表演系统 + 声音系统（全新模块） |
| §7–8 | 一致性系统 + 双层 Anti-AI 禁令 |
| §9–11 | 分镜板生成器 · 长度控制 · Genre Presets |
| §12 | **最终组装模板**——每条提示词都按这个骨架拼 |
| §14 | **大师级电影感军规**（12 条，成片逐帧评审沉淀） |
| §15 | 枕镜头模块——B-roll 语义库 + 运镜情绪映射 |
| §16 | 镜头心理学矩阵（实测转正中） |
| §17 | **表情肌肉系统**（FACS-lite）——写肌肉，不写形容词 |
| §18 | **画框物理可行性与提示词工程纪律**——最容易翻车的地方，12 条子规则全部来自真实失败 |
| §19 | 台词工程——多语言/方言、语速预算、逐句声明语法 |
| §20 | B-roll 地点身份锚 |
| §21 | 角色卡制作与平台合规——过审格式、场景档案、宫格的正确用途 |
| §22 | 进场纪律与镜头配比 |

## 仓库导航

| 文件 | 内容 |
|---|---|
| [FORMULA.md](FORMULA.md) | 完整框架，见上表 |
| [SKILL.md](SKILL.md) | Claude Code Skill 入口——装进 `~/.claude/skills/`，说一句话产出导演级提示词 |
| [AGENTS.md](AGENTS.md) | **给任何 AI 代理的使用说明**（Codex / Cursor / Gemini CLI 等）：必读顺序、工作流、交付前自检清单 |
| [docs/cinematic-techniques.md](docs/cinematic-techniques.md) | ⭐ **电影感十一条拍摄手法（速查）**——想快速上手先看这份 |
| [docs/material-discipline.md](docs/material-discipline.md) | ⚠️ 素材纪律：转场/换段时该删哪些图（乱入事故的头号预防） |
| [docs/voice-continuity.md](docs/voice-continuity.md) | ⚠️ 语音连贯性 SOP：跨段保持同一角色声音（TTS/音色锚点） |
| [docs/repair-sop.md](docs/repair-sop.md) | 补镜与修复 SOP：延长上限、60 秒天花板、剪一段再延长 |
| [docs/post-production.md](docs/post-production.md) | 剪映后期去 AI 感：颗粒/暗角/调色/导出参数 |
| 案例一《咖啡计划》 | 30 秒粤语咖啡广告：[剧本](examples/coffee-plan/story.md) · [提示词](examples/coffee-plan/prompts.md) |
| 案例二《雨夜》 | 85 秒三段式悲剧短片：[剧本](examples/rainy-night/story.md) · [第一段](examples/rainy-night/segment-1-prompt.md) · [第二段+补镜](examples/rainy-night/segment-2-prompt.md) · [第三段](examples/rainy-night/segment-3-prompt.md) · [参考图](examples/rainy-night/image-prompts.md) · [成片评审复盘](examples/rainy-night/review.md) |
| [CHANGELOG.md](CHANGELOG.md) | 版本历史——每一条都能追溯到一次具体的失败 |

## 快速上手

**制作工作流 2.0 已归档**：[完整流程](docs/workflows/production-workflow-2.0-pilot.md) · [BGM 卡点流程与脚本](docs/workflows/bgm-led-mv.md) · [琉璃光院交付复盘](examples/rurikoin-mv/review.md) · [用户试听确认记录](examples/bgm-beat-check/review.md)。旧版 [1.5 快照](docs/workflows/production-workflow-1.5-legacy.md) 保留。拍点检测与本片交付已验证；下一条 BGM 驱动整片仍需实际验收。

1. **读 [FORMULA.md](FORMULA.md) 第 12 章"最终组装模板"**——一条 2.5 提示词的完整骨架
2. **照抄一个 example**——两个案例的提示词都是实测跑通的成品，改主体就能用
3. **每次换场景/新段生成前，过一遍 [material-discipline.md](docs/material-discipline.md) 的删图清单**
4. **角色有台词的**：延长段自动继承音色（加一句延续声明即可）；**独立新生成的段落必须先按 [voice-continuity.md](docs/voice-continuity.md) 剪音色锚点并绑定**
5. 想让 AI 自动干这些：把整个仓库放进 `~/.claude/skills/jacob-seedance/`，或在任意支持读文件的 AI 代理里 clone 后直接对话

## 在其他 AI 代理里使用

仓库是纯 Markdown，任何能读文件的代理都能用。

```bash
git clone https://github.com/jacobye2017-afk/jacob-ye-seedance-prompt.git
cd jacob-ye-seedance-prompt
```

| 代理 | 用法 |
|---|---|
| **Codex CLI** | 在仓库目录里启动，它会自动读取 [AGENTS.md](AGENTS.md)；直接说"帮我写一段30秒雨夜吵架的提示词" |
| **Cursor / Windsurf** | 打开仓库为工作区，让它先读 AGENTS.md 和 FORMULA.md |
| **Claude Code** | 复制到 `~/.claude/skills/jacob-seedance/`，或在仓库目录里直接对话 |
| **Gemini CLI / 其他** | 让代理先读 AGENTS.md，其余照做 |

不想装工具的话，把 [FORMULA.md](FORMULA.md) 的 §12 组装模板和 §14 军规贴进任意聊天窗口，也能直接用。

## 实战验证记录

| 项目 | 形态 | 验证的能力 |
|---|---|---|
| 《咖啡计划》 | 30s 单次直出，粤语台词 | 官方架构组装、色彩弧线、双角色一致性、声音标记语法 |
| 《雨夜》第一段 | 30s 直出 | 情绪五级台阶（怒忍崩泣释）、眼泪秒表门控、道具戏（伞） |
| 《雨夜》第二段 | 30s 延长 | B-roll 开场块、倒影转场、延长衔接、出租车素材绑定 |
| 《雨夜》补镜 | 裁剪+9s 延长 | 60s 天花板绕行、"延长是接着拍不是重拍"原理 |
| 《雨夜》第三段 | 30s 独立新生成 | 30 秒一镜到底怼脸哭戏、六道防线、音色锚点跨段锁声、手机门控 |
| 《以后落雨》全片 | ~6 分钟粤语微电影 | 双卡分工绑定、卡锁形文字锁态、群演密度正向指定、逐句台词工程、俯拍解决液体物理、禁令换互斥正向状态 |

## 为什么不是随便一份提示词合集

| | 通用提示词合集 | 直接问 ChatGPT/Claude 要提示词 | 本框架 |
|---|---|---|---|
| 画框物理可行性检查 | ❌ | ❌（经常写出"特写里塞进一部手机"这类无解构图） | ✅ §18，12 条子规则 |
| 情绪→肌肉级动作词库 | ❌ | 偶尔 | ✅ §17，含幅度约束防浮夸 |
| 方言 TTS 语速预算 | ❌ | ❌ | ✅ §19，约 3 音节/秒 |
| 平台过审格式规则 | ❌ | ❌ | ✅ §21，含审核时间线考证 |
| 每条规则可追溯到具体失败 | ❌ | — | ✅ 见 [CHANGELOG.md](CHANGELOG.md) |
| 完整可跑通的成片案例 | 很少 | ❌ | ✅ 两部，全部提示词开源 |

## Roadmap

- [ ] §16 镜头心理学矩阵——焦段×高度×方位×景别→心理效果的完整索引表（实测转正进行中）
- [ ] 更多语言/方言的台词工程规则（现有：香港粤语）
- [ ] 第三部成片案例开源

对新失败模式感兴趣？欢迎 Issue/PR——这个仓库**靠真实翻车养大**，一条新规则 = 一次被验证过的教训。

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=jacobye2017-afk/jacob-ye-seedance-prompt&type=Date)](https://star-history.com/#jacobye2017-afk/jacob-ye-seedance-prompt&Date)

## FAQ

**这套框架能用在 Seedance 2.0 上吗？**
部分可以。§3-§9、§14-§17（摄影/呼吸感/表演/声音/军规/枕镜头/肌肉系统）是通用电影方法论，2.0 一样适用。但 §1（50 槽位绑定语法）、§2（30 秒单次直出+延长机制）、§12 的官方组装模板是 2.5 专属语法——2.0 上限 15 秒、绑定语法更简单、且曾有真人素材限制（2026-02 一度禁用，4 月起改为合规校验，见 §21.1）。用在 2.0 上时，把"导演思维"部分保留，"平台语法"部分降级到 2.0 的实际限制即可。

**我不会中文，能用吗？**
提示词是即梦（中文平台）的输入语言，本框架的提示词产出物本来就是中文，直接复制粘贴使用不需要你懂中文。深度文档目前是中文写的，但结构清晰、可以丢给任何 AI 翻译，或者让 [AGENTS.md](AGENTS.md) 里列出的任意 AI 代理直接帮你操作全流程。

**这是字节跳动官方项目吗？**
不是。这是独立开发者对官方提示词手册的实战扩展与合并，仅供学习参考，与字节跳动无隶属关系。

**素材、案例里的角色形象可以商用吗？**
案例中的提示词是原创设计，你可以照抄修改用于自己的项目；但生成结果的最终授权与合规判断请以即梦平台条款为准。

**为什么要用真实失败驱动规则，而不是理论最佳实践？**
因为理论最佳实践在 AI 生成场景里经常不成立——模型会用你想不到的方式满足一个"看起来合理"的构图要求。这个仓库的每一条规则都是先烧了积分才写下来的，可信度更高。

## 致谢与来源

- 字节跳动 Seedance 2.5 官方用户手册与提示词指南（2026-07-31）
- Seedance 2.5 production reference by Serge Shima — [smixs/visual-skills](https://github.com/smixs/visual-skills)（CC BY 4.0）
- [MapleShaw/seedance2.0-prompt-skill](https://github.com/MapleShaw/seedance2.0-prompt-skill) 的相机四维编码与合规红线经验
- Jacob Ye 的 FILM FORMULA V2.0（与 GPT 共研的 2.0 时代原型）

## Contributing

发现了一种新的翻车方式并且已经写出修复写法？欢迎提 PR——按 [CHANGELOG.md](CHANGELOG.md) 现有条目的格式（**问题 → 根因 → 规则 → 示例**）写清楚，附上章节号。纯理论、未经实测的建议请先在 Issue 里讨论。

## License

[CC BY 4.0](LICENSE) — 转载与二创请注明出处，署名与引用来源见 [NOTICE](NOTICE)。

---

**如果这套框架帮你省下了几百个生成积分，点一个 ⭐ 是最好的谢谢。**

*JACOB YE · SEEDANCE PROMPT · 2026-08*
