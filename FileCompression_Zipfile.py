import zipfile
import os

def process_file():
    file_path = input("Enter the full path to your file: ").strip().strip('"')
    
    if not os.path.exists(file_path) and not os.path.exists(file_path + ".zip"):
        print(f"Error: Could not find the file at {file_path}")
        return

    choice = input("Type 'C' to compress or 'D' to decompress: ").upper()

    # Get the base path without the extension (e.g., "image")
    base_path, extension = os.path.splitext(file_path)

    if choice == 'C':
        # Now creates "image.zip" instead of "image.jpg.zip"
        zip_path = base_path + ".zip"
        try:
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(file_path, os.path.basename(file_path))
            print(f"--- Success! Created: {zip_path} ---")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif choice == 'D':
        # Logic to handle both "image.zip" or "image.jpg.zip"
        zip_path = file_path if file_path.endswith('.zip') else file_path + ".zip"
        
        extract_to = os.path.dirname(zip_path)
        try:
            with zipfile.ZipFile(zip_path, 'r') as zipf:
                zipf.extractall(extract_to)
            print(f"--- Success! Extracted to: {extract_to} ---")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    process_file()
