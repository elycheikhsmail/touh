import re
import csv

def extract_and_merge_tables(input_filename="merged.txt", output_filename="tables.csv"):
    """
    Extracts data from multiple tables in a text file and merges them into a CSV file.

    Args:
        input_filename (str): The name of the input text file.
        output_filename (str): The name of the output CSV file.
    """
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w', newline='') as outfile:
            csv_writer = csv.writer(outfile)
            csv_writer.writerow(['x', 'y', 'tableIndex'])  # Write CSV header

            current_table_index = None
            data_started = False
            for line in infile:
                header_match = re.match(r'\s+Frequency / GHz\s+S1,1 \((\d+)\)/abs,dB', line)
                if header_match:
                    current_table_index = int(header_match.group(1))
                    data_started = False
                elif line.strip() == '----------------------------------------------------------------------':
                    data_started = True
                elif data_started and line.strip():
                    try:
                        x_str, y_str = line.strip().split()
                        x = float(x_str)
                        y = float(y_str)
                        csv_writer.writerow([x, y, current_table_index])
                    except ValueError:
                        # Handle potential errors in data lines
                        print(f"Skipping invalid data line: {line.strip()}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    extract_and_merge_tables()
    print("Data extraction and merging complete. The results are saved in tables.csv")