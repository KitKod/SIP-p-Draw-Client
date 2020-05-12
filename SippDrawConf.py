class SippDrawConf:
    RECV_CMD_COLUMN = 0
    ACTION_CMD_COLUMN = 1
    SEND_CMD_COLUMN = 2
    COUNT_OF_COLUMN = 3
    COLUMN_HEADERS = ('recv', 'action', 'send')

    TOOLBOX_COMM_ATTR_PAGE = 0
    TOOLBOX_SPEC_ATTR_PAGE = 1
    TOOLBOX_CONTENT_PAGE = 2

    STACK_SPEC_ATTR_RECV_PAGE = 0
    STACK_SPEC_ATTR_SEND_PAGE = 1
    STACK_SPEC_ATTR_PAUSE_PAGE = 2
    STACK_SPEC_ATTR_NOP_PAGE = 3

    STACK_CONTENT_PAGE = 0
    STACK_CONTENT_STAB_PAGE = 1

    SPECIAL_VALUE_SPINBOX = '-'

    main_window = None
    ui = None


def getMainWindow():
    if SippDrawConf.main_window is None:
        from gui.Windows import MainWindow
        SippDrawConf.main_window = MainWindow()
    return SippDrawConf.main_window


def getUI():
    if SippDrawConf.ui is None:
        SippDrawConf.ui = getMainWindow().ui
    return SippDrawConf.ui

