# Define the default target
all: result.csv

# Rule to download raw text and create download_raw_text.log
download_raw_text.log:
	@echo "Running the download script..."
	bash get_the_books.sh

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

# Rule to clean up the generated files
clean:
	@echo "Cleaning up..."
	rm -f download_raw_text.log clean_content.csv result.csv
	rm -f pg*.txt
	@echo "Cleanup complete."

# Phony targets to avoid conflicts with files of the same name
.PHONY: all clean

