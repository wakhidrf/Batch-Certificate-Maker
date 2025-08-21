import csv

file1_path = "data.csv.2"
file2_path = "data.csv.bak"

def compare_csv_ignore_case(file1_path, file2_path):
    """
    Compares two CSV files, ignoring differences in capitalization.
    """
    with open(file1_path, 'r', newline='', encoding='utf-8') as file1, \
         open(file2_path, 'r', newline='', encoding='utf-8') as file2:
        reader1 = csv.reader(file1)
        reader2 = csv.reader(file2)

        is_same = True
        row_count = 0

        for row1, row2 in zip(reader1, reader2):
            row_count += 1
            if len(row1) != len(row2):
                print(f"Row {row_count}: Number of columns differ.")
                is_same = False
                continue

            for i in range(len(row1)):
                # Convert to lowercase for comparison
                if row1[i].lower() != row2[i].lower():
                    print(f"Row {row_count}, Column {i+1}: Values differ.")
                    print(f"  {file1_path}: '{row1[i]}'")
                    print(f"  {file2_path}: '{row2[i]}'")
                    is_same = False
        
        # Check if one file has more rows
        try:
            next(reader1)
            print(f"File '{file1_path}' has more rows.")
            is_same = False
        except StopIteration:
            pass
        
        try:
            next(reader2)
            print(f"File '{file2_path}' has more rows.")
            is_same = False
        except StopIteration:
            pass

    if is_same:
        print("The two files are identical (ignoring capitalization).")
    else:
        print("There are differences between the two files.")

# Run the comparison function
compare_csv_ignore_case(file1_path, file2_path)