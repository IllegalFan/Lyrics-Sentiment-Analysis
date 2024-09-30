import json
import csv
import os


def json_to_csv(folder_path, output_csv):
    # Create a CSV file and open it for writing
    with open(output_csv, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['year', 'title', 'artist', 'lyrics','rank'])
        # Loop through all files in the folder
        for filename in os.listdir(folder_path):
            # Check if the file is a JSON file
            if filename.endswith('.json'):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r') as f:
                    data = json.load(f)

                    # Iterate through the key-value pairs in the JSON
                    first_key = next(iter(data),None)
                    if first_key != None:
                        songs = data[first_key]
                        for song in songs:
                            row = []
                            row.append(first_key)
                            for key,value in song.items():
                                row.append(value)
                            writer.writerow(row)
                    else:
                        continue

if __name__ == "__main__":
    # Folder containing JSON files
    folder_path = 'Hot_100_06_01'  # Path to your folder

    # Output CSV file
    output_csv = 'output_summer.csv'

    # Call the function to convert JSON files to CSV
    json_to_csv(folder_path, output_csv)

    print(f"CSV file '{output_csv}' created successfully from JSON files in '{folder_path}'!")
