---
name: word-fillter-438c-srs
description: "当用户提到「GJB 438C」「438C-2021」「5.10」「软件需求规格说明」「SRS」「需求文档」「软件需求」时触发。基于 GJB 438C-2021 [5.10] 软件需求规格说明模板，严格填写封面、章节内容、需求条目、合格性规定和需求追踪表，生成符合规范的 .docx 文档。"
---

# 何时使用

当用户需要基于 `[10][SRS] 软件需求规格说明-438C-2021.docx` 模板生成或修改 GJB 438C-2021 软件需求规格说明（SRS）时使用本 Skill。

# 迁移关系

- 旧 GJB 438B `[08] 软件需求规格说明` 对应新版 GJB 438C-2021 `[5.10] 软件需求规格说明`。
- 不再使用 `[08]` 作为新版模板编号；遇到用户说“08/SRS”时，按新版 `[5.10] SRS` 处理。

# 约束

- 只处理 `.docx` 模板，不处理 `.doc`
- 严格模式运行，不做兜底和回退；模板锚点、表格表头或章节原型不匹配时必须报错
- 目录通过 Word 域刷新，不直接改目录文本
- 只修改 `content` 字段和 `rows` 数组，不得修改模板结构

# 目录结构

- `documents/[10][SRS] 软件需求规格说明-438C-2021.docx`：新版 438C SRS 模板文档
- `templates/config.json`：封面与标识配置
- `templates/project.json`：章节内容、子章节和表格数据
- `scripts/main.py`：命令行入口（推荐）
- `scripts/process.py`：免参数入口

# 工作流

1. 修改 `templates/config.json` 中各字段的 `content`，填写项目名称、版本、单位、日期等封面信息。
2. 修改 `templates/project.json` 中各章节内容：
   - 第 1 章（范围）使用 `placeholders` 数组
   - 第 2 章（引用文档）使用 `tables`
   - 第 3 章（需求）使用 `placeholders`，含 `subsections`（动态章节）和 `tables`（合格性、追踪表）
   - 第 4 章（合格性规定）使用 `tables`
   - 第 5 章（需求可追踪性）使用 `tables`
   - 第 6 章（注释）为静态章节
3. 运行生成脚本（见“运行”章节）。
4. 检查输出 `.docx` 文件，首次在 Word 中打开时刷新目录。

# JSON 规则

## config.json

config.json 包含 `project`、`document`、`content` 三部分，所有字段只修改 `content` 值。

## project.json

- 只修改 `content` 字段和 `rows` 数组
- 不修改 `id`、`name`、`type`、`columns`、`replacement_pattern`、`locator_rows` 等模板结构字段
- `subsections` 的 key 必须是有效章节编号（如 `"3.2.1"`）
- `rows` 中每行的字段必须严格等于 `columns` 定义

> `locator_rows` 用于在模板 docx 中定位表格，必须与模板中的实际表头文本完全一致。

# 运行

安装依赖（首次）：

```bash
pip install python-docx>=1.1.0
```

生成文档（推荐，使用命令行入口）：

```bash
python scripts/main.py \
  --template "documents/[10][SRS] 软件需求规格说明-438C-2021.docx" \
  --config "templates/config.json" \
  --project "templates/project.json" \
  --output "output/[10][SRS] 软件需求规格说明-438C-2021-filled.docx"
```

或使用免参数入口：

```bash
cd scripts
python process.py
```