from pdfminer.high_level import extract_text
import language_tool_python

file_path = '/Users/sunchenge/Desktop/apply/CV/myAwesomeCV/examples/cv.pdf'
output_file_path = './output.txt'
text = extract_text(file_path)

tool = language_tool_python.LanguageTool('en-GB')
matches = tool.check(text)

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for match in matches:
        output_file.write(str(match) + '\n')