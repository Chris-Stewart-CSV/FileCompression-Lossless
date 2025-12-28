import lzma
import os

def process_lzma_smart():
    raw_path = input("Enter the full path to your file: ").strip().strip('"')
    base_path, original_ext = os.path.splitext(raw_path)

    choice = input("Type 'C' to compress or 'D' to decompress: ").upper()

    if choice == 'C':
        if not os.path.exists(raw_path):
            print(f"Error: File '{raw_path}' not found.")
            return

        output_file = base_path + ".xz"
        print(f"Compressing {os.path.basename(raw_path)}...")
        
        try:
            with open(raw_path, 'rb') as f_in:
                data = f_in.read()
                
            with lzma.open(output_file, 'wb', preset=9) as f_out:
                # We write the extension (e.g., '.jpg') followed by a '|' separator
                # Then we write the actual image data
                header = (original_ext + "|").encode('utf-8')
                f_out.write(header + data)
            
            orig_size = os.path.getsize(raw_path) / 1024
            new_size = os.path.getsize(output_file) / 1024
            print(f"--- Success! Created: {os.path.basename(output_file)} ---")
            print(f"Reduced: {orig_size:.1f}KB -> {new_size:.1f}KB")
        except Exception as e:
            print(f"Error: {e}")

    elif choice == 'D':
        input_file = raw_path if raw_path.endswith('.xz') else raw_path + ".xz"
        if not os.path.exists(input_file):
            print(f"Error: File '{input_file}' not found.")
            return

        print("Decompressing and restoring original format...")
        try:
            with lzma.open(input_file, 'rb') as f_in:
                content = f_in.read()
                
            # Find the '|' separator we added earlier
            separator_index = content.find(b'|')
            if separator_index == -1:
                print("Error: This file wasn't compressed with the 'Smart' script.")
                return
            
            # Extract the extension and the data
            stored_ext = content[:separator_index].decode('utf-8')
            actual_data = content[separator_index + 1:]
            
            output_file = os.path.splitext(input_file)[0] + stored_ext
            
            with open(output_file, 'wb') as f_out:
                f_out.write(actual_data)
                
            print(f"--- Success! Restored to: {os.path.basename(output_file)} ---")
        except Exception as e:
            print(f"Error during decompression: {e}")

if __name__ == "__main__":
    process_lzma_smart()
