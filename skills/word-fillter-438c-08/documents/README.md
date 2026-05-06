# Strict Word Filler V2

这是一套独立于原有 `src/` 的新实现，目标是：

- 严格按照当前模板结构填充内容
- 不做兜底、不做回退、不猜测模板结构
- 模板锚点、命中数、原型段落只要不符合预期就直接报错
- 支持正文替换、封面固定字段填写、动态插入子节、目录刷新标记

## 运行

```bash
cd /Users/wujunjie/work/word文档填写脚本项目/word_doc_filler_v2
python3 -m pip install -r requirements.txt
python3 main.py \
  --template "/Users/wujunjie/work/word文档填写脚本项目/[08]软件需求规格说明-438C.docx" \
  --config "/Users/wujunjie/work/word文档填写脚本项目/config.json" \
  --project "/Users/wujunjie/work/word文档填写脚本项目/project.json" \
  --output "/Users/wujunjie/work/word文档填写脚本项目/word_doc_filler_v2/output/[08]软件需求规格说明-438C-filled.docx"
```

## 严格规则

- `外部型号+产品名称` 必须在模板中精确出现 2 次
- `软件需求规格说明` 必须在封面区域精确出现 2 次
- `产品型号-XXXX` 必须精确出现 2 次
- `XXXXXXXX公司`、`XXXX年XX月XX日`、`密  级： 内部`、`阶  段：     `、`版  次： A 版` 必须各出现 1 次
- `3.1`、`3.2`、`3.3`、`3.4` 被当成动态章节父节点处理
- `3.2` 和 `3.3` 使用模板里的 `X` 占位标题作为插入原型
- `3.1` 和 `3.4` 使用 `3.10.1` 的标题/正文样式作为显式原型
- 如果模板文字、结构或样式和这套规则不一致，脚本会直接报错，不会继续生成

## 当前实现范围

- 支持 `config.json` 中的封面/标识字段填写
- 支持 `project.json` 中顶层章节、普通占位段落、子节插入
- 支持 `tables` 数组形式的严格表格填充，当前已覆盖引用文档、合格性规定、需求可追踪性表格
- 将目录字段标记为待更新

## 已知约束

- 目录不是静态文本，脚本只负责写入标题并标记字段更新；首次打开 Word 时应刷新目录
- 这套实现是针对当前模板定制的严格版本，不是通用任意 `.docx` 模板引擎
