import csv

def read_csv(file_path):
    """Reads a CSV file and returns the data as a list of dictionaries."""
    data = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return data

def process_data(data):
    """Processes the data by converting all values to uppercase."""
    for row in data:
        for key in row:
            row[key] = row[key].upper()
    return data

def write_csv(file_path, data):
    """Writes the processed data to a new CSV file."""
    if not data:
        print("No data to write.")
        return
    
    try:
        with open(file_path, mode='w', newline='') as file:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"An error occurred while writing the file: {e}")

def main():
    """Main function to execute the CSV processing."""
    input_file = 'input_data.csv'
    output_file = 'output_data.csv'
    
    # Step 1: Read the CSV file
    data = read_csv(input_file)
    
    if not data:
        print("No data found. Exiting...")
        return
    
    # Step 2: Process the data
    processed_data = process_data(data)
    
    # Step 3: Write the processed data to a new CSV file
    write_csv(output_file, processed_data)
    print(f"Data processing complete. Processed data written to {output_file}")

if __name__ == "__main__":
    main()

