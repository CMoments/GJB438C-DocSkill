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

仓库 `GJB438C全套模版/` 包含全部 31 类模板，目前仅实现了 [08] 和 [10]。为其他模板编写 Skill 是最重要的贡献方式。

#### 目录结构

参照已有 Skill 建立目录：

```
skills/
└── word-fillter-438c-XX/          # XX 为模板编号（如 09、12）
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

   将 `GJB438C全套模版/` 中的 `.doc` 模板转为 `.docx` 格式，放入 `documents/`。

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
