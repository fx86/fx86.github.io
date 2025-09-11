#!/bin/bash

# Define pairs of directories where we want to keep the first one
PAIRS=(
  "a-checklist-for-debugging-cronjobs debugging-cronjobs"
)

POSTS_DIR="/Users/fibinse/fx86/fx86.github.io/new-quarto-blog/posts"

for PAIR in "${PAIRS[@]}"; do
  read -r KEEP REMOVE <<< "$PAIR"
  
  if [ -d "$POSTS_DIR/$KEEP" ] && [ -d "$POSTS_DIR/$REMOVE" ]; then
    echo "Keeping $KEEP, removing $REMOVE"
    rm -rf "$POSTS_DIR/$REMOVE"
  else
    echo "One of the directories does not exist: $KEEP or $REMOVE"
  fi
done

echo "Cleanup complete!"
