from lxml import etree as ET


class XmlExporter:
    commands_roadmap = None

    def __init__(self, commands_roadmap):
        self.commands_roadmap = commands_roadmap

    def loadToFile(self, path):
        scenario_name = path.split('/')[-1].split('.')[0]
        root = ET.Element('scenario')
        root.set('name', scenario_name)
        for cmd in self.commands_roadmap:
            root.append(cmd.convertToXmlView())
        tree = ET.ElementTree(root)
        tree.write(path,
                   pretty_print = True,
                   xml_declaration = True,
                   encoding = "UTF-8",
                   doctype = '<!DOCTYPE scenario SYSTEM "sipp.dtd">')
