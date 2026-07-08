from __future__ import annotations

import argparse
from pathlib import Path

from docx import Document

from .docx_ops import apply_plan
from .loader import build_plan, load_json


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Strict Word document filler")
    parser.add_argument("--template", required=True, help="Path to the source .docx template")
    parser.add_argument("--config", required=True, help="Path to config.json")
    parser.add_argument("--project", required=True, help="Path to project.json")
    parser.add_argument("--output", required=True, help="Path to the output .docx file")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    template_path = Path(args.template).resolve()
    config_path = Path(args.config).resolve()
    project_path = Path(args.project).resolve()
    output_path = Path(args.output).resolve()

    config_data = load_json(config_path)
    project_data = load_json(project_path)
    plan = build_plan(config_data, project_data)

    doc = Document(str(template_path))
    apply_plan(doc, plan)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(output_path))
    print(f"文档已生成: {output_path}")
    print("目录字段已标记为需要更新，首次在 Word 中打开时应刷新目录。")
    return 0
