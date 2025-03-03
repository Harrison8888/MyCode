import xml.etree.ElementTree as ET

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return [elem.tag for elem in root.iter()]

# 示例调用
print(parse_xml("example.xml"))
