import sys

input_file = str(sys.argv[1])
output_file = str(sys.argv[2])

indent_depth = ""

# Boilerplate
html = "<!DOCTYPE html>\n"
html += "<html>\n"
indent_depth += "\t"
html += indent_depth + "<head>\n"
indent_depth += "\t"
html += indent_depth + "<link rel=\"stylesheet\" type=\"text/css\" href=\"./theme.css\" />\n" #Adding Stylesheet
html += indent_depth + "<title> "
html += input_file #Adding Title
html += " </title>\n"
indent_depth = indent_depth.replace("\t", "", 1)
html += indent_depth + "</head>\n"


#Body
html += indent_depth + "<body>\n"
indent_depth += "\t"

with open(input_file, "r") as f:
    md = f.read()

lines = md.split("\n")
for line in lines:
    if line.startswith("#"):
        level = line.count("#")
        content = line[level+1:]
        imageEnd = content
        while content.count("![") > 0:
            preText = content[:imageEnd.find("![")]

            imageEnd = imageEnd[imageEnd.find("![")+2:]
            imageName = imageEnd[:imageEnd.find("](")]
            imageEnd = imageEnd[imageEnd.find("](")+2:]
            imageSrc = imageEnd[:imageEnd.find(")")]
            imageEnd = imageEnd[imageEnd.find(")")+1:]
            
            content = preText + f"<img src = \"{imageSrc}\" alt=\"{imageName}\"/>" + imageEnd
            
        html += indent_depth + f"<h{level}>{content}</h{level}>\n"
    else:
        if(line == ""):
            html+= indent_depth + "<br>\n"
        else:
            html += indent_depth + f"<p>{line}</p>\n"

indent_depth = indent_depth.replace("\t", "", 1)
html += indent_depth + "</body>\n"
html += "</html>"

# Write the output to a file
with open(output_file, "w") as f:
    f.write(html)

#print(html)