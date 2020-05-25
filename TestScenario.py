from PySide2.QtGui import QColor
from lxml import etree as ET

from models.SIPpCommands import SendCommand, RecvCommand, NopCommand, PauseCommand
from models.TableBlock import TableBlock
from SippDrawConf import getMUI, SippDrawConf


class TestScenario:
    name = None
    path_to_file = None
    saved = True

    def __init__(self, from_file = None):
        if from_file is not None:
            self.path_to_file = from_file
            self.name = from_file.split('/')[-1]
            self.loadFromFile()
        else:
            self.name = 'new_sip_p_draw.xml'

    def loadToFile(self):
        scenario_name = self.path_to_file.split('/')[-1].split('.')[0]
        root = ET.Element('scenario')
        root.set('name', scenario_name)

        ui = getMUI()
        table = ui.table_constructor

        row_count = table.rowCount()
        commands_position_roadmap = []
        for row in range(row_count):
            for column in range(SippDrawConf.COUNT_OF_COLUMN):
                block = table.item(row, column)
                if block is not None:
                    commands_position_roadmap.append(block.command)
        print(commands_position_roadmap)

        for cmd in commands_position_roadmap:
            root.append(cmd.convertToXmlView())

        tree = ET.ElementTree(root)
        tree.write(self.path_to_file,
                   pretty_print = True,
                   xml_declaration = True,
                   encoding = "UTF-8",
                   doctype = '<!DOCTYPE scenario SYSTEM "sipp.dtd">')
        self.saved = True

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
            color = 'white'
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
            elif isinstance(command, NopCommand):
                insert_to_column = SippDrawConf.ACTION_CMD_COLUMN
                block_name = 'Nop'
            elif isinstance(command, PauseCommand):
                insert_to_column = SippDrawConf.ACTION_CMD_COLUMN
                block_name = 'Pause={}'.format(command.milliseconds if command.milliseconds > 0 else '')

            block = TableBlock(block_name, command)
            block.setBackgroundColor(QColor(color))
            ui.table_constructor.setItem(insert_to_row, insert_to_column, block)

