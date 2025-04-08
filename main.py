import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_main_window import Ui_MainWindow
from controller import ReservationController

class HotelReservationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.controller = ReservationController()

        
        self.ui.pushButton1.clicked.connect(self.new_reservation)
        self.ui.pushButton_2.clicked.connect(self.view_reservation)
        self.ui.pushButton_3.clicked.connect(self.edit_reservation)
        self.ui.pushButton_4.clicked.connect(self.cancel_reservation)
        self.ui.pushButton_5.clicked.connect(self.exit_app)

    def new_reservation(self):
        
        self.controller.create_reservation("Aliya", 101, "2025-04-06", "2025-04-10")
        print("New reservation added.")

    def view_reservation(self):
        reservations = self.controller.get_reservations()
        for res in reservations:
            print(res)

    def edit_reservation(self):
        print("Edit reservation – пока не реализовано")

    def cancel_reservation(self):
        print("Cancel reservation – пока не реализовано")

    def exit_app(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HotelReservationApp()
    window.show()
    sys.exit(app.exec())

