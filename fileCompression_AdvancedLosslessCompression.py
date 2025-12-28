import lzma
import os

def process_lzma():
    file_path = input("Enter the full path to your file: ").strip().strip('"')
    
    if not os.path.exists(file_path) and not os.path.exists(file_path + ".xz"):
        print(f"Error: Could not find the file.")
        return

    choice = input("Type 'C' to compress (LZMA) or 'D' to decompress: ").upper()

    if choice == 'C':
        output_file = file_path + ".xz"
        print("Compressing using LZMA (Level 9)... this may take a moment.")
        try:
            with open(file_path, 'rb') as f_in:
                # preset=9 is the maximum compression level
                with lzma.open(output_file, 'wb', preset=9) as f_out:
                    f_out.write(f_in.read())
            
            orig_size = os.path.getsize(file_path) // 1024
            new_size = os.path.getsize(output_file) // 1024
            print(f"--- Success! ---")
            print(f"Original: {orig_size} KB | Compressed: {new_size} KB")
        except Exception as e:
            print(f"Error: {e}")

    elif choice == 'D':
        # Ensure we are looking for the .xz file
        input_file = file_path if file_path.endswith('.xz') else file_path + ".xz"
        # Remove .xz for the output name
        output_file = input_file.replace('.xz', '')
        
        print("Decompressing...")
        try:
            with lzma.open(input_file, 'rb') as f_in:
                with open(output_file, 'wb') as f_out:
                    f_out.write(f_in.read())
            print(f"--- Success! Restored to: {output_file} ---")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    process_lzma()