---
title: About
date: 2026-06-11 12:00:00
---
# GJB 438C 文档填写工具集

基于 Claude Code 的军用软件文档自动填写工具 — 告别手工填表，让 AI 替你写文档。

## 功能特性

| 序号 | 文档类型 | 状态 |
|:---:|:---|:---:|
| 08 | 软件需求规格说明书 (SRS) | 已支持 |
| 10 | 软件概要设计说明书 (SDD) | 已支持 |
| 12 | 软件详细设计说明 (SDD-Detail) | 计划中 |
| 09 | 接口需求规格说明 (IRS) | 计划中 |
| 13 | 软件接口设计说明 (IDD) | 计划中 |
| 15 | 软件测试计划 (STP) | 计划中 |
| 19 | 软件测试报告 (STR) | 计划中 |
| 20 | 软件用户手册 (SUM) | 计划中 |
| — | 更多模板持续开发中… | 敬请期待 |

> 目标：覆盖 GJB 438C 全部 31 类文档模板，实现军用软件文档全流程自动化。

## 安装

```bash
claude plugin add CMoments/GJB438C-DocSkill
```

或在 Claude Code 对话中执行：

```
/plugin add CMoments/GJB438C-DocSkill
```

## 使用

安装后，在 Claude Code 对话中用自然语言描述需求即可自动触发对应 Skill：

| 触发关键词 | 触发 Skill |
|:---|:---|
| `438C` `需求规格说明` `SRS` `软件需求` | [08] 软件需求规格说明书 |
| `概要设计` `SDD` `设计说明` `概要设计说明` | [10] 软件概要设计说明书 |

示例：

```
> 帮我按照438C模板生成一份软件需求规格说明书，
> 项目名称是"XXX系统"，开发单位是"XX研究所"
```

## 技术架构

```
GJB438C-DocSkill/
├── .claude-plugin/
│   ├── plugin.json              # 插件清单
│   └── marketplace.json         # Marketplace 注册表
├── skills/
│   ├── word-fillter-438c-08/    # [08] 软件需求规格说明书
│   │   ├── SKILL.md             # Skill 定义
│   │   ├── documents/           # 模板 .docx
│   │   ├── templates/           # config.json + project.json
│   │   └── scripts/             # Python 填写引擎
│   │       └── strict_word_filler/  # 核心引擎
│   └── word-fillter-438c-10/    # [10] 软件概要设计说明书
├── demo/                        # 示例输出文档
└── GJB438C全套模版/             # GJB 438C 标准全部模板
```

## 核心引擎

`strict_word_filler/` 引擎采用严格模式，支持以下操作：

- **精确替换** (ExactReplaceRule)：封面信息精确匹配
- **段落替换** (ParagraphReplaceRule)：锚点文本定位，格式保持
- **动态章节** (DynamicSectionRule)：克隆原型段落，生成可变子节
- **CSCI 章节** (CSCISectionRule)：[10] 专属，自动组织 CSCI 块
- **表格填充** (TableFillRule)：按 locator_rows 匹配，自动插入数据行
- **图表编号**：自动更新 表X-X / 图X-X
- **目录标记**：设置 updateFields，Word 打开时自动刷新

## 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/new-template`)
3. 提交变更 (`git commit -m 'feat: 添加 [XX] 模板支持'`)
4. 推送到分支 (`git push origin feature/new-template`)
5. 创建 Pull Request

## 许可证

木兰宽松许可证 第2版 (Mulan PSL v2)
