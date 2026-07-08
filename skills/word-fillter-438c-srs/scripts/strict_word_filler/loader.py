from __future__ import annotations

import json
from pathlib import Path

from .errors import StrictDataError
from .models import BuildPlan, DynamicSectionItem, DynamicSectionRule, ExactReplaceRule, ParagraphReplaceRule, TableFillRule
from .template_rules import IDENTITY_LINE_ANCHORS, INSERTION_PARENT_RULES, PATTERN_OVERRIDES


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _require_content(data: dict, *keys: str) -> str:
    current = data
    for key in keys:
        if key not in current:
            joined = ".".join(keys)
            raise StrictDataError(f"缺少必填字段: {joined}")
        current = current[key]
    if not isinstance(current, str) or not current.strip():
        joined = ".".join(keys)
        raise StrictDataError(f"字段为空: {joined}")
    return current.strip()


def _sorted_section_items(items: dict[str, dict]) -> list[tuple[str, dict]]:
    def sort_key(item: tuple[str, dict]) -> tuple[int, ...]:
        return tuple(int(part) for part in item[0].split("."))

    return sorted(items.items(), key=sort_key)


def _require_int(data: dict, *keys: str) -> int:
    current = data
    for key in keys:
        if key not in current:
            joined = ".".join(keys)
            raise StrictDataError(f"缺少必填字段: {joined}")
        current = current[key]
    if not isinstance(current, int):
        joined = ".".join(keys)
        raise StrictDataError(f"字段不是整数: {joined}")
    return current


def _parse_table_rules(section_id: str, section_data: dict) -> list[TableFillRule]:
    raw_tables = section_data.get("tables", [])
    if not raw_tables:
        return []
    if not isinstance(raw_tables, list):
        raise StrictDataError(f"章节 {section_id} 的 tables 必须是数组")

    table_rules: list[TableFillRule] = []
    for index, table in enumerate(raw_tables, start=1):
        if not isinstance(table, dict):
            raise StrictDataError(f"章节 {section_id} 的 tables[{index}] 结构非法")

        table_id = _require_content({"value": table.get("table_id")}, "value")
        data_start_row = _require_int(table, "data_start_row")
        preserve_tail_rows = _require_int(table, "preserve_tail_rows")
        if data_start_row < 0 or preserve_tail_rows < 0:
            raise StrictDataError(f"章节 {section_id} 的表格 {table_id} 行参数不能为负数")

        locator_rows = table.get("locator_rows")
        if not isinstance(locator_rows, list) or not locator_rows:
            raise StrictDataError(f"章节 {section_id} 的表格 {table_id} 缺少 locator_rows")
        parsed_locator_rows: list[tuple[str, ...]] = []
        for locator_index, locator_row in enumerate(locator_rows, start=1):
            if not isinstance(locator_row, list) or not locator_row:
                raise StrictDataError(f"章节 {section_id} 的表格 {table_id} locator_rows[{locator_index}] 非法")
            parsed_locator_rows.append(
                tuple(_require_content({"value": cell}, "value") for cell in locator_row)
            )

        columns = table.get("columns")
        if not isinstance(columns, list) or not columns:
            raise StrictDataError(f"章节 {section_id} 的表格 {table_id} 缺少 columns")
        parsed_columns = tuple(_require_content({"value": column}, "value") for column in columns)
        if len(set(parsed_columns)) != len(parsed_columns):
            raise StrictDataError(f"章节 {section_id} 的表格 {table_id} columns 不能重复")

        rows = table.get("rows")
        if not isinstance(rows, list):
            raise StrictDataError(f"章节 {section_id} 的表格 {table_id} rows 必须是数组")
        parsed_rows: list[tuple[str, ...]] = []
        for row_index, row in enumerate(rows, start=1):
            if not isinstance(row, dict):
                raise StrictDataError(f"章节 {section_id} 的表格 {table_id} rows[{row_index}] 结构非法")
            row_keys = set(row.keys())
            expected_keys = set(parsed_columns)
            if row_keys != expected_keys:
                raise StrictDataError(
                    f"章节 {section_id} 的表格 {table_id} rows[{row_index}] 字段必须严格等于 {list(parsed_columns)}"
                )
            parsed_rows.append(
                tuple(_require_content({"value": row[column]}, "value") for column in parsed_columns)
            )

        table_rules.append(
            TableFillRule(
                key=f"{section_id}.{table_id}",
                locator_rows=tuple(parsed_locator_rows),
                columns=parsed_columns,
                rows=tuple(parsed_rows),
                data_start_row=data_start_row,
                preserve_tail_rows=preserve_tail_rows,
            )
        )

    return table_rules


