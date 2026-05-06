from __future__ import annotations


IDENTITY_LINE_ANCHORS = {
    "document_id": "文档标识号：TN/x-DO-DS-V{N.xx}；",
    "title": "标题：；",
    "project_name": "软件名称：；",
    "short_name": "软件缩写：；",
    "version": "软件版本号：。",
}


PATTERN_OVERRIDES: dict[str, str] = {}


INSERTION_PARENT_RULES: dict[str, dict] = {}


CSCI_SECTION_RULE = {
    "summary_anchor": "本章应分为以下几条描述CSCI（或系统）体系结构设计。如果设计的全部或部分依赖于系统的状态或方式，此依赖性应予指明。如果设计信息在多于一个条中出现，它只需被提供一次，而在其他条中引用。本条应提供或引用为了理解设计所需要的设计约定。",
    "end_before_title": "需求可追踪性",
    "prototype_title_anchor": "4.X CSCI",
    "overview_heading_anchor": "4.X.1 CSCI概述",
    "component_section_heading_anchor": "4.X.2 CSCI部件设计",
    "component_item_heading_anchor": "4.X.2.X CSCI部件",
    "component_body_anchor": "本条应描述:",
    "execution_heading_anchor": "4.X.3执行方案",
    "execution_body_anchor": "本条应说明软件部件间的执行方案，可采用图表和描述，来说明软件部件间的动态关系，即CSCI运行期间软件部件间的相互作用情况，(若适用)应包括执行控制流程、数据流、动态控制序列、状态转换图、时序图、部件间的优先关系、中断处理、时序/排序关系、例外处理、并发执行、动态分配与去除分配、对象/进程/任务的动态创建/删除、以及动态行为的其他方面。",
    "interface_heading_anchor": "4.X.4接口设计",
    "interface_id_heading_anchor": "4.X.4.1接口标识和接口图",
    "interface_id_body_anchor": "本条应说明赋予每个接口的项目唯一的标识符，(若适用)应通过名称、编号、版本及文档引用来标识接口实体(软件部件、系统、配置项、用户等)。该标识应说明哪些实体具有固定的接口特性(从而把接口需求分配给这些接口实体);说明哪些实体正在开发或修改(这些实体已有各自的接口需求)。(若适用)应通过接口图来描述这些接口。",
    "interface_detail_heading_anchor": "4.X.4.1.X (接口的项目唯一的标识符)",
    "interface_detail_body_anchor": "本条(从4.X.4.1.1开始)应通过项目唯一的标识符来标识接口，应简要地标识接口实体，根据需要可分条描述单方或双方接口实体的特性。",
}
