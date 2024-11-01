def generate_snippets_array(file_path):
    snippets = []
    with open(file_path, 'r') as file:
        content = file.read()
        for char in content:
            if char == '\n':
                snippets.append('"`n"')
            elif char == '"':
                snippets.append('"`""')
            elif char == '`':
                snippets.append('"``"')
            else:
                snippets.append(f'"{char}"') 

    ahk_snippets_array = f"Snippets := [{', '.join(snippets)}]"
    
    with open("snippets_output.txt", "w") as output_file:
        output_file.write(ahk_snippets_array)
    print("Snippets array generated successfully! Check snippets_output.txt")

generate_snippets_array("your_code_file.py")
