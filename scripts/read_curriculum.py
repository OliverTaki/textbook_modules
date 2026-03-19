# -*- coding: utf-8 -*-
"""Extract math-relevant sections from Japan high school curriculum."""
import sys

path = r'C:\Users\punch\Desktop\KnowledgeMapProject\textbook-modules\curriculum-standards\japan\high\gakushu_shidoyoryo_ko_H30.txt'

with open(path, encoding='utf-8', errors='replace') as f:
    text = f.read()

lines = text.split('\n')
math_lines = []
in_math = False
count = 0
for line in lines:
    if not in_math and '数学' in line:
        in_math = True
    if in_math:
        math_lines.append(line)
        count += 1
    if count > 600:
        break

print(f"Total chars: {len(text)}")
print("="*60)
out = '\n'.join(math_lines[:600])
sys.stdout.buffer.write(out.encode('utf-8', 'replace'))
