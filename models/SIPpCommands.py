class BaseCommand:
    """This class is base for all SIPp commands.

    The main task for classes that implement it is to match the SIPp command attributes with its
    value. If a attribute has not default value, the 'None' value shall be set.

    """
    #: str:
    start_rtd = None
    #: int?:
    rtd = None
    #: bool:
    repeat_rtd = False
    #: bool:
    crlf = False
    #: str:
    next = None
    #: str:
    test = None
    #: float:
    chance = None
    #: str:
    condexec = None
    #: bool:
    condexec_inverse = False
    #: str:
    counter = None
    #: str?: contains data that located in command.
    content = None


class SendCommand(BaseCommand):
    #: int:
    retrans = None
    #: int:
    lost = None
    #: str?:
    start_txn = None
    #: str?:
    ack_txn = None


class RecvCommand(BaseCommand):
    #: int:
    response = None
    request = None
    optional = False
    ignoresdp = False
    rrs = False
    auth = False
    #: int:
    lost = None
    #: int:
    timeout = None
    #: str?:
    ontimeout = None
    regexp_match = False
    #: str?
    response_txn = None


class PauseCommand(BaseCommand):
    #: int:
    milliseconds = None
    #: str?:
    variable = None
    #: str:
    distribution = None
    #: bool:
    sanity_check = True


class NopCommand(BaseCommand):
    pass

