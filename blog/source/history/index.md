---
title: History
date: 2026-06-11 12:00:00
---
# 项目更新与发展历史

## 2026-06 — 博客站全面更新

- 重写全部 7 篇博文，从旧版 v1.1.0 架构更新为当前 `strict_word_filler` 引擎
- 新增 About 页面和 History 页面
- 修复导航栏链接跳转到主站根目录的问题
- 移除默认社交链接，替换为项目标语

## 2026-05 — 插件化与双 Skill 支持

项目从独立脚本演进为 Claude Code 插件：

- 注册为 Claude Code Plugin（`.claude-plugin/plugin.json`）
- 新增 [10] 软件概要设计说明书 (SDD) Skill
- SDD Skill 引入 `CSCISectionRule`，支持 CSCI 体系结构块自动组织
- `_actual_row_cells()` 处理合并单元格，清除多余数据行
- 两个 Skill 共享 `strict_word_filler/` 核心引擎

## 2026-03 — 架构重构：strict_word_filler

核心引擎完全重写，引入严格模式设计：

- **BuildPlan 模式**：两阶段设计（构建 → 应用），不可变数据模型
- **models.py**：`frozen=True` dataclass（ExactReplaceRule / ParagraphReplaceRule / DynamicSectionRule / TableFillRule）
- **loader.py**：JSON 解析 + 完整字段校验（`_require_content` / `_require_int`）
- **docx_ops.py**：文档操作核心（段落遍历、克隆、替换、表格填充、图表编号、TOC 标记）
- **template_rules.py**：模板锚点常量与动态章节规则外部化
- **errors.py**：`StrictTemplateError` / `StrictDataError`，不做静默降级
- 废弃旧模块（`doc_fill.py` / `find_and_rep.py` / `dynamic_process.py` / `validate.py`）

## 2026-02 — 初始版本

- 基于 Claude Code Skill 的 Word 文档自动填写工具
- 支持 [08] 软件需求规格说明书 (SRS)
- 交互式问答收集项目信息 → 生成 config.json + project.json → python-docx 填充模板
- 通过 `AskUserQuestion` 工具引导用户完成需求收集
- 支持动态章节（3.2.X 软件能力需求等可变数量子节）
- 博客站基于 Hexo + cactus 主题搭建，部署到 GitHub Pages

## 技术演进路线

```
v1.0 (2026-02)                v2.0 (2026-03)                v3.0 (2026-05)
┌─────────────────┐          ┌─────────────────┐          ┌─────────────────┐
│ 单 Skill [08]    │          │ strict 引擎重构  │          │ Plugin + 双 Skill│
│                 │    ──►   │                 │    ──►   │                 │
│ doc_fill.py     │          │ BuildPlan 模式   │          │ [08] SRS        │
│ find_and_rep.py │          │ frozen dataclass │          │ [10] SDD        │
│ dynamic_proc.py │          │ 严格模式校验     │          │ CSCISectionRule │
│ validate.py     │          │ template_rules   │          │ Claude Plugin   │
└─────────────────┘          └─────────────────┘          └─────────────────┘
  独立脚本                      引擎统一                      插件生态
```

## 未来计划

- [ ] [12] 软件详细设计说明 (SDD-Detail)
- [ ] [09] 接口需求规格说明 (IRS)
- [ ] [13] 软件接口设计说明 (IDD)
- [ ] [15] 软件测试计划 (STP)
- [ ] [19] 软件测试报告 (STR)
- [ ] [20] 软件用户手册 (SUM)
- [ ] 覆盖 GJB 438C 全部 31 类文档模板
