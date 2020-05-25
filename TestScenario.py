from PySide2.QtGui import QColor
from lxml import etree as ET

from models.SIPpCommands import SendCommand, RecvCommand, NopCommand, PauseCommand
from models.TableBlock import TableBlock
from SippDrawConf import getMUI, SippDrawConf


class TestScenario:
    commands_roadmap = None

    name = None
    path_to_file = None
    saved = True

    def __init__(self, from_file = None):
        if from_file is not None:
            self.loadFromFile(from_file)
            self.path_to_file = from_file
            self.name = from_file.split('/')[-1].split('.')[0]
        else:
            self.name = 'new_sip_p_draw.xml'
        # self.commands_roadmap = commands_roadmap

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

    def loadFromFile(self):
        tree = ET.parse(self.path_to_file)
        root = tree.getroot()
        cmds_roadmap = []

        for elemn in root:
            print(elemn.tag, ' ', elemn.attrib, ' ', elemn.text)
            command_name = elemn.tag
            command = None
            if command_name == 'send':
                command = SendCommand(elemn)
            elif command_name == 'recv':
                command = RecvCommand(elemn)
            elif command_name == 'pause':
                command = PauseCommand(elemn)
            elif command_name == 'nop':
                command = NopCommand(elemn)

            cmds_roadmap.append(command)

        ui = getMUI()
        for command in cmds_roadmap:
            insert_to_row = ui.table_constructor.rowCount()
            insert_to_column = None
            ui.table_constructor.insertRow(insert_to_row)

            block_name = 'EmptyCMD'
            if isinstance(command, SendCommand):
                color = 'green'
                insert_to_column = SippDrawConf.SEND_CMD_COLUMN
                if command.content:
                    block_name = command.content.strip().split(' ', 1)[0]
                else:
                    block_name = 'NotConfig'
            elif isinstance(command, RecvCommand):
                color = 'red'
                insert_to_column = SippDrawConf.RECV_CMD_COLUMN
                if command.response >= 0:
                    block_name = command.response
                elif command.request != '-':
                    block_name = command.request
                else:
                    block_name = 'NotConfig'

            block = TableBlock(block_name, command)
            block.setBackgroundColor(QColor(color))
            ui.table_constructor.setItem(insert_to_row, insert_to_column, block)

