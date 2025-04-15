from PyQt6.QtWidgets import QMainWindow, QMessageBox, QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel
from reservation_controller import ReservationController
from qtdesign4_ui import Ui_MainWindow
from dialogs import ReservationDialog, AddRoomDialog, UpdateReservationDialog, CancelReservationDialog, ViewReservationsDialog

class HotelReservationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.controller = ReservationController()

        self.ui.pushButton_5.clicked.connect(self.view_rooms)
        self.ui.pushButton_3.clicked.connect(self.make_reservation)
        self.ui.pushButton_4.clicked.connect(self.view_reservations)
        self.ui.pushButton_2.clicked.connect(self.add_room)
        self.ui.pushButton.clicked.connect(self.cancel_reservation)
        self.ui.btnUpdate.clicked.connect(self.update_reservation)
        self.ui.btnExit.clicked.connect(self.close)

    def view_rooms(self):
        try:
            rooms = self.controller.get_available_rooms()
            if not rooms:
                QMessageBox.information(self, "View Rooms", "No available rooms.")
                return

            dialog = QDialog(self)
            dialog.setWindowTitle("Available Rooms")
            dialog.setMinimumSize(600, 300)
            dialog.setStyleSheet("QDialog { background-color: #2c3e50; } QLabel { color: white; font-size: 16px; }")

            layout = QVBoxLayout()
            layout.addWidget(QLabel("Available Rooms"))

            table = QTableWidget()
            table.setColumnCount(3)
            table.setHorizontalHeaderLabels(["Room ID", "Type", "Price"])
            table.setRowCount(len(rooms))
            for row, room in enumerate(rooms):
                table.setItem(row, 0, QTableWidgetItem(str(room[0])))
                table.setItem(row, 1, QTableWidgetItem(room[1].capitalize()))
                table.setItem(row, 2, QTableWidgetItem(f"${room[2]:.2f}"))
            table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
            layout.addWidget(table)

            dialog.setLayout(layout)
            dialog.exec()

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def make_reservation(self):
        dialog = ReservationDialog(controller=self.controller)

        if dialog.exec():
            try:
                room_id, name, surname, email, mobile, check_in, check_out = dialog.get_data()
                self.controller.make_reservation(room_id, name, surname, email, mobile, check_in, check_out)
                QMessageBox.information(self, "Success", "Reservation successful.")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    def update_reservation(self):
        dialog = UpdateReservationDialog()
        dialog.exec()


    def view_reservations(self):
        dialog = ViewReservationsDialog(controller=self.controller)
        dialog.exec()

    def add_room(self):
        dialog = AddRoomDialog()
        if dialog.exec():
            QMessageBox.information(self, "Success", "Room added successfully.")

    def cancel_reservation(self):
        dialog = CancelReservationDialog()
        if dialog.exec():
            try:
                reservation_id, room_id = dialog.get_data()
                self.controller.cancel_reservation(reservation_id, room_id)
                QMessageBox.information(self, "Success", "Reservation cancelled.")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

