#!/bin/bash

# List of book IDs
BOOK_IDS=(1064 10947 25525 1063 10031 17192 2151 51060 15143 32037)

# Base URL
BASE_URL="https://gutenberg.org/cache/epub"

# Download each book
for ID in "${BOOK_IDS[@]}"; do
  wget -O "pg${ID}.txt" "${BASE_URL}/${ID}/pg${ID}.txt"
done

# Log the number of downloaded files
echo "Counting downloaded files..." > download_raw_text.log
ls pg*.txt | wc -l >> download_raw_text.log
echo "Download complete."
