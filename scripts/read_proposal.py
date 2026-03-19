import sys, pathlib
proposals = pathlib.Path(r'C:\Users\punch\Desktop\KnowledgeMapProject\textbook-modules\high-school-math\modules\proposals')
files = sorted(proposals.glob('*.md'))
if not files:
    print("No proposals found")
    sys.exit(1)
latest = files[-1]
print(f"=== {latest.name} ===\n")
sys.stdout.buffer.write(latest.read_text(encoding='utf-8').encode('utf-8', 'replace'))
