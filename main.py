import sys
from PyQt6.QtWidgets import QApplication
from view import HotelReservationApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HotelReservationApp()
    window.show()
    sys.exit(app.exec())
