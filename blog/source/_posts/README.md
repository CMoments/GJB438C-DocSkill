---
title: README
date: 2026-03-28 11:25:45
tags:
---
# GJB 438C 文档填写工具集

基于 Claude Code 的军用软件文档自动填写工具 — 告别手工填表，让 AI 替你写文档。

## 支持的文档类型

| 序号 | 文档类型 | 状态 |
|:---:|:---|:---:|
| 08 | 软件需求规格说明书 (SRS) | 已支持 |
| 10 | 软件概要设计说明书 (SDD) | 已支持 |
| 12 | 软件详细设计说明 (SDD-Detail) | 计划中 |
| 09 | 接口需求规格说明 (IRS) | 计划中 |
| 13 | 软件接口设计说明 (IDD) | 计划中 |

> 目标：覆盖 GJB 438C 全部 31 类文档模板。

## 安装

```bash
claude plugin add CMoments/GJB438C-DocSkill
```

## 使用

在 Claude Code 中用自然语言描述需求即可触发对应 Skill：

```
> 帮我按照438C模板生成一份软件需求规格说明书
> 按照GJB 438C标准填写软件概要设计说明
```

## 核心特性

1. **精确替换**：封面信息精确匹配，验证命中数量
2. **段落替换**：锚点文本定位，保留原段落格式
3. **动态章节**：克隆模板段落，批量生成子章节（如 3.2.X）
4. **CSCI 章节**：[10] 专属，自动组织 CSCI 体系结构块
5. **表格填充**：按 `locator_rows` 匹配表格，自动插入数据行
6. **图表编号**：自动更新图表标题编号（表X-X → 表1-1）
7. **目录标记**：设置 `updateFields` 标记，Word 打开时自动刷新目录

## 技术架构

```
skills/
├── word-fillter-438c-08/          # [08] 软件需求规格说明书
│   ├── SKILL.md                   # Skill 定义
│   ├── documents/                 # 模板 .docx
│   ├── templates/                 # config.json + project.json
│   └── scripts/
│       ├── main.py                # CLI 入口
│       ├── process.py             # 免参数入口
│       └── strict_word_filler/    # 核心引擎
│           ├── models.py          # 数据模型（BuildPlan 等）
│           ├── loader.py          # JSON 解析 → BuildPlan
│           ├── docx_ops.py        # 文档操作
│           ├── template_rules.py  # 模板锚点常量
│           ├── errors.py          # 异常类型
│           └── pipeline.py        # CLI 参数解析
└── word-fillter-438c-10/          # [10] 软件概要设计说明书
    └── ...（同上，含 CSCISectionRule 扩展）
```

## 严格模式

引擎采用严格模式，不做静默降级：

- 锚点未精确命中指定数量 → `StrictTemplateError`
- JSON 缺少必填字段 → `StrictDataError`
- 表格列数不匹配 → `StrictTemplateError`
- 只允许修改 `content` 和 `rows`，不得修改 `replacement_pattern`、`locator_rows` 等结构字段

## 许可证

木兰宽松许可证 第2版 (Mulan PSL v2)
