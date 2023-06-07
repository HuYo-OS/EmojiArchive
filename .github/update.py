import json
from pathlib import Path

root_path = Path(__file__).parent.parent.resolve()
ignored_dirs = {'.github', '.git', '准备中2', 'node_modules'}
ignored_files = {'info.json'}

image_extensions = ['.png', '.jpg', '.jpeg', '.gif']

def process_directory(directory):
    items = []
    for file in directory.iterdir():
        if file.is_file() and file.suffix.lower() in image_extensions and file.name not in ignored_files:
            items.append(str(file.name))

    if items:
        directory_name = directory.name
        icon_name = f"{directory_name}.png"
        info = {
            'name': directory_name,
            'icon': icon_name,
            'items': items
        }
        info_json_path = directory / 'info.json'
        with open(info_json_path, 'w', encoding='utf-8') as file:
            json.dump(info, file, ensure_ascii=False, indent=2)

    for subdirectory in directory.iterdir():
        if subdirectory.is_dir() and subdirectory.name not in ignored_dirs:
            process_directory(subdirectory)

process_directory(root_path)
