import os 
import re

DATA_DICTIONARY_FILE_PATH = r"..\data\schema\cps\cps_data_dictionary.txt"
DATA_DICTIONARY_OUTPUT_CSV_PATH = r"..\data\schema\cps\cps_data_dictionary.csv"
DATA_DICTIONARY_FIELDS_DIR_PATH = r"..\data\schema\cps\fields"

output_list = []

with open(os.path.join(os.path.dirname(__file__), DATA_DICTIONARY_FILE_PATH), "r") as f:
    lines = f.readlines()

is_start_of_field = False
groups = None

for line in lines[15:4151]:
    t_line = line.strip()

    if t_line == "A3.  PERSONS INFORMATION DEMOGRAPHIC ITEMS":
        continue
    if t_line == "PERSON'S WEIGHTS":
        continue


    
    if t_line == "FILLER            1":
        col_pos = int(groups["columns"].split("-")[1].strip()) + 1
        t_line = f"FILLER 1 {col_pos}-{col_pos}"

    # if first character is an actual character, then it's the start of a field 
    if line[0].isalpha() and line[:5] != "NOTE:":
        is_start_of_field = True
        # normalize whitespace to a single space
        t_line = re.sub(r"\s+", " ", t_line)
        print(t_line)

        # append the previous group if it exists
        if groups:
            output_list.append(groups)

        # handle the special case of FILLER fields
        if t_line[:6] == "FILLER" or t_line[:7] == "PADDING":
            t_line = t_line.replace("PADDING", "FILLER")
            groups = {
                "field": "FILLER",
                "size": re.match(r"FILLER\s(?P<size>\d+)\s", t_line).group("size"),
                "desc": "FILLER",
                "columns": re.match(r".*(?P<columns>\d+\s?-\s?\d+$)", t_line).group("columns"),
                "content": []
            }
            groups["columns"] = groups["columns"].replace(" ", "")
            continue

        groups = re.match(r"(?P<field>^\w+)\s(?P<size>\d+)\s(?P<desc>.+)\s(?P<columns>\d+\s?-\s?\d+$)", t_line).groupdict()
        groups["content"] = []
        groups["columns"] = groups["columns"].replace(" ", "")
        continue
    
    # if the line starts with whitespace and is not empty, then it's a continuation of the description
    if is_start_of_field and t_line != "":
        t_line = re.sub(r"\s+", " ", t_line)
        groups["desc"] += " " + t_line
        continue
    
    # if the line is empty, then it's the end of the field description
    if is_start_of_field:
        is_start_of_field = False

    groups["content"].append(t_line)

# append the last group if it exists
if groups:
    output_list.append(groups)
    
with open(os.path.join(os.path.dirname(__file__), DATA_DICTIONARY_OUTPUT_CSV_PATH), "w") as f:
    f.write("field,size,desc,columns\n")
    for item in output_list:
        f.write(f'"{item["field"]}","{item["size"]}","{item["desc"]}","{item["columns"]}"\n')

# write each field to its own text file
for field in output_list:
    field_name = field["field"]
    field_file_path = os.path.join(os.path.dirname(__file__), DATA_DICTIONARY_FIELDS_DIR_PATH, f"{field_name}.txt")
    with open(field_file_path, "w") as f:
        f.write(f"Field: {field['field']}\n")
        f.write(f"Size: {field['size']}\n")
        f.write(f"Description: {field['desc']}\n")
        f.write(f"Columns: {field['columns']}\n")
        f.write("Content:\n")
        for content_line in field["content"]:
            f.write(f"{content_line}\n")