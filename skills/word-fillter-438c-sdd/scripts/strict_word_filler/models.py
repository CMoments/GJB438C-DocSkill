from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ExactReplaceRule:
    key: str
    old_text: str
    new_text: str
    expected_matches: int


@dataclass(frozen=True)
class ParagraphReplaceRule:
    key: str
    anchor_text: str
    new_text: str
    expected_matches: int = 1


@dataclass(frozen=True)
class DynamicSectionItem:
    section_id: str
    title: str
    body: str


@dataclass(frozen=True)
class DynamicSectionRule:
    parent_id: str
    parent_title: str
    summary_anchor: str
    end_before_title: str
    prototype_title_anchor: str
    prototype_body_anchor: str
    cleanup_anchors: tuple[str, ...]
    cleanup_to_end: bool
    items: tuple[DynamicSectionItem, ...]
    summary_text: str


@dataclass(frozen=True)
class TableFillRule:
    key: str
    locator_rows: tuple[tuple[str, ...], ...]
    columns: tuple[str, ...]
    rows: tuple[tuple[str, ...], ...]
    data_start_row: int
    preserve_tail_rows: int


@dataclass(frozen=True)
class BuildPlan:
    exact_replacements: tuple[ExactReplaceRule, ...]
    paragraph_replacements: tuple[ParagraphReplaceRule, ...]
    dynamic_sections: tuple[DynamicSectionRule, ...]
    tables: tuple[TableFillRule, ...]
