---
name: word-fillter-438C
description: "当用户提到「按照438C模板填写word文档」「需求文档」「软件需求」「438C」「规格说明」「SRS」时触发。交互式填写 GJB 438C [08] 软件需求规格说明书模板，生成符合规范的 .docx 文档。"
---

# 何时使用

当用户需要基于 `[08]软件需求规格说明-438C.docx` 模板生成或修改 GJB 438C 软件需求规格说明书时使用本 Skill。

# 约束

- 只处理 `.docx` 模板，不处理 `.doc`
- 严格模式运行，不做兜底和回退；模板锚点、表格表头或章节原型不匹配时必须报错
- 目录通过 Word 域刷新，不直接改目录文本
- 只修改 `content` 字段和 `rows` 数组，不得修改模板结构

# 目录结构

- `documents/[08]软件需求规格说明-438C.docx`：模板文档
- `templates/config.json`：封面与标识配置
- `templates/project.json`：章节内容、子章节和表格数据
- `scripts/main.py`：命令行入口（推荐）
- `scripts/process.py`：免参数入口（需将 config/project 放到 scripts/ 目录）

# 工作流

1. 修改 `templates/config.json` 中各字段的 `content`，填写项目名称、版本、单位、日期等封面信息。
2. 修改 `templates/project.json` 中各章节内容：
   - 第 1 章（范围）使用 `placeholders` 数组
   - 第 2 章（引用文档）使用 `tables`
   - 第 3 章（需求）使用 `placeholders`，含 `subsections`（动态章节）和 `tables`（合格性、追踪表）
   - 第 4 章（合格性规定）使用 `tables`
   - 第 5 章（需求可追踪性）使用 `tables`
   - 第 6 章（注释）为静态章节
3. 运行生成脚本（见"运行"章节）。
4. 检查输出 `.docx` 文件，首次在 Word 中打开时刷新目录。

# JSON 规则

## config.json

config.json 包含 `project`、`document`、`content` 三部分，所有字段只修改 `content` 值。

| 字段位置 | type | 说明 | content 生成方式 |
|----------|------|------|-----------------|
| project.* | `original_text` | 项目基础信息（名称、版本、单位等） | 直接使用用户输入 |
| document.* | `original_text` | 文档元信息（编号、标题、日期等） | 直接使用用户输入 |
| content.overview | `background_information` | 项目概述 | 结合用户描述生成 |
| content.scope | `background_information` | 项目范围 | 结合用户描述生成 |
| content.features | `background_information` | 功能特性 | 结合用户描述生成 |

## project.json

### type 取值

| type | 说明 | content 生成方式 |
|------|------|-----------------|
| `content_generation` | 根据提示生成内容 | 结合 `generation_prompt` + 用户需求生成 |
| `text_generation` | 文本生成（较简单） | 根据用户描述生成 |
| `original_text` | 原始文本 | 直接使用用户输入 |

### 章节结构类型

**静态章节**（无 subsections）：
```json
{
  "id": "1.2",
  "name": "系统概述",
  "type": "content_generation",
  "replacement_pattern": "锚点文本...",
  "content": "string"
}
```

**动态章节**（有 subsections）：
```json
{
  "id": "3.2",
  "name": "软件能力需求",
  "type": "content_generation",
  "generation_prompt": "生成子章节的提示...",
  "content": "string（摘要）",
  "subsections": {
    "3.2.1": { "name": "模块名", "content": "string" },
    "3.2.2": { "name": "模块名", "content": "string" }
  }
}
```

**表格填充**：
```json
{
  "id": "2",
  "tables": [{
    "table_id": "reference_documents",
    "locator_rows": [["序号", "名称", "版本", "发布日期", "来源"]],
    "data_start_row": 1,
    "preserve_tail_rows": 0,
    "columns": ["number", "name", "version", "release_date", "source"],
    "rows": [
      { "number": "1", "name": "...", "version": "...", "release_date": "...", "source": "..." }
    ]
  }]
}
```

### 处理规则

1. 只修改 `content` 字段和 `rows` 数组
2. 不修改 `id`、`name`、`type`、`columns`、`replacement_pattern` 等模板结构字段
3. `subsections` 的 key 必须是有效章节编号（如 `"3.2.1"`）
4. `rows` 中每行的字段必须严格等于 `columns` 定义

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
pip install python-docx>=1.1.0
```

生成文档（推荐，使用命令行入口）：

```bash
python scripts/main.py \
  --template "documents/[08]软件需求规格说明-438C.docx" \
  --config "templates/config.json" \
  --project "templates/project.json" \
  --output "output/[08]软件需求规格说明-438C-filled.docx"
```

或使用免参数入口（需先将 config.json 和 project.json 复制到 scripts/ 目录）：

```bash
cd scripts
python process.py
```

输出文档路径会打印在控制台。首次在 Word 中打开时，按提示刷新目录。
