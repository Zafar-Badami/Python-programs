from pathlib import Path
path=Path()
for file in path.glob('c*.py'):
    print(file)
