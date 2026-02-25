import os
import re

workspace_root = r'c:\Users\kkour\Documents\GitHub\experience-manager-cloud-service.en'
assets_dir = os.path.join(workspace_root, 'help', 'assets')
src_file = os.path.join(assets_dir, 'toc-assets.md')
dst_file = os.path.join(assets_dir, 'TOC.md')
bak_file = os.path.join(assets_dir, 'toc-assets.md.bak')

# Read source
with open(src_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Adjust links
# Replace /help/assets/ with empty string
# This assumes all links are like /help/assets/...
# We should be careful not to replace text that is not a link, but the pattern is specific enough usually.
# Better to use regex to target links specifically if possible, but global replace of /help/assets/ in a TOC file is likely safe for paths.
# However, let's be safer and target ](/help/assets/
new_content = content.replace('](/help/assets/', '](')

# Write TOC.md
with open(dst_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

# Rename original to .bak so it's not processed as an orphan
if os.path.exists(src_file):
    os.rename(src_file, bak_file)

print(f"Created {dst_file} and renamed source to {bak_file}")
