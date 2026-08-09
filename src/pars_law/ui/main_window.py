from PySide6.QtWidgets import QLabel, QMainWindow, QStatusBar
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, app_name: str):
        super().__init__()
        self.setWindowTitle(app_name)
        self.resize(1200, 760)

        label = QLabel(
            "ParsLaw AI Enterprise\n\n"
            "هسته اولیه پروژه با موفقیت اجرا شد.\n"
            "ماژول‌های قوانین، PDF، OCR، RAG و تحلیل قرارداد در مراحل بعدی اضافه می‌شوند."
        )
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)

        status = QStatusBar()
        status.showMessage("نسخه توسعه 0.1.0")
        self.setStatusBar(status)
