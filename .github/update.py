import json
from pathlib import Path


root_path = Path(__file__).parent.parent.resolve()
ignored_dirs = {'.github', '.git', '准备中2', 'node_modules'}
ignored_files = {'info.json'}

path_data = {
    dir.name: {
        file.stem: str(file.relative_to(root_path))
            .replace('\\', '/')
        for file in dir.rglob('*')
            if (file.is_file() and file.name not in ignored_files
                and not any(p.name.startswith('.')
                or p.name in ignored_dirs for p in file.parents))
    }
    for dir in root_path.iterdir()
        if dir.is_dir() and dir.name not in ignored_dirs
}

with open(root_path / 'path.json', 'w', encoding='utf-8') as file:
    json.dump(
        path_data,
        file,
        ensure_ascii=False,
        indent=2
    )
