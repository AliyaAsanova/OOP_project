from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox,
    QSpinBox, QDoubleSpinBox, QPushButton, QDateEdit, QTableWidget,
    QTableWidgetItem
)
from PyQt6.QtCore import QDate
from reservation_controller import ReservationController
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QSpinBox, QDateEdit, QPushButton, QMessageBox
from PyQt6.QtCore import QDate
from datetime import datetime


COMMON_STYLE = """
    QLabel { color: white; font-size: 14px; }
    QPushButton {
        background-color: #3498db;
        color: white;
        border-radius: 6px;
        padding: 8px;
        font-weight: bold;
    }
    QPushButton:hover { background-color: #2980b9; }
    QDialog { background-color: #2c3e50; }
"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLineEdit, QSpinBox, QDateEdit, QPushButton,
    QMessageBox, QTableWidget, QTableWidgetItem, QLabel
)
from PyQt6.QtCore import QDate
from datetime import datetime


class ReservationDialog(QDialog):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.setWindowTitle("Make Reservation")
        self.setMinimumSize(900, 400)
        self.setStyleSheet(COMMON_STYLE)

        
        main_layout = QHBoxLayout()

        
        form_layout = QFormLayout()
        self.room_id_input = QSpinBox()
        self.room_id_input.setMinimum(1)

        self.name_input = QLineEdit()
        self.surname_input = QLineEdit()
        self.email_input = QLineEdit()
        self.mobile_input = QLineEdit()

        self.check_in_input = QDateEdit()
        self.check_in_input.setCalendarPopup(True)
        self.check_in_input.setDate(QDate.currentDate())

        self.check_out_input = QDateEdit()
        self.check_out_input.setCalendarPopup(True)
        self.check_out_input.setDate(QDate.currentDate().addDays(1))

        form_layout.addRow("Room ID:", self.room_id_input)
        form_layout.addRow("Name:", self.name_input)
        form_layout.addRow("Surname:", self.surname_input)
        form_layout.addRow("Email:", self.email_input)
        form_layout.addRow("Mobile:", self.mobile_input)
        form_layout.addRow("Check-in:", self.check_in_input)
        form_layout.addRow("Check-out:", self.check_out_input)

        reserve_button = QPushButton("Reserve")
        reserve_button.clicked.connect(self.accept)

        left_layout = QVBoxLayout()
        left_layout.addLayout(form_layout)
        left_layout.addWidget(reserve_button)

        
        self.table = QTableWidget()
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Surname", "Email", "Mobile", "Room ID", "Check-in", "Check-out","Cost"])
        self.load_reservations()

        
        main_layout.addLayout(left_layout, 1)
        main_layout.addWidget(self.table, 2)

        self.setLayout(main_layout)

    def load_reservations(self):
        try:
            reservations = self.controller.get_all_reservations()
            self.table.setRowCount(len(reservations))
            for row, r in enumerate(reservations):
                for col in range(9):
                    self.table.setItem(row, col, QTableWidgetItem(str(r[col])))
        except Exception as e:
            QMessageBox.critical(self, "Error loading reservations", str(e))

    def accept(self):
        try:
            room_id = self.room_id_input.value()
            name = self.name_input.text()
            surname = self.surname_input.text()
            email = self.email_input.text()
            mobile = self.mobile_input.text()
            check_in = self.check_in_input.date().toString("yyyy-MM-dd")
            check_out = self.check_out_input.date().toString("yyyy-MM-dd")

            
            check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
            check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
            nights = (check_out_date - check_in_date).days

            if nights <= 0:
                raise ValueError("Check-out date must be after check-in date.")

            price = self.controller.get_room_price(room_id)
            if price is None:
                raise ValueError("Room not found.")

            cost = price * nights

            
            self.controller.make_reservation(name, surname, email, mobile, room_id, check_in, check_out, cost)

            QMessageBox.information(self, "Success", "Reservation created.")
            self.load_reservations()  
            self.close()

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


class UpdateReservationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Update Reservation")
        self.setMinimumSize(900, 400)
        self.controller = ReservationController()
        self.setStyleSheet(COMMON_STYLE)

        main_layout = QHBoxLayout()
        form_layout = QFormLayout()

        self.reservation_id_input = QSpinBox()
        self.reservation_id_input.setMaximum(9999)

        self.room_id_input = QSpinBox()
        self.room_id_input.setMaximum(9999)

        self.name_input = QLineEdit()
        self.surname_input = QLineEdit()
        self.email_input = QLineEdit()
        self.mobile_input = QLineEdit()

        self.check_in_input = QDateEdit()
        self.check_in_input.setCalendarPopup(True)
        self.check_in_input.setDate(QDate.currentDate())

        self.check_out_input = QDateEdit()
        self.check_out_input.setCalendarPopup(True)
        self.check_out_input.setDate(QDate.currentDate().addDays(1))

        form_layout.addRow("Reservation ID:", self.reservation_id_input)
        form_layout.addRow("Room ID:", self.room_id_input)
        form_layout.addRow("Name:", self.name_input)
        form_layout.addRow("Surname:", self.surname_input)
        form_layout.addRow("Email:", self.email_input)
        form_layout.addRow("Mobile:", self.mobile_input)
        form_layout.addRow("Check-in:", self.check_in_input)
        form_layout.addRow("Check-out:", self.check_out_input)

        self.submit_btn = QPushButton("Update Reservation")
        self.submit_btn.clicked.connect(self.accept)
        form_layout.addRow(self.submit_btn)

        self.table = QTableWidget()
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels([
            "ID", "Name", "Surname", "Email", "Mobile",
            "Room ID", "Check-in", "Check-out", "Cost"
        ])
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        main_layout.addLayout(form_layout, 1)
        main_layout.addWidget(self.table, 2)

        self.setLayout(main_layout)
        self.load_reservations()

    def get_data(self):
        return (
            self.reservation_id_input.value(),
            self.name_input.text(),
            self.surname_input.text(),
            self.email_input.text(),
            self.mobile_input.text(),
            self.room_id_input.value(),
            self.check_in_input.date().toString("yyyy-MM-dd"),
            self.check_out_input.date().toString("yyyy-MM-dd"),
        )

    def accept(self):
        
        if not all([
            self.name_input.text().strip(),
            self.surname_input.text().strip(),
            self.email_input.text().strip(),
            self.mobile_input.text().strip()
        ]):
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return

        try:
            reservation_id, name, surname, email, mobile, room_id, check_in, check_out = self.get_data()

            check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
            check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
            nights = (check_out_date - check_in_date).days

            if nights <= 0:
                raise ValueError("Check-out must be after check-in.")

            price = self.controller.get_room_price(room_id)
            if price is None:
                raise ValueError("Room not found.")

            cost = price * nights


            found = False
            for r in self.controller.get_all_reservations():
                if r[0] == reservation_id and r[5] == room_id: 
                    found = True
                    break

            if not found:
                raise ValueError("Choose the correct reservation and room ID.")


            self.controller.update_reservation(
                reservation_id, name, surname, email, mobile,
                room_id, check_in, check_out, cost
            )



            QMessageBox.information(self, "Success", "Reservation updated.")
            self.load_reservations()
            self.close()

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def load_reservations(self):
        reservations = self.controller.get_all_reservations()
        self.table.setRowCount(len(reservations))
        for row, r in enumerate(reservations):
            for col in range(9):
                self.table.setItem(row, col, QTableWidgetItem(str(r[col])))

class AddRoomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Room")
        self.setMinimumSize(700, 300)
        self.setStyleSheet(COMMON_STYLE)
        self.controller = ReservationController()

        layout = QHBoxLayout()
        form_layout = QVBoxLayout()

        self.room_id_input = QSpinBox()
        self.room_id_input.setMaximum(9999)

        self.room_type_input = QComboBox()
        self.room_type_input.addItems(["single", "double", "suite"])

        self.price_input = QDoubleSpinBox()
        self.price_input.setMaximum(10000.00)
        self.price_input.setDecimals(2)

        form_layout.addWidget(QLabel("Room ID:"))
        form_layout.addWidget(self.room_id_input)
        form_layout.addWidget(QLabel("Room Type:"))
        form_layout.addWidget(self.room_type_input)
        form_layout.addWidget(QLabel("Price:"))
        form_layout.addWidget(self.price_input)

        self.submit_btn = QPushButton("Add Room")
        self.submit_btn.clicked.connect(self.add_room)
        form_layout.addWidget(self.submit_btn)

        self.rooms_table = QTableWidget()
        self.rooms_table.setColumnCount(3)
        self.rooms_table.setHorizontalHeaderLabels(["Room ID", "Type", "Price"])
        self.rooms_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        layout.addLayout(form_layout, 1)
        layout.addWidget(self.rooms_table, 2)

        self.setLayout(layout)
        self.load_available_rooms()

    def add_room(self):
        data = (
            self.room_id_input.value(),
            self.room_type_input.currentText(),
            self.price_input.value()
        )
        self.controller.add_room(*data)
        self.load_available_rooms()

    def load_available_rooms(self):
        rooms = self.controller.get_available_rooms()
        self.rooms_table.setRowCount(len(rooms))
        for row, room in enumerate(rooms):
            self.rooms_table.setItem(row, 0, QTableWidgetItem(str(room[0])))
            self.rooms_table.setItem(row, 1, QTableWidgetItem(room[1]))
            self.rooms_table.setItem(row, 2, QTableWidgetItem(f"{room[2]:.2f}"))


from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QMessageBox
)

class ViewReservationsDialog(QDialog):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.setWindowTitle("View Reservations")
        self.setMinimumSize(900, 400)
        self.setStyleSheet(COMMON_STYLE)
        

        layout = QVBoxLayout()

        
        self.table = QTableWidget()
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels([
            "ID", "Name", "Surname", "Email", "Mobile",
            "Room ID", "Check-in", "Check-out", "Cost"
        ])
        layout.addWidget(self.table)

        
        refresh_btn = QPushButton("Refresh")
        refresh_btn.clicked.connect(self.load_reservations)
        layout.addWidget(refresh_btn)

        self.setLayout(layout)
        self.load_reservations()

    def load_reservations(self):
        try:
            reservations = self.controller.get_all_reservations()
            self.table.setRowCount(len(reservations))
            for row, r in enumerate(reservations):
                for col in range(9):
                    self.table.setItem(row, col, QTableWidgetItem(str(r[col])))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


class CancelReservationDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cancel Reservation")
        self.setMinimumSize(800, 300)
        self.setStyleSheet(COMMON_STYLE)
        self.controller = ReservationController()

        layout = QHBoxLayout()
        form_layout = QVBoxLayout()

        
        self.reservation_id_input = QSpinBox()
        self.reservation_id_input.setMaximum(9999)
        form_layout.addWidget(QLabel("Reservation ID to Cancel:"))
        form_layout.addWidget(self.reservation_id_input)

        self.room_id_input = QSpinBox()
        self.room_id_input.setMaximum(9999)
        form_layout.addWidget(QLabel("Room ID to Cancel:"))
        form_layout.addWidget(self.room_id_input)

        self.submit_btn = QPushButton("Cancel Reservation")
        self.submit_btn.clicked.connect(self.accept)
        form_layout.addWidget(self.submit_btn)

        self.res_table = QTableWidget()
        self.res_table.setColumnCount(8)
        self.res_table.setHorizontalHeaderLabels([
            "ID", "Name", "Surname", "Email", "Mobile",
            "Room ID", "Check-in", "Check-out"
        ])
        self.res_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        layout.addLayout(form_layout, 1)
        layout.addWidget(self.res_table, 2)

        self.setLayout(layout)
        self.load_reservations()

    def get_data(self):
        return self.reservation_id_input.value(), self.room_id_input.value()

    def load_reservations(self):
        reservations = self.controller.get_all_reservations()
        self.res_table.setRowCount(len(reservations))
        for row, r in enumerate(reservations):
            for col in range(8):
                self.res_table.setItem(row, col, QTableWidgetItem(str(r[col])))

