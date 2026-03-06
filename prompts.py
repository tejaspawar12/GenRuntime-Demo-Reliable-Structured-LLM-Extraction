def build_resume_extraction_prompt(document_text: str) -> str:
    return f"""
You are an information extraction system.

Task:
Extract resume information into JSON that matches this EXACT structure:
- name (string, required)
- email (string or null)
- phone (string or null)
- linkedin (string or null)
- github (string or null)
- skills (array of strings)
- education (array of strings)
- experience (array of strings)
- projects (array of strings)

Rules:
- Output ONLY JSON. No markdown. No extra commentary.
- If a field is not present, return null (for single values) or [] (for lists).
- Keep items concise.
- Do not invent data.

RESUME TEXT:
\"\"\"{document_text}\"\"\"
""".strip()