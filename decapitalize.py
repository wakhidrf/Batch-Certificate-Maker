import csv

input_file = "data.csv.bak"
output_file = "data.csv"

def title_case_with_apostrophe(s):
    # Split the string by spaces
    words = s.split(' ')
    result_words = []
    for word in words:
        # Handle words with an apostrophe
        if "'" in word:
            parts = word.split("'")
            if len(parts) > 1:
                # Capitalize the first part
                first_part = parts[0].capitalize()
                # Re-join with the apostrophe and the second part in lowercase
                result_words.append(f"{first_part}'{parts[1].lower()}")
            else:
                # If there is only an apostrophe with no text after it
                result_words.append(word.capitalize())
        else:
            # Handle normal words without an apostrophe
            result_words.append(word.capitalize())
    # Join the words back into a string
    return ' '.join(result_words)

with open(input_file, newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    for row in reader:
        if len(row) >= 2:
            row[1] = title_case_with_apostrophe(row[1])
        writer.writerow(row)