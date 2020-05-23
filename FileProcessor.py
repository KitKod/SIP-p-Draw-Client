import xml.etree.ElementTree as ET


class XmlExporter:
    commands_roadmap = None

    def __init__(self, commands_roadmap):
        self.commands_roadmap = commands_roadmap

    def loadToFile(self, path):
        root = ET.Element('scenario')
        root.set('name', 'test1')

        for cmd in self.commands_roadmap:
            root.append(cmd.convertToXmlView())

        with open(path, 'wb') as f:
            f.write('<?xml version="1.0" encoding="UTF-8" ?>\n<!DOCTYPE tmx SYSTEM "tmx14a.dtd">'.encode('utf8'))
            # tree = ET.ElementTree(root)
            # tree.write(f, 'utf-8')
            f.write(ET.tostring(root))

