from __future__ import annotations

from pathlib import Path

from docx import Document

from strict_word_filler.docx_ops import apply_plan
from strict_word_filler.loader import build_plan, load_json


BASE_DIR = Path(__file__).resolve().parent
SKILL_DIR = BASE_DIR.parent
TEMPLATE_PATH = SKILL_DIR / "documents" / "[10][SRS] 软件需求规格说明-438C-2021.docx"
CONFIG_PATH = SKILL_DIR / "templates" / "config.json"
PROJECT_PATH = SKILL_DIR / "templates" / "project.json"
OUTPUT_PATH = BASE_DIR / "output" / "[10][SRS] 软件需求规格说明-438C-2021-filled.docx"


def main() -> int:
    config_data = load_json(CONFIG_PATH)
    project_data = load_json(PROJECT_PATH)
    plan = build_plan(config_data, project_data)

    doc = Document(str(TEMPLATE_PATH))
    apply_plan(doc, plan)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(OUTPUT_PATH))
    print(f"文档已生成: {OUTPUT_PATH}")
    print("目录字段已标记为需要更新，首次在 Word 中打开时应刷新目录。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
