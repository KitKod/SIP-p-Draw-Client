import xml.etree.ElementTree as ET


class BaseCommand:
    """This class is base for all SIPp commands.

    The main task for classes that implement it is to match the SIPp command attributes with its
    value. If a attribute has not default value, the 'None' value shall be set.

    """
    #: str:
    start_rtd = ''
    #: int?:
    rtd = -1
    #: bool:
    repeat_rtd = False
    #: bool:
    crlf = False
    #: str:
    next = ''
    #: str:
    test = ''
    #: float:
    chance = -1
    #: str:
    condexec = ''
    #: bool:
    condexec_inverse = False
    #: str:
    counter = ''
    #: str?: contains data that located in command.
    content = ''

    def convertToXmlView(self):
        pass

    def convertFromXmlView(self):
        pass


class SendCommand(BaseCommand):
    #: int:
    retrans = -1
    #: int:
    lost_send = -1
    #: str?:
    start_txn = ''
    #: str?:
    ack_txn = ''

    def convertToXmlView(self):
        # b = ET.SubElement(a, 'b')
        # tree = ET.ElementTree(a)
        # tree.write("filename.xml")
        element = ET.Element('send')
        if self.retrans >= 0:
            element.set('retrans', str(self.retrans))
        if self.lost_send >= 0:
            element.set('lost', str(self.lost_send))
        if self.start_txn:
            element.set('start_txn', self.start_txn)
        if self.ack_txn:
            element.set('ack_txn', self.ack_txn)
        if self.content:
            element.text = self.content
        ET.dump(element)

        return element


class RecvCommand(BaseCommand):
    #: int:
    response = -1
    request = '-'
    optional = False
    ignoresdp = False
    rrs = False
    auth = False
    #: int:
    lost = -1
    #: int:
    timeout = -1
    #: str?:
    ontimeout = ''
    regexp_match = False
    #: str?
    response_txn = ''


class PauseCommand(BaseCommand):
    #: int:
    milliseconds = -1
    #: int?:
    variable = -1
    #: str:
    distribution = '-'
    #: bool:
    sanity_check = True


class NopCommand(BaseCommand):
    pass

