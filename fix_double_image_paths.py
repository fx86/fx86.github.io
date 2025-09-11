#!/usr/bin/env python
import os
import glob
import re

# Directory containing the posts
posts_dir = '/Users/fibinse/fx86/fx86.github.io/new-quarto-blog/posts'

# Find all qmd files
qmd_files = glob.glob(f'{posts_dir}/**/index.qmd', recursive=True)

for qmd_file in qmd_files:
    print(f"Processing {qmd_file}...")
    
    # Read file content
    with open(qmd_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix image paths with double assets/images
    content = re.sub(r'/assets/images/assets/images/', r'/assets/images/', content)
    
    # Write back to file
    with open(qmd_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {qmd_file}")

print("Image path fixing completed.")
