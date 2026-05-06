---
title: 📚Reference：word文档结构 
date: 2026-03-02 14:28:44
tags:
---

这页文档与项目关系不大。但主要介绍doc文档的XML结构，理解docx库和XML的结构对于能够高效、正确修改脚本至关重要。

[**python-docx官方文档**](https://python-docx.readthedocs.io/en/latest/)

# 整体结构
`.docx`本质是一个ZIP包，核心正文在解压后的`word/document.xml`。
脚本所做的工作就是在操作`document.xml`里的正文树。

### 正文XML树
``` xml
<w:document>
  <w:body>
    <w:p>...</w:p>          <!-- 段落 Paragraph -->
    <w:tbl>...</w:tbl>      <!-- 表格 Table -->
    <w:p>...</w:p>
    ...
    <w:sectPr>...</w:sectPr> <!-- 节属性（页边距/页码等） -->
  </w:body>
</w:document>
```

### 段落内部（`w:p`）
```xml
<w:p>
  <w:pPr>...</w:pPr>        <!-- 段落样式、编号、对齐等 -->
  <w:r><w:t>文本</w:t></w:r> <!-- run + text -->
  <w:hyperlink>...</w:hyperlink>
  <w:r><w:drawing>图片/形状</w:drawing></w:r>
</w:p>
```


### 表格内部（`w:tbl`）
```xml
<w:tbl>
  <w:tr>                    <!-- 行 -->
    <w:tc>                  <!-- 单元格 -->
      <w:p>...</w:p>        <!-- 单元格里仍然是段落 -->
    </w:tc>
  </w:tr>
</w:tbl>
```

# Tips
- 脚本`delete_anchor.py`删 `Paragraph` 时，是把整个 `w:p` 节点移除，因此里面的 run/文本/超链接/行内图都会一起删除。
- 表格是和段落并列的“块级节点”；删段落函数不会删 `w:tbl`。
- `delete_paragraph(paragraph)` 仅适配 `w:p`。
- 对“正文顶层的表格”无效；要删表格需移除 `Table._element`（`w:tbl`）。

- `doc.paragraphs` 只给你段落视图，不代表文档全部元素。
- 文本框、页眉页脚、批注、脚注等在别的 part，不在 `document.body` 的这条简单路径里。
