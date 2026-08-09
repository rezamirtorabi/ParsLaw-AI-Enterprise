from PySide6.QtWidgets import QApplication
from pars_law.core.config import get_settings
from pars_law.core.logging import configure_logging
from pars_law.ui.main_window import MainWindow

def main() -> None:
    settings = get_settings()
    configure_logging(settings.log_level)

    app = QApplication([])
    app.setApplicationName(settings.app_name)
    window = MainWindow(settings.app_name)
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
