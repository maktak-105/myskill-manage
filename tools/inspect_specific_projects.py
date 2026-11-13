import os
import glob

base_dir = r'~\source\project'
target_names = [
    'QuickFolderSize', 'QuickMarkPDF', 'QuickFileCopy', 'QuickDiskBench',
    'Quick7Zip', 'QuickImageView', 'QuickRightClick', 'QuickDiskRescue', 'QuickDock',
    'bunai-server', 'panzer-front', 'supplier-manage', 'ikusei-taikei-2026',
    'gleam', 'project-LLM', 'LLM-manage', 'fabric', 'camp', 'note', 'AI_mensetsu'
]

for name in target_names:
    p_path = os.path.join(base_dir, name)
    if not os.path.isdir(p_path):
        continue
    all_files = []
    for root, dirs, files in os.walk(p_path):
        # exclude git
        if '.git' in dirs: dirs.remove('.git')
        if 'node_modules' in dirs: dirs.remove('node_modules')
        if 'obj' in dirs: dirs.remove('obj')
        if 'bin' in dirs: dirs.remove('bin')
        for f in files:
            all_files.append(os.path.relpath(os.path.join(root, f), p_path))
    
    print(f"=== {name} ({len(all_files)} files) ===")
    sample = all_files[:10]
    for s in sample:
        print(f"  {s}")
    if len(all_files) > 10:
        print(f"  ... (+ {len(all_files) - 10} files)")
