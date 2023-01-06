import xml.etree.ElementTree as ET
def write_xml_from_element_list(fileNameWithPath:str, lista:list, rootElementName:str):
    rootOut = ET.Element(rootElementName)
    for item in lista:
        rootOut.append(item)
    newtree = ET.ElementTree(rootOut)
    newtree.write(fileNameWithPath)