from __future__ import annotations

from pathlib import Path

from docx import Document

from strict_word_filler.docx_ops import apply_plan
from strict_word_filler.loader import build_plan, load_json


BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = BASE_DIR / "[08]软件需求规格说明-438C.docx"
CONFIG_PATH = BASE_DIR / "config.json"
PROJECT_PATH = BASE_DIR / "project.json"
OUTPUT_PATH = BASE_DIR / "output" / "[08]软件需求规格说明-438C-project-copy.docx"


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
