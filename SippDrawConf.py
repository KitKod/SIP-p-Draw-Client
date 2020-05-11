class SippDrawConf:
    main_window = None
    ui = None


def getMainWindow():
    if SippDrawConf.main_window is None:
        from main import MainWindow
        SippDrawConf.main_window = MainWindow()
    return SippDrawConf.main_window


def getUI():
    if SippDrawConf.ui is None:
        SippDrawConf.ui = getMainWindow().ui
    return SippDrawConf.ui

