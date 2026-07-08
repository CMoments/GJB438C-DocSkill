---
name: word-fillter-438c-sdd
description: "当用户提到「GJB 438C」「438C-2021」「5.11」「软件设计说明」「SDD」「概要设计」「详细设计」「CSCI 体系结构」「CSCI 详细设计」并需要生成或填写软件设计说明 .docx 时触发。基于 GJB 438C-2021 [5.11] `[11][SDD] 软件设计说明-438C-2021.docx`，严格按真实 Word 模板的锚点段落和表格表头定位，支持封面字段填写、正文段落替换、4.3/5 动态子节插入、引用文档表与需求追踪表填充，并在生成后标记 Word 目录字段为待刷新。"
---

# GJB 438C SDD 严格填写

使用本 Skill 填写 GJB 438C-2021 [5.11] 软件设计说明（SDD）。模板文件为 `documents/[11][SDD] 软件设计说明-438C-2021.docx`。

## 何时使用

当用户需要基于 `[11][SDD] 软件设计说明-438C-2021.docx` 生成或修改 GJB 438C-2021 软件设计说明（SDD）时使用本 Skill。

## 设计原则

- **严格模式**：模板锚点、命中数、原型段落、表头任何一项不符合预期都直接报错，不做静默跳过、不做兜底、不猜测模板结构。
- **只改内容**：脚本只读取/写入 JSON 中的 `content` 与 `rows`，不修改模板的 `id`、`name`、`type`、`columns`、`replacement_pattern`、`locator_rows` 等结构字段。
- **JSON 驱动**：所有可填写内容通过 `templates/config.json` 与 `templates/project.json` 配置，脚本不硬编码业务内容。
- **目录刷新**：脚本只写入标题并标记 `w:updateFields`，目录的实际刷新发生在 Word 首次打开文档时。

## 当前模板的严格规则

以下规则基于 `documents/[11][SDD] 软件设计说明-438C-2021.docx` 的实际扫描结果，**不是**通用 438C 模板约定，与 SRS 模板的封面锚点也不同：

- `外部型号+产品名称` 必须在模板中精确出现 **1** 次（封面表格第 1 行）。
- `软件需求规格说明` 必须在封面区域精确出现 **1** 次（模板封面书写为 SRS 标题，脚本将其替换为 `document.title`，例如「软件设计说明」）。
- `产品型号-XXXX` 必须精确出现 **1** 次（封面表格第 2 行）。
- `文档标识号：TN/x-DO-DS-V{N.xx}；`、`标题：`、`软件名称：`、`软件缩写：`、`软件版本号。` 各精确出现 **1** 次（1.1 标识的 Normal Indent 段落块）。
- 本 SDD 模板封面**没有** `XXXXXXXX公司`、`XXXX年XX月XX日`、`密  级： 内部`、`阶  段：     `、`版  次： A 版` 等锚点；这些字段不会出现在 `config.json`，也不会在生成时被替换。
- `4.3` 接口设计 是动态章节父节点，使用模板中的 `4.3.X （接口的唯一标识符）` 作为插入原型，从 `4.3.2` 起按 `subsections` 顺序克隆插入。
- `5` CSCI详细设计 是动态章节父节点，使用模板中的 `5.X (软件单元的唯一标识符，或者一组软件单元的标志符)` 作为插入原型，从 `5.1` 起按 `subsections` 顺序克隆插入。
- `4.3.X`、`5.X` 原型段及其后的模板示例说明文字会被一并删除，再按 `subsections` 重新生成；4.3.1（接口标识和接口图）和第 5 章引言段保留并由 `content` 字段决定其文字。
- 引用文档表（第 2 章）、需求正向追踪表与逆向追踪表（第 6 章）按 `locator_rows` 精确匹配表头；行数不够时按数据行原型克隆扩行。
- 模板「表 X-X」题注由脚本按章号重写：`表2-X 引用文件` → `表2-1 引用文件`、`表X-X 需求的正向追踪性` → `表6-1 需求的正向追踪性`、`表X-X需求的逆向追踪性` → `表6-2需求的逆向追踪性`。

## 与 SRS 模板的关键差异

- 封面锚点每个仅出现 1 次（SRS 大多为 2 次）。
- 封面没有 `XXXXXXXX公司`、`密级`、`阶段`、`版次`、`日期` 等字段，不要在 `config.json` 里给 SDD 加这些字段并期望被写入封面。
- 封面正文写错了文档标题（写作「软件需求规格说明」），脚本默认将其替换为 `document.title`；若 `document.title` 与封面锚点完全相同（例如仍填写 `软件需求规格说明`），脚本仍会按 1 次精确命中替换。
- 第 1 章「范围」标题在模板里是 `Normal` 段落，不是 `Heading 1`；脚本据此调整了题注号编排逻辑，不会把第 2 章的 `表2-X` 误编为 `表1-X`。
- 动态章节父节点为 `4.3` 和 `5`，不是 SRS 的 `3.1`/`3.2`/`3.3`/`3.4`。

## 目录结构

- `documents/[11][SDD] 软件设计说明-438C-2021.docx`：SDD 模板文档
- `templates/config.json`：封面与标识配置（仅 `project.name/short_name/version` 与 `document.id/title` 会被写入模板）
- `templates/project.json`：章节内容、动态子节、表格数据
- `scripts/main.py`：命令行入口（推荐）
- `scripts/process.py`：免参数入口
- `scripts/strict_word_filler/`：严格填充运行时
  - `loader.py`：解析 JSON、构造 `BuildPlan`、调用模板规则
  - `docx_ops.py`：Word 段落 / 表格 / 题注 / 目录刷新操作
  - `template_rules.py`：SDD 模板锚点、动态章节规则、模式覆盖
  - `models.py`：`BuildPlan` 等数据类
  - `errors.py`：`StrictTemplateError` / `StrictDataError`
  - `pipeline.py`：CLI 入口

