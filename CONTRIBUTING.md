# Contributing to GJB438C-DocSkill

感谢你对本项目的关注！以下是参与贡献的指南。

## 贡献方式

### 报告问题

提交 Issue 时请包含：

- 使用的 Skill（[08] / [10]）和触发方式
- 输入的项目描述或 JSON 配置
- 期望行为与实际行为
- 控制台报错信息（如有）

### 新增 438C 模板 Skill

GJB 438C-2021 第五节规定共 **20 类文档**（5.1–5.20）。`GJB438C全套模版/438B-2009全套模板/` 是旧标准模板集（仅供参考）；`GJB438C全套模版/438C-2021全套模板/` 已按附录 A–T 搭建全套 20 份新标准模板（14 份由 438B 模板改造，6 份按附录全新搭建，详见 `GJB438C全套模版/README.md`）。当前已实现 SRS（5.10）和 SDD（5.11）两个 Skill，但仍基于 438B 模板，将 Skill 内模板替换为 `438C-2021全套模板/` 中对应版本是首要工作。为新文档编写 Skill 是最重要的贡献方式。

#### 目录结构

参照已有 Skill 建立目录：

```
skills/
└── word-fillter-438c-XX/          # XX 为文档缩略语（如 srs、sdd）
    ├── SKILL.md                   # Skill 定义（触发条件 + 工作流 + JSON 规则）
    ├── documents/                 # .docx 模板文件
    │   └── [XX]文档名称-438C.docx
    ├── templates/                 # JSON 配置
    │   ├── config.json            # 封面与标识字段
    │   └── project.json           # 章节结构、锚点、表格定义
    └── scripts/                   # Python 填写脚本
        ├── main.py                # 命令行入口
        ├── process.py             # 免参数入口
        ├── requirements.txt
        └── strict_word_filler/    # 填写引擎（可复用现有实现）
```

#### 编写步骤

1. **准备 .docx 模板**

   **三种来源**（按推荐顺序）：
   - **直接复用现成的 438C-2021 模板**（首选）：从 `GJB438C全套模版/438C-2021全套模板/` 取对应 `.docx` 文件，本项目已按附录 A–T 搭建好 20 份模板骨架与占位文本。
   - **以 438B 模板为起点**（备用）：从 `GJB438C全套模版/438B-2009全套模板/` 取对应 `.doc` 文件转 `.docx`，再按 438C-2021 附录格式调整章节结构。
   - **从标准附录搭建**（最严格）：依据 `GJB438C全套模版/GJB 438C-2021 -word版本 .doc` 中对应附录的"正文格式"说明，从空白 `.docx` 起步搭建。

   放入 `documents/` 目录。

2. **提取模板结构**

   使用以下脚本提取文档中的锚点文本和表格结构：

   ```python
   from docx import Document
   doc = Document("模板文件.docx")
   for i, table in enumerate(doc.tables):
       for j, row in enumerate(table.rows[:3]):
           print(f"Table {i} Row {j}: {[c.text.strip() for c in row.cells]}")
   ```

3. **编写 SKILL.md**

   参照 `skills/word-fillter-438c-08/SKILL.md` 的格式，包含：
   - frontmatter 中的 `name` 和 `description`（含触发关键词）
   - 约束条件
   - 工作流说明
   - JSON 规则（config.json / project.json 各字段的含义和填写方式）
   - 运行命令

4. **编写 config.json**

   封面信息字段，结构与已有 Skill 一致（`project` / `document` / `content` 三部分）。

5. **编写 project.json**

   定义章节结构，包括：
   - 静态章节：`id`、`name`、`type`、`replacement_pattern`、`content`
   - 动态章节：含 `subsections`
   - 表格填充：含 `locator_rows`、`columns`、`rows`

   > **`locator_rows` 必须与模板中的实际表头完全一致**，包括标点符号和空格。

6. **编写脚本**

   可复用 `strict_word_filler/` 填写引擎，只需调整 `main.py` 和 `process.py` 中的路径。

7. **测试**

   使用模板编号对应的示例项目进行端到端测试，确认：
   - 所有锚点正确替换
   - 表格数据正确填充
   - 在 Word 中打开后目录可正常刷新

#### 设计原则

- **严格模式**：锚点或表头不匹配时必须报错，不做静默跳过
- **只改内容**：脚本只修改 `content` 和 `rows`，不修改模板结构字段
- **JSON 驱动**：所有填写内容通过 JSON 配置，脚本不硬编码业务逻辑

- `外部型号+产品名称` 必须在模板中精确出现 2 次
- `软件需求规格说明` 必须在封面区域精确出现 2 次
- `产品型号-XXXX` 必须精确出现 2 次
- `XXXXXXXX公司`、`XXXX年XX月XX日`、`密  级： 内部`、`阶  段：     `、`版  次： A 版` 必须各出现 1 次
- 注意部分章节被当成动态章节父节点处理
- 注意部分章节使用模板里的 `X` 占位标题作为插入原型
- 如果模板文字、结构或样式和这套规则不一致，脚本会直接报错，不会继续生成

### 已知约束

- 目录不是静态文本，脚本只负责写入标题并标记字段更新；首次打开 Word 时应刷新目录
- 这套实现是针对当前模板定制

### 改进现有 Skill

- 修复 `locator_rows` 匹配问题
- 补充遗漏的章节或表格
- 优化 AI 生成的 `generation_prompt`
- 改进填写引擎的鲁棒性

### 文档与博客

- 修正 `blog/` 中的文档错误
- 补充使用教程或最佳实践
- 添加更多语言的说明

## 开发环境

```bash
# 克隆仓库
git clone https://github.com/CMoments/GJB438C-DocSkill.git

# 安装 Python 依赖
pip install python-docx>=1.1.0

# 安装 Claude Code（如需调试 Skill 触发）
# 见 https://claude.ai/code
```

## 提交规范

### Commit Message

```
<type>: <description>
```

type 取值：

| type | 说明 |
|:-----|:-----|
| feat | 新增 Skill 或功能 |
| fix | 修复锚点匹配、表格填充等 Bug |
| docs | 文档或博客更新 |
| refactor | 重构填写引擎，不改变输出 |
| chore | 构建配置、依赖更新 |

示例：

```
feat: 新增 [09] 接口需求规格说明 Skill
fix: [08] 修正引用文档表 locator_rows 匹配
docs: 补充动态章节的使用说明
```

### Pull Request

1. Fork 本仓库
2. 创建分支：`feat/skill-09`、`fix/08-locator` 等
3. 确保本地测试通过（生成文档可正常打开且内容正确）
4. PR 标题遵循 commit message 格式
5. PR 描述中说明：
   - 改动了什么
   - 测试方式
   - 附上生成的样例文件截图或 PDF（如适用）

## 许可

提交贡献即表示你同意将代码以 MIT 许可证发布。
