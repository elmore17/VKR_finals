import json
from docx import Document
from docxtpl import DocxTemplate


def read_docx(docx_path, items_per_subarray=142):
    doc = Document(docx_path)
    all_text_list = []

    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                text = cell.text.strip()
                if text:
                    all_text_list.append(text)

    divided_data = [all_text_list[i:i + items_per_subarray] for i in range(0, len(all_text_list), items_per_subarray)]

    return divided_data