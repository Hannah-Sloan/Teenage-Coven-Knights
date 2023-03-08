import sys

def replaceLineWithImages(content):
    imageEnd = content
    while content.count("![") > 0:
        preText = content[:content.find("![")]

        imageEnd = imageEnd[imageEnd.find("![")+2:]
        imageName = imageEnd[:imageEnd.find("](")]
        imageEnd = imageEnd[imageEnd.find("](")+2:]
        imageSrc = imageEnd[:imageEnd.find(")")]
        imageEnd = imageEnd[imageEnd.find(")")+1:]
        
        content = preText + f"<img src = \"{imageSrc}\" alt=\"{imageName}\"/>" + imageEnd
    return content

def replaceLineWithLinks(content):
    linkEnd = content
    while content.count("[") > 0:
        preText = content[:content.find("[")]

        linkEnd = linkEnd[linkEnd.find("[")+1:]
        linkName = linkEnd[:linkEnd.find("](")]
        linkEnd = linkEnd[linkEnd.find("](")+2:]
        linkSrc = linkEnd[:linkEnd.find(")")]
        linkEnd = linkEnd[linkEnd.find(")")+1:]

        content = preText + f"<p><a href=\"{linkSrc}\">{linkName}</a></p>" + linkEnd
    return content

def replaceLineWithBold(content):
    boldEnd = content
    while content.count("**") > 0:
        preText = content[:content.find("**")]

        boldEnd = boldEnd[boldEnd.find("**")+2:]
        boldText = boldEnd[:boldEnd.find("**")]
        boldEnd = boldEnd[boldEnd.find("**")+2:]

        content = preText + f"<b>{boldText}</b>" + boldEnd
    return content

def replaceLineWithItalic(content):
    italicEnd = content
    while content.count("*") > 0:
        preText = content[:content.find("*")]

        italicEnd = italicEnd[italicEnd.find("*")+1:]
        italicText = italicEnd[:italicEnd.find("*")]
        italicEnd = italicEnd[italicEnd.find("*")+1:]

        content = preText + f"<em>{italicText}</em>" + italicEnd
    return content

input_file = str(sys.argv[1])
output_file = str(sys.argv[2])

indent_depth = ""

# Boilerplate
html = "<!DOCTYPE html>\n"
html += "<html>\n"
indent_depth += "\t"
html += indent_depth + "<head>\n"
indent_depth += "\t"
html += indent_depth + "<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\" />\n" #Adding Stylesheet
# html += indent_depth + "<link rel=\"shortcut icon\" href=\"img/moon.ico\" type=\"image/x-icon\"/>\n" #Adding Favicon
html += indent_depth + "<link rel=\"shortcut icon\" href=\"https://raw.githubusercontent.com/Hannah-Sloan/Teenage-Coven-Knights/master/docs/img/moon.ico\" type=\"image/x-icon\"/>\n" #Adding Favicon
html += indent_depth + "<link rel=\"icon\" href=\"https://raw.githubusercontent.com/Hannah-Sloan/Teenage-Coven-Knights/master/docs/img/moon.ico\" type=\"image/x-icon\"/>\n"
html += indent_depth + "<title> "
if((input_file[:len(input_file)-3]) == "index"): #Adding Title
    html += "Home - Teenage Coven Knights" 
else:
    title = (input_file[:len(input_file)-3])
    title = title.replace("_", " ")
    title = title.upper()
    html += title + " - Teenage Coven Knights"
html += " </title>\n"
indent_depth = indent_depth.replace("\t", "", 1)
html += indent_depth + "</head>\n"


#Body
html += indent_depth + "<body>\n"
indent_depth += "\t"

html += indent_depth + f"<p><a href=\"https://github.com/Hannah-Sloan/Teenage-Coven-Knights\">GITHUB</a>\n"
html += indent_depth + f"<a href=\"index.html\">HOME</a></p>\n"

with open(f"markdown\{input_file}", "r") as f:
    md = f.read()

counter = 0

header_depth = 1

def header_indent(header_depth_in):
  return "\t"*(header_depth_in-1)

lines = md.split("\n")
for line in lines:
    if line.startswith("#"):
        level = line.count("#")
        header_depth = level
        content = line[level+1:]
        content = replaceLineWithImages(content)
        content = replaceLineWithLinks(content)
        content = replaceLineWithBold(content)
        content = replaceLineWithItalic(content)

        html += indent_depth + header_indent(level) + f"<h{level}>{content}</h{level}>\n"
    else:
        if(line != ""):
            line = replaceLineWithImages(line)
            line = replaceLineWithLinks(line)
            line = replaceLineWithBold(line)
            line = replaceLineWithItalic(line)

            html += indent_depth + header_indent(header_depth+1) + f"<p>{line}</p>\n"

indent_depth = indent_depth.replace("\t", "", 1)
html += indent_depth + "</body>\n"
html += "</html>"

# Write the output to a file
with open(f"docs\{output_file}", "w") as f:
    f.write(html)