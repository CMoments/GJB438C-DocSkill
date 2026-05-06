---
name: word-fillter-438C-10
description: "当用户提到「438C 软件概要设计说明」「[10] 软件概要设计说明」「SDD」「概要设计模板填写」「设计说明」时触发。基于 GJB 438C [10] 软件概要设计说明模板，严格填写封面、章节内容、CSCI 体系结构块和追踪表，生成符合规范的 .docx 文档。"
---

# 何时使用

当用户需要基于 `[10]软件概要设计说明-438C.docx` 模板生成或修改 GJB 438C 软件概要设计说明时使用本 Skill。

# 约束

- 只处理 `.docx` 模板，不处理 `.doc`
- 严格模式运行，不做兜底和回退；模板锚点、表格表头或章节原型不匹配时必须报错
- 目录通过 Word 域刷新，不直接改目录文本
- 只修改 `content` 字段和 `rows` 数组，不得修改模板结构

# 目录结构

- `documents/[10]软件概要设计说明-438C.docx`：模板文档
- `templates/config.json`：封面与标识配置
- `templates/project.json`：章节内容、CSCI 结构和表格数据
- `scripts/main.py`：命令行入口（推荐）
- `scripts/process.py`：免参数入口

# 工作流

1. 修改 `templates/config.json` 中各字段的 `content`，填写项目名称、版本、单位、日期等封面信息。
2. 修改 `templates/project.json` 中各章节内容：
   - 第 1 章（范围）使用 `placeholders` 数组
   - 第 2 章（引用文档）使用 `tables`
   - 第 3 章（系统设计决策）为静态章节
   - 第 4 章（系统体系结构设计）使用 `cscis` 数组定义 CSCI 块
   - 第 5 章（需求可追踪性）使用 `tables`
   - 第 6 章（注释）为静态章节
3. 运行生成脚本（见"运行"章节）。
4. 检查输出 `.docx` 文件，首次在 Word 中打开时刷新目录。

# JSON 规则

## config.json

所有字段只修改 `content` 值，结构与 [08] Skill 完全一致，包含 `project`、`document`、`content` 三部分。

## project.json

### 通用规则

- 普通章节只修改 `content`
- 表格只修改 `rows`
- `locator_rows`、`columns`、章节编号和模板锚点不得改动

### 第 4 章 cscis 结构

第 4 章使用 `cscis` 数组，每个 CSCI 项必须提供以下 9 个字段：

| 字段 | 说明 |
|------|------|
| `title` | CSCI 名称 |
| `overview` | CSCI 概述 |
| `component_title` | 部件标题 |
| `component_design` | 部件设计描述 |
| `execution_plan` | 执行计划 |
| `interface_overview` | 接口概述 |
| `interface_identification` | 接口标识规则 |
| `interface_detail_title` | 接口详细标题 |
| `interface_details` | 接口详细描述 |

> **`locator_rows` 严禁修改！**
> `locator_rows` 用于在模板 docx 中定位表格，脚本通过逐行比较单元格文本查找目标表格。
> 其中的文本必须与模板 docx 中的实际表头文本完全一致，包括标点符号、空格和特殊字符。
>
> 修改后会导致报错 `期望命中 1 张表，实际 0 张`。
>
> 若不确定实际表头文本，用以下脚本提取：
> ```python
> from docx import Document
> doc = Document("模板文件.docx")
> for i, table in enumerate(doc.tables):
>     for j, row in enumerate(table.rows[:3]):
>         print(f"Table {i} Row {j}: {[c.text.strip() for c in row.cells]}")
> ```

# 运行

安装依赖（首次）：

```bash
pip install -r scripts/requirements.txt
```

生成文档（推荐，使用命令行入口）：

```bash
python scripts/main.py \
  --template "documents/[10]软件概要设计说明-438C.docx" \
  --config "templates/config.json" \
  --project "templates/project.json" \
  --output "output/[10]软件概要设计说明-438C-filled.docx"
```

或使用免参数入口：

```bash
cd scripts
python process.py
```

输出文档路径会打印在控制台。首次在 Word 中打开时，按提示刷新目录。