## JSON 规则

### config.json

`config.json` 沿用 SRS 三段式结构（`project`、`document`、`content`），脚本只读取下列字段的 `content`：

- `project.name`：外部型号+产品名称（写入封面表格第 1 行第 1 段）
- `project.short_name`：项目简称（与「产品型号-」前缀拼接写入封面表格第 2 行）
- `project.version`：版本号（写入 1.1 标识块的「软件版本号：…。」）
- `document.id`：文档标识号（写入 1.1 标识块的「文档标识号：…；」）
- `document.title`：文档标题（同时写入封面「软件需求规格说明」位置和 1.1 标识块的「标题：…」）

`project.company`、`project.department`、`document.classification`、`document.phase`、`document.date`、`content.*` 仅为兼容 SRS 命令行参数保留，SDD 模板里没有对应锚点，**不会**被写入文档。

### project.json

- 顶层 `structure` 中的每个章节按章号（`"1"`、`"2"`、…、`"7"`）组织。
- 章节可选字段：
  - `replacement_pattern` + `content`：将该章正文里的占位段替换为 `content`（多行用 `\n\n` 分段）。
  - `placeholders`：章节下的固定子节列表（如 1.1/1.2/1.3、4.1/4.2），每个 placeholder 同样支持 `replacement_pattern` + `content`，并可在 `subsections` 中定义更深层子节。
  - `tables`：严格表格填充定义（见下）。
- 动态章节父节点 `4.3` 和 `5` 必须作为顶层 `structure` 条目（不能放在某个章节的 `placeholders` 里），结构为：
  ```json
  "4.3": {
    "title": "接口设计",
    "type": "content_generation",
    "content": "<4.3.1 接口标识和接口图 段的正文>",
    "subsections": {
      "4.3.2": {"name": "<接口标题>", "content": "<接口正文，多行用 \n\n>"},
      "4.3.3": {"name": "...", "content": "..."}
    }
  }
  ```
  - 脚本会把模板里 `4.3.X` 原型段及其后的所有示例说明删除，再按 `subsections` 顺序生成 `4.3.2`、`4.3.3`、… 每个子节都使用原型段的样式。
  - `content` 会替换 4.3 章节首段的文本（模板中是 4.3.1 的正文）。
- 表格填充（`tables` 数组，每项）：
  - `table_id`：脚本内部使用的表名（仅用于错误信息）
  - `locator_rows`：按从上到下顺序匹配模板表头行的精确文本（每个单元格必须完全一致）
  - `data_start_row`：模板里第一行数据行的索引（0 基，从表头之下开始计数）
  - `preserve_tail_rows`：模板末尾需要原样保留的行数（例如正向追踪表尾部的「若存在一对多则此形式表达」示例行）
  - `columns`：列名列表，**必须**与每个 `rows` 项的键完全一致
  - `rows`：数据行数组，每行的字段集合必须严格等于 `columns`
- 不允许在 `subsections` 中给一个既没有 `replacement_pattern` 又不是动态章节的子节随便塞内容；脚本会报错。

## 工作流

1. 修改 `templates/config.json` 中 `project.*` 与 `document.*` 的 `content`。
2. 修改 `templates/project.json` 中各章节的 `content`、`subsections`、`tables.rows`：
   - 第 1 章（范围）使用 `placeholders` 数组。
   - 第 2 章（引用文档）使用 `tables`。
   - 第 3 章（CSCI 级设计决策）使用 `replacement_pattern` + `content`。
   - 第 4 章（CSCI 体系结构设计）使用 `placeholders`（4.1、4.2），4.3 作为顶层动态章节。
   - 第 4.3 章（接口设计）作为顶层 `structure.4.3` 动态章节，含 `subsections`。
   - 第 5 章（CSCI 详细设计）作为顶层 `structure.5` 动态章节，含 `subsections`。
   - 第 6 章（需求可追踪性）使用 `tables`（正向 + 逆向）。
   - 第 7 章（注释）使用 `replacement_pattern` + `content`。
3. 运行生成脚本（见下）。
4. 在 Word 中打开输出文件，按 F9 或右键「更新域」刷新目录与题注。

## 运行

安装依赖（首次）：

```bash
pip install -r scripts/requirements.txt
```

生成文档（推荐，使用命令行入口）：

```bash
python scripts/main.py \
  --template "documents/[11][SDD] 软件设计说明-438C-2021.docx" \
  --config "templates/config.json" \
  --project "templates/project.json" \
  --output "output/[11][SDD] 软件设计说明-438C-2021-filled.docx"
```

或使用免参数入口：

```bash
cd scripts
python process.py
```

## 已知约束

- 目录不是静态文本，脚本只负责写入标题并标记字段更新；首次打开 Word 时应刷新目录（F9 或「更新域」）。
- 模板里第 1 章标题「范围」是 `Normal` 段落而非 `Heading 1`，因此 Word 自动生成的 TOC 默认不会列出「1 范围」这条目，但章节下的 1.1/1.2/1.3 子节会照常出现；这是模板本身的行为，脚本不强行修正。
- 题注号编排以题注文字中显式给出的章号为准（例如 `表2-X` 编为 `表2-1`），`表X-X` 形式则按当前 Heading 1 章号编排。
- 这套实现是针对当前模板定制的严格版本，不是通用任意 `.docx` 模板引擎。
