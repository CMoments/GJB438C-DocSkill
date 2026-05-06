---
title: 😍README
date: 2026-03-28 11:25:45
tags:
---
# 简介

本工具基于Agent Skill实现交互式word文档填写，可在Claude、OpenCode等大语言模型驱动的对话系统上运行，按照软件需求文档438C进行填写。

本工具的脚本实现基于 python-docx 库操作 Word 文档，核心特性：

  1. 段落替换：通过锚点文本定位，保留原段落格式
  2. 多行文本：自动拆分为多个段落，继承原段落样式
  3. 动态章节：克隆模板段落，批量生成子章节
  4. 表格填充：按定位行匹配表格，自动插入数据行
  5. 图表编号：自动更新图表标题编号（表X-X → 表1-1）
  6. 目录标记：设置更新标记，Word 打开时自动刷新目录


# 下载安装
**下载安装Opencode：https://opencode.ai/zh/download**
**安装Skill，将Skill放入`C:\Users\<用户名字>\.config\opencode\skill`**

**配置OpenCode后端模型API**

**任意终端处(建议工作目录的终端)运行：**
```
opencode web
```

# 实现现原理介绍
### 1. 核心流程 (pipeline.py)

  模板 + 配置 → 构建替换计划 → 应用到文档 → 输出

### 2. 数据模型 (models.py)

**定义了 4 种替换规则：**

- ExactReplaceRule     │ 精确文本替换（如封面信息）           
- ParagraphReplaceRule │ 段落锚点替换（查找包含某文本的段落） 
- DynamicSectionRule   │ 动态生成子章节（如需求列表）         
- TableFillRule        │ 表格数据填充                         