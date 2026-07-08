<div align="center">

# GJB 438C 文档填写工具集

**基于 Claude Code 的军用软件文档自动填写工具 — 告别手工填表，让 AI 替你写文档**

[![GitHub Stars](https://img.shields.io/badge/Stars-999+-yellow?style=social&logo=github)](https://github.com/CMoments/GJB438C-DocSkill/stargazers)
[![License](https://img.shields.io/badge/License-Mulan_PSL_v2-blue)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Plugin-7C3AED?logo=anthropic&logoColor=white)](https://claude.ai/code)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg)](https://github.com/CMoments/GJB438C-DocSkill/pulls)

---

</div>

## 目录

- [功能特性](#-功能特性)
- [快速开始](#-快速开始)
- [使用方式](#-使用方式)
- [模板覆盖](#-模板覆盖)
- [技术架构](#-技术架构)
- [贡献指南](#-贡献指南)
- [许可证](#-许可证)

---

## ✨ 功能特性

<table>
<tr>
<td width="50%">

### 📝 [10] 软件需求规格说明书

基于 GJB 438C-2021 [5.10] 标准模板的 SRS 文档自动生成

- 交互式填写封面信息
- 自动生成章节内容（范围、需求、接口…）
- 合格性规定表格自动填充
- 需求追踪表双向关联
- 严格模式校验模板锚点

</td>
<td width="50%">

### 🏗️ [11] 软件设计说明书

基于 GJB 438C-2021 [5.11] 标准模板的 SDD 文档自动生成

- CSCI 体系结构自动组织
- 部件设计与接口描述生成
- 执行计划与接口详细设计
- 需求可追踪性矩阵
- 严格模式校验模板锚点

</td>
</tr>
</table>



💡 **核心理念**：用户只需用自然语言描述项目信息，Claude 自动完成模板匹配、内容生成和文档导出。

---

## 🚀 快速开始

### 前置要求

- 任意支持Agent Skill的AI工具
- Python 3.10+（由 skill 自动调用）

### 安装

**方式一：直接安装 Plugin**（推荐 ✅）
以Claude为例：

[Claude Code CLI](https://claude.ai/code) 需安装并完成配置：

```bash
claude plugin add CMoments/GJB438C-DocSkill
```

或在 Claude Code 对话中执行：

```
/plugin add CMoments/GJB438C-DocSkill
```

**方式二：通过 Marketplace 添加**

```bash
claude plugin marketplace add https://github.com/CMoments/GJB438C-DocSkill
claude plugin install gjb438c-doc-filler
```

---

## 📖 使用方式

安装后，在 Claude Code 对话中用自然语言描述需求即可自动触发对应 Skill：

| 触发关键词 | 触发 Skill |
|:---|:---|
| `438C` `5.10` `需求规格说明` `SRS` `软件需求` | `[10]` 软件需求规格说明书 |
| `438C` `5.11` `SDD` `软件设计说明` `概要设计` | `[11]` 软件设计说明书 |

### 示例对话

```
# 生成需求规格说明书
> 帮我按照438C 5.10模板生成一份软件需求规格说明书，
> 项目名称是"XXX系统"，开发单位是"XX研究所"

# 生成概要设计说明书
> 按照GJB 438C 5.11模板填写软件设计说明，
> 项目是编译器系统，包含词法分析和语法分析模块
```

Claude 会依次引导你完成封面信息、章节内容的填写，最终输出合规的 `.docx` 文件。

---

## 📋 模板覆盖

GJB 438C-2021 第五节规定共 **20 类文档**（5.1–5.20），`GJB438C全套模版/438C-2021全套模板/` 已按新版编号保存模板。当前 Skill 明确支持旧版能力迁移后的两类文档：

| 438C 编号 | 文档类型 | 缩略语 | 旧 438B 对应 | Skill 支持状态 |
|:---:|:---|:---:|:---:|:---:|
| [10] | 软件需求规格说明 | SRS | 软件需求规格说明（旧 438B） | ✅ 已支持 |
| [11] | 软件设计说明 | SDD | 软件概要设计说明（旧 438B） | ✅ 已支持 |
| 5.1–5.9, 5.12–5.20 | 其他 438C 文档模板 | - | - | 🔜 计划中 |

> 📁 新版模板文件位于 `GJB438C全套模版/438C-2021全套模板/`。当前两个 Skill 分别放在 `skills/word-fillter-438c-srs/` 和 `skills/word-fillter-438c-sdd/`。
> ---:|:---|:---:|:---:|
> | [1] | 软件开发计划 | SDP | 🔜 计划中 |
> | [2] | 软件安装计划 | SIP | 🔜 计划中 |
> | [3] | 软件移交计划 | STrP | 🔜 计划中 |
> | [4] | 软件测试计划 | STP | 🔜 计划中 |
> | [5] | 运行方案说明 | OCD | 🔜 计划中 |
> | [6] | 系统/子系统规格说明 | SSS | 🔜 计划中 |
> | [7] | 接口需求规格说明 | IRS | 🔜 计划中 |
> | [8] | 系统/子系统设计说明 | SSDD | 🔜 计划中 |
> | [9] | 接口设计说明 | IDD | 🔜 计划中 |
> | [10] | 软件需求规格说明 | SRS | ✅ 已支持  |
> | [11] | 软件设计说明 | SDD |  ✅ 已支持  |
> | [12] | 数据库设计说明 | DBDD | 🔜 计划中 |
> | [13] | 软件测试说明 | STD | 🔜 计划中 |
> | [14] | 软件测试报告 | STR | 🔜 计划中 |
> | [15] | 软件产品规格说明 | SPS | 🔜 计划中 |
> | [16] | 软件版本说明 | SVD | 🔜 计划中 |
> | [17] | 软件用户手册 | SUM | 🔜 计划中 |
> | [18] | 计算机编程手册 | CPM | 🔜 计划中 |
> | [19] | 固件保障手册 | FSM | 🔜 计划中 |
> | [20] | 软件研制总结报告 | SDSR | 🔜 计划中 |

> 🎯 **目标**：覆盖 GJB 438B-2021 全部 20 类文档，实现军用软件文档全流程自动化。
> 📁 模板文件位于 `GJB438C全套模版/438B-2009全套模板/`，14 份由 438B 模板改造而来，6 份按附录全新搭建；每份均含章节骨架与示例占位文本，供具体项目填写。Skill 仍在开发中，欢迎贡献。

---

## 🛠️ 技术架构

```
GJB438C-DocSkill/
├── .claude-plugin/
│   ├── plugin.json              # 插件清单
│   └── marketplace.json         # Marketplace 注册表
├── skills/
│   ├── word-fillter-438c-srs/    # [10] 软件需求规格说明书
│   │   ├── SKILL.md             # Skill 定义
│   │   ├── documents/           # 模板 .docx
│   │   ├── templates/           # config.json + project.json
│   │   └── scripts/             # Python 填写引擎
│   │       ├── main.py          # CLI 入口
│   │       ├── process.py       # 免参数入口
│   │       └── strict_word_filler/  # 核心引擎
│   └── word-fillter-438c-sdd/    # [11] 软件设计说明书
│       ├── SKILL.md
│       ├── documents/
│       ├── templates/
│       └── scripts/
├── demo/                        # 示例输出文档
└── GJB438C全套模版/             # 标准资料与历史模板
    ├── 438B-2009全套模板/        # 旧标准 31 类模板（仅供参考）
    ├── 438B-2009全套模板/        # ✅ 新标准 20 类模板（按附录 A–T 搭建）
    ├── GJB 438C-2021 -word版本 .doc  # 新标准原文
    └── README.md                # 模板状态说明
```

**技术栈：**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![python-docx](https://img.shields.io/badge/python--docx-1.1.0+-orange)
![Claude](https://img.shields.io/badge/Claude-Code-7C3AED?logo=anthropic&logoColor=white)

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg)](https://github.com/CMoments/GJB438C-DocSkill/pulls)
[![Issues](https://img.shields.io/github/issues/CMoments/GJB438C-DocSkill)](https://github.com/CMoments/GJB438C-DocSkill/issues)

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/new-template`)
3. 提交变更 (`git commit -m 'feat: 添加 [XX] 模板支持'`)
4. 推送到分支 (`git push origin feature/new-template`)
5. 创建 Pull Request

### 致谢

感谢所有为本项目做出贡献的开发者：

[![Contributors](https://img.shields.io/github/contributors/CMoments/GJB438C-DocSkill?color=blue)](https://github.com/CMoments/GJB438C-DocSkill/graphs/contributors)

---

## 📄 许可证

本项目基于 [木兰宽松许可证 第2版 (Mulan PSL v2)](LICENSE) 开源。

---

<div align="center">

[![Made with Claude Code](https://img.shields.io/badge/Made_with-Claude_Code-7C3AED?logo=anthropic&logoColor=white)](https://claude.ai/code)

**如果这个项目对你有帮助，请给个 ⭐ Star 支持一下！**

</div>
