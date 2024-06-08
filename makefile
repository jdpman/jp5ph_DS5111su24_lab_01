default:
	@cat makefile

# Define the default target
all: result.csv

# Rule to download raw text and create download_raw_text.log
download_raw_text.log:
	@echo "Running the download script..."
	bash get_the_books.sh
	@echo "Download complete."

# Rule to clean the content and create clean_content.csv
clean_content.csv: download_raw_text.log
	@echo "Cleaning content..."
	# Replace the following line with your actual text cleaning commands
	# Example cleaning command: concatenating files, removing newlines, sorting, and making unique entries
	cat pg*.txt | tr -d '\r\n' | tr ' ' '\n' | sort | uniq > clean_content.csv
	@echo "Cleaning complete."

# Rule to run the model and store results in result.csv
result.csv: clean_content.csv
	@echo "Running model..."
	# Replace the following line with your actual model running command
	# Example shell command to process the cleaned content
	# For illustration: simply counting the number of lines and words as a placeholder for a model
	wc -l clean_content.csv > result.csv
	wc -w clean_content.csv >> result.csv
	@echo "Model run complete."

# Rule to count the number of lines in The Raven
raven_line_count:
	@echo "Counting lines in The Raven (pg17192.txt)..."
	wc -l pg17192.txt

# Rule to count the number of words in The Raven
raven_word_count:
	@echo "Counting words in The Raven (pg17192.txt)..."
	wc -w pg17192.txt

# Rule to count the number of lines in The Raven that contain the word 'raven'
raven_counts:
	@echo "Counting lines with 'raven' (case-sensitive and case-insensitive) in The Raven (pg17192.txt)..."
	@echo "raven (lowercase):"
	grep -c 'raven' pg17192.txt
	@echo "Raven (title case):"
	grep -c 'Raven' pg17192.txt
	@echo "raven (case-insensitive):"
	grep -i -c 'raven' pg17192.txt

# Rule to count the total number of lines in all downloaded files
total_lines:
	@echo "Counting total lines in all downloaded files..."
	wc -l *.txt | tail -n 1

# Rule to count the total number of words in all downloaded files
total_words:
	@echo "Counting total words in all downloaded files..."
	wc -w *.txt | tail -n 1

# Rule to clean up the generated files
clean:
	@echo "Cleaning up..."
	rm -f download_raw_text.log clean_content.csv result.csv
	rm -f pg*.txt
	@echo "Cleanup complete."

# Phony targets to avoid conflicts with files of the same name
.PHONY: all clean raven_line_count raven_word_count raven_counts total_lines total_words

