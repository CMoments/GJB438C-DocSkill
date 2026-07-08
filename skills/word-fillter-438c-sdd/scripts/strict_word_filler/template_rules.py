from __future__ import annotations


IDENTITY_LINE_ANCHORS = {
    "document_id": "文档标识号：TN/x-DO-DS-V{N.xx}；",
    "title": "标题：",
    "project_name": "软件名称：",
    "short_name": "软件缩写：",
    "version": "软件版本号。",
}


PATTERN_OVERRIDES: dict[str, str] = {
    "1.1": "本条应描述本文档所适用软件的完整标识",
    "1.2": "本条应概述本文档所适用软件的用途",
    "1.3": "本条应概述本文档的用途和内容",
    "2": "本章应列出引用文档的编号、标题、编写单位、修订版及日期",
    "3": "本章应根据需要分条给出CSCI级设计决策",
    "4.1": "本条应描述：",
    "4.2": "本条应说明软件单元间的执行方案",
    "4.3": "本条应说明赋予每个接口的唯一标识符",
    "5": "本章应分为以下子条描述CSCI的软件单元",
    "6": "本章应包含:",
    "7": "本章应包括有助于了解文档的所有信息",
}


COVER_TITLE_ANCHOR = "软件需求规格说明"


INSERTION_PARENT_RULES = {
    "4.3": {
        "parent_title": "接口设计",
        "summary_anchor": "本条应说明赋予每个接口的唯一标识符",
        "end_before_title": "CSCI详细设计",
        "prototype_title_anchor": "4.3.X （接口的唯一标识符）",
        "prototype_body_anchor": "本条(从4.3.2开始)应通过唯一标识符来标识接口",
        "cleanup_anchors": (
            "4.3.X （接口的唯一标识符）",
        ),
        "cleanup_to_end": True,
    },
    "5": {
        "parent_title": "CSCI详细设计",
        "summary_anchor": "本章应分为以下子条描述CSCI的软件单元",
        "end_before_title": "需求可追踪性",
        "prototype_title_anchor": "5.X (软件单元的唯一标识符，或者一组软件单元的标志符)",
        "prototype_body_anchor": "本条应通过唯一标识符来标识软件单元",
        "cleanup_anchors": (
            "5.X (软件单元的唯一标识符，或者一组软件单元的标志符)",
        ),
        "cleanup_to_end": True,
    },
}
