#!/usr/bin/env python3

import os
import re
import shutil
from datetime import datetime
import yaml

def slugify(text):
    """Convert a string to a URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content"""
    match = re.match(r'^---\s*(.*?)\s*---\s*(.*)', content, re.DOTALL)
    if match:
        frontmatter_yaml = match.group(1)
        content = match.group(2)
        try:
            frontmatter = yaml.safe_load(frontmatter_yaml)
            return frontmatter, content.strip()
        except yaml.YAMLError:
            print(f"Error parsing YAML frontmatter")
            return {}, content
    return {}, content

def convert_jekyll_to_quarto(jekyll_path, quarto_path):
    """Convert Jekyll post to Quarto format"""
    # Get list of Jekyll posts
    jekyll_posts_dir = os.path.join(jekyll_path, "_posts")
    quarto_posts_dir = os.path.join(quarto_path, "posts")
    
    # Ensure quarto posts directory exists
    os.makedirs(quarto_posts_dir, exist_ok=True)
    
    # Process each Jekyll post
    for filename in os.listdir(jekyll_posts_dir):
        if not (filename.endswith('.md') or filename.endswith('.markdown')):
            continue
            
        # Extract date and title from filename
        match = re.match(r'(\d{4}-\d{2}-\d{2})-(.*)\.(md|markdown)$', filename)
        if not match:
            print(f"Skipping {filename}, doesn't match expected format")
            continue
            
        date_str, title_with_ext, ext = match.groups()
        title = title_with_ext.replace('-', ' ')
        
        # Read Jekyll post content
        with open(os.path.join(jekyll_posts_dir, filename), 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter and content
        frontmatter, post_content = extract_frontmatter(content)
        
        # Create new Quarto frontmatter
        new_frontmatter = {
            'title': frontmatter.get('title', title),
            'description': frontmatter.get('excerpt', ''),
            'date': date_str,
            'categories': frontmatter.get('categories', []),
            'tags': frontmatter.get('tags', [])
        }
        
        # Create slug for directory name
        slug = slugify(title_with_ext)
        post_dir = os.path.join(quarto_posts_dir, slug)
        os.makedirs(post_dir, exist_ok=True)
        
        # Create Quarto post content
        quarto_content = '---\n'
        quarto_content += yaml.dump(new_frontmatter, default_flow_style=False)
        quarto_content += '---\n\n'
        quarto_content += post_content
        
        # Write Quarto post
        with open(os.path.join(post_dir, 'index.qmd'), 'w', encoding='utf-8') as f:
            f.write(quarto_content)
        
        print(f"Converted: {filename} -> posts/{slug}/index.qmd")

if __name__ == "__main__":
    jekyll_path = "/Users/fibinse/fx86/fx86.github.io"
    quarto_path = "/Users/fibinse/fx86/fx86.github.io/new-quarto-blog"
    convert_jekyll_to_quarto(jekyll_path, quarto_path)
    print("Migration completed!")
