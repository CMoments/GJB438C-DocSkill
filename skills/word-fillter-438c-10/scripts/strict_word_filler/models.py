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
class CSCISectionItem:
    section_id: str
    title: str
    overview: str
    component_title: str
    component_design: str
    execution_plan: str
    interface_overview: str
    interface_identification: str
    interface_detail_title: str
    interface_details: str


@dataclass(frozen=True)
class CSCISectionRule:
    key: str
    summary_anchor: str
    end_before_title: str
    prototype_title_anchor: str
    overview_heading_anchor: str
    component_section_heading_anchor: str
    component_item_heading_anchor: str
    component_body_anchor: str
    execution_heading_anchor: str
    execution_body_anchor: str
    interface_heading_anchor: str
    interface_id_heading_anchor: str
    interface_id_body_anchor: str
    interface_detail_heading_anchor: str
    interface_detail_body_anchor: str
    items: tuple[CSCISectionItem, ...]


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
    csci_sections: tuple[CSCISectionRule, ...]
    tables: tuple[TableFillRule, ...]
