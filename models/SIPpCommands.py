from lxml import etree as ET


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

    def __init__(self, xml_elem = None):
        if xml_elem is not None:
            attrs_to_update = {}
            for k, v in xml_elem.attrib.items():
                try:
                    attrs_to_update[k] = int(v)
                except ValueError:
                    try:
                        attrs_to_update[k] = float(v)
                    except ValueError:
                        attrs_to_update[k] = v
                if v == 'true':
                    attrs_to_update[k] = True
                elif v == 'false':
                    attrs_to_update[k] = False
            self.__dict__.update(attrs_to_update)
            self.content = xml_elem.text if xml_elem.text is not None else ''

    def convertToXmlView(self):
        element = ET.Element('base')
        if self.start_rtd:
            element.set('start_rtd', self.start_rtd)
        if self.rtd >= 0:
            element.set('rtd', str(self.rtd))
        if self.repeat_rtd:
            element.set('repeat_rtd', 'true')
        if self.crlf:
            element.set('crlf', 'true')
        if self.next:
            element.set('next', self.next)
        if self.test:
            element.set('test', self.test)
        if self.chance >= 0:
            element.set('chance', str(self.chance))
        if self.condexec:
            element.set('condexec', self.condexec)
        if self.condexec_inverse:
            element.set('condexec_inverse', 'true')
        if self.counter:
            element.set('counter', self.counter)
        return element

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
        element = super().convertToXmlView()
        element.tag = 'send'

        if self.retrans >= 0:
            element.set('retrans', str(self.retrans))
        if self.lost_send >= 0:
            element.set('lost', str(self.lost_send))
        if self.start_txn:
            element.set('start_txn', self.start_txn)
        if self.ack_txn:
            element.set('ack_txn', self.ack_txn)
        if self.content:
            element.text = ET.CDATA(self.content)
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

    def convertToXmlView(self):
        element = super().convertToXmlView()
        element.tag = 'recv'

        if self.response >= 0:
            element.set('response', str(self.response))
        if self.request != '-':
            element.set('request', self.request)
        if self.optional:
            element.set('optional', 'true')
        if self.ignoresdp:
            element.set('ignoresdp', 'true')
        if self.rrs:
            element.set('rrs', 'true')
        if self.auth:
            element.set('auth', 'true')
        if self.lost >= 0:
            element.set('lost', str(self.lost))
        if self.timeout >= 0:
            element.set('timeout', str(self.timeout))
        if self.ontimeout:
            element.set('ontimeout', self.ontimeout)
        if self.regexp_match:
            element.set('regexp_match', 'true')
        if self.response_txn:
            element.set('response_txn', self.response_txn)
        if self.content:
            element.text = self.content
        return element


class PauseCommand(BaseCommand):
    #: int:
    milliseconds = -1
    #: int?:
    variable = -1
    #: str:
    distribution = '-'
    #: bool:
    sanity_check = True

    def convertToXmlView(self):
        element = super().convertToXmlView()
        element.tag = 'pause'

        if self.milliseconds >= 0:
            element.set('milliseconds', str(self.milliseconds))
        if self.variable >= 0:
            element.set('variable', str(self.variable))
        if self.distribution != '-':
            element.set('distribution', self.distribution)
        if not self.sanity_check:
            element.set('sanity_check', 'false')
        return element


class NopCommand(BaseCommand):

    def convertToXmlView(self):
        element = super().convertToXmlView()
        element.tag = 'nop'
        if self.content:
            element.text = self.content
        return element


