from PySide2.QtWidgets import QTableWidgetItem


class TableBlock(QTableWidgetItem):
    #: str: the value to be displayed in the construct table.
    display_name = None
    #: BaseCommand: this instance represents a SIPp command.
    command = None

    def __init__(self, display_name, command):
        self.display_name = display_name
        self.command = command
        super().__init__(display_name)



