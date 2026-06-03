import os
import glob
import shutil

for path in glob.glob('scratch-gui/build/*.html'):
  print(f'Patching HTML {path}')
  with open(path, 'r') as f:
    contents = f.read()
    # Sneaky GarboMuffin... I'll respect this for now.
    contents = contents.replace('</head>', '<meta name="robots" content="noindex"></head>')
  with open(path, 'w') as f:
    f.write(contents)

for path in glob.glob('scratch-gui/build/**/*.js', recursive=True):
  print(f'Patching JS {path}')
  with open(path, 'r') as f:
    contents = f.read()
    contents = contents.replace('https://trampoline.turbowarp.org', 'https://trampoline.turbowarp.xyz')
  with open(path, 'w') as f:
    f.write(contents)

# Yes, this is *very* disgusting, but this is just an archive.
fetchFile = glob.glob('scratch-gui/build/js/editor~embed~fullscreen~player.*.js')[0]
  print(f'Patching JS {path}')
  with open(fetchFile, 'r') as f:
    contents = f.read()
    contents = contents.replace('e=>{if("<"!==', 'e=>{if("\n"!==')
  with open(fetchFile, 'w') as f:
    f.write(contents)
