import xml.etree.ElementTree as ET
from xml.dom import minidom


class XmlExporter:
    commands_roadmap = None

    def __init__(self, commands_roadmap):
        self.commands_roadmap = commands_roadmap

    def __prettify(self, elem):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = ET.tostring(elem)
        doc = minidom.parseString(rough_string)
        dt = minidom.getDOMImplementation('').createDocumentType('scenario', '', 'sipp.dtd')
        doc.insertBefore(dt, doc.documentElement)
        return doc.toprettyxml(indent = "  ", encoding = 'ISO-8859-1').decode('utf-8')

    def loadToFile(self, path):
        root = ET.Element('scenario')
        root.set('name', 'test1')
        for cmd in self.commands_roadmap:
            root.append(cmd.convertToXmlView())
        with open(path, 'w') as f:
            f.write(self.__prettify(root))

