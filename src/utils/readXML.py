import xml.etree.ElementTree as ET

def read_xml(path:str)->ET.Element:
    """
    lê o arquivo xml e retorna o elemento root
    args:
        path: caminho do arquivo xml
    return
        elemento root
    """
    tree = ET.parse(path)
    root = tree.getroot()
    return root