def build_plan(config_data: dict, project_data: dict) -> BuildPlan:
    exact_rules: list[ExactReplaceRule] = []
    paragraph_rules: list[ParagraphReplaceRule] = []
    dynamic_rules: list[DynamicSectionRule] = []
    table_rules: list[TableFillRule] = []

    project_name = _require_content(config_data, "project", "name", "content")
    short_name = _require_content(config_data, "project", "short_name", "content")
    version = _require_content(config_data, "project", "version", "content")
    company = _require_content(config_data, "project", "company", "content")
    document_id = _require_content(config_data, "document", "id", "content")
    document_title = _require_content(config_data, "document", "title", "content")
    classification = _require_content(config_data, "document", "classification", "content")
    phase = _require_content(config_data, "document", "phase", "content")
    document_date = _require_content(config_data, "document", "date", "content")

    exact_rules.extend(
        [
            ExactReplaceRule("cover.project_name", "外部型号+产品名称", project_name, 2),
            ExactReplaceRule("cover.document_title", "软件需求规格说明", document_title, 2),
            ExactReplaceRule("cover.short_name", "产品型号-XXXX", f"产品型号-{short_name}", 2),
            ExactReplaceRule("cover.company", "XXXXXXXX公司", company, 1),
            ExactReplaceRule("cover.date", "XXXX年XX月XX日", document_date, 1),
            ExactReplaceRule("cover.classification", "密  级： 内部", f"密  级： {classification}", 1),
            ExactReplaceRule("cover.phase", "阶  段：     ", f"阶  段： {phase}", 1),
            ExactReplaceRule("cover.version", "版  次： A 版", f"版  次： {version}", 1),
            ExactReplaceRule("identity.document_id", IDENTITY_LINE_ANCHORS["document_id"], f"文档标识号：{document_id}；", 1),
            ExactReplaceRule("identity.title", IDENTITY_LINE_ANCHORS["title"], f"标题：{document_title}", 1),
            ExactReplaceRule("identity.project_name", IDENTITY_LINE_ANCHORS["project_name"], f"软件名称：{project_name}", 1),
            ExactReplaceRule("identity.short_name", IDENTITY_LINE_ANCHORS["short_name"], f"软件缩写：{short_name}", 1),
            ExactReplaceRule("identity.version", IDENTITY_LINE_ANCHORS["version"], f"软件版本号：{version}。", 1),
        ]
    )

    structure = project_data.get("structure")
    if not isinstance(structure, dict):
        raise StrictDataError("project.json 缺少 structure 对象")

    for section_id, section_data in structure.items():
        if not isinstance(section_data, dict):
            raise StrictDataError(f"章节 {section_id} 结构非法")

        if "replacement_pattern" in section_data and "content" in section_data:
            paragraph_rules.append(
                ParagraphReplaceRule(
                    key=section_id,
                    anchor_text=PATTERN_OVERRIDES.get(section_id, section_data["replacement_pattern"]),
                    new_text=_require_content({"value": section_data["content"]}, "value"),
                )
            )

        table_rules.extend(_parse_table_rules(section_id, section_data))

        for sub_id, sub_data in _sorted_section_items(section_data.get("subsections", {})):
            if section_id in INSERTION_PARENT_RULES:
                raise StrictDataError(f"不支持顶层章节 {section_id} 的动态子节写法")
            if not isinstance(sub_data, dict):
                raise StrictDataError(f"章节 {sub_id} 结构非法")
            if "replacement_pattern" not in sub_data or "content" not in sub_data:
                raise StrictDataError(f"章节 {sub_id} 缺少 replacement_pattern 或 content")
            paragraph_rules.append(
                ParagraphReplaceRule(
                    key=sub_id,
                    anchor_text=sub_data["replacement_pattern"],
                    new_text=_require_content({"value": sub_data["content"]}, "value"),
                )
            )

        for placeholder in section_data.get("placeholders", []):
            if not isinstance(placeholder, dict) or "id" not in placeholder:
                raise StrictDataError(f"章节 {section_id} 的 placeholder 结构非法")

            placeholder_id = placeholder["id"]
            if placeholder_id in INSERTION_PARENT_RULES:
                rule_spec = INSERTION_PARENT_RULES[placeholder_id]
                items: list[DynamicSectionItem] = []
                subsections = placeholder.get("subsections", {})
                if not isinstance(subsections, dict) or not subsections:
                    raise StrictDataError(f"动态章节 {placeholder_id} 缺少 subsections")
                for sub_id, sub_data in _sorted_section_items(subsections):
                    if not isinstance(sub_data, dict):
                        raise StrictDataError(f"动态章节 {sub_id} 结构非法")
                    title = _require_content({"value": sub_data.get("name")}, "value")
                    body = _require_content({"value": sub_data.get("content")}, "value")
                    items.append(DynamicSectionItem(section_id=sub_id, title=title, body=body))

                summary_text = _require_content({"value": placeholder.get("content")}, "value")
                paragraph_rules.append(
                    ParagraphReplaceRule(
                        key=f"{placeholder_id}.summary",
                        anchor_text=rule_spec["summary_anchor"],
                        new_text=summary_text,
                    )
                )
                dynamic_rules.append(
                    DynamicSectionRule(
                        parent_id=placeholder_id,
                        parent_title=rule_spec["parent_title"],
                        summary_anchor=rule_spec["summary_anchor"],
                        end_before_title=rule_spec["end_before_title"],
                        prototype_title_anchor=rule_spec["prototype_title_anchor"],
                        prototype_body_anchor=rule_spec["prototype_body_anchor"],
                        cleanup_anchors=tuple(rule_spec["cleanup_anchors"]),
                        cleanup_to_end=bool(rule_spec["cleanup_to_end"]),
                        items=tuple(items),
                        summary_text=summary_text,
                    )
                )
                continue

            if "replacement_pattern" in placeholder and "content" in placeholder:
                anchor_text = PATTERN_OVERRIDES.get(placeholder_id, placeholder["replacement_pattern"])
                paragraph_rules.append(
                    ParagraphReplaceRule(
                        key=placeholder_id,
                        anchor_text=anchor_text,
                        new_text=_require_content({"value": placeholder["content"]}, "value"),
                    )
                )

            subsections = placeholder.get("subsections", {})
            if not isinstance(subsections, dict):
                raise StrictDataError(f"章节 {placeholder_id} 的 subsections 结构非法")
            for sub_id, sub_data in _sorted_section_items(subsections):
                if not isinstance(sub_data, dict):
                    raise StrictDataError(f"章节 {sub_id} 结构非法")
                if "replacement_pattern" in sub_data and "content" in sub_data:
                    paragraph_rules.append(
                        ParagraphReplaceRule(
                            key=sub_id,
                            anchor_text=sub_data["replacement_pattern"],
                            new_text=_require_content({"value": sub_data["content"]}, "value"),
                        )
                    )
                elif sub_data:
                    raise StrictDataError(f"章节 {sub_id} 需要明确配置 replacement_pattern，或被声明为动态章节")

    return BuildPlan(
        exact_replacements=tuple(exact_rules),
        paragraph_replacements=tuple(paragraph_rules),
        dynamic_sections=tuple(dynamic_rules),
        tables=tuple(table_rules),
    )
