# 🏨 Hotel Reservation System

This project is a Hotel Room Reservation System developed as a final Object-Oriented Programming (OOP) project. It is designed to facilitate hotel room bookings for customers and manage reservations efficiently. The system aims to streamline the booking process, provide an intuitive user interface, and ensure smooth hotel operations through effective room management.

## 👥 Our Team
- [Aliya Asanova](https://github.com/AliyaAsanova) (AliyaAsanova): 🧠 Backend Developer 
- [Madina Gabbazova](https://github.com/vinw777) (vinw777): 🎨 Project Manager
- [Gulum Manasova](https://github.com/GulumManasova) (GulumManasova): 🗄️ Database Administrator

## 📂 Structure

hotel_reservation/

├── controller.py       
├── model.py           
├── view.py             
├── hotel_reservation.db  
├── resources/          
└── README.md   

- # controller.py
    [reservation_controller.py](https://github.com/AliyaAsanova/OOP_project/blob/master/reservation_controller.py) : Implements controller logic (MVC). Connects UI actions to database operations using DAOs.

-  # model.py 
    [room_dao.py](https://github.com/AliyaAsanova/OOP_project/blob/master/room_dao.py) : DAO for rooms. Handles room creation, retrieval, and updating availability.

    [customer_dao.py](https://github.com/AliyaAsanova/OOP_project/blob/master/customer_dao.py) : Data Access Object for customers. Supports creating, reading, updating, and deleting customer records
    
    [reservation_dao.py](https://github.com/AliyaAsanova/OOP_project/blob/master/reservation_dao.py) : DAO for reservations. Supports CRUD operations for reservation records, including cost calculations.
hotel_reservation.db | SQLite database file. Stores data for customers, rooms, and reservations

    [test_customer_dao.py](https://github.com/AliyaAsanova/OOP_project/blob/master/test_customer_dao.py) : Unit test for CustomerDAO. Adds test customers and checks they are correctly stored in the database.

    [test_reservation_dao.py](https://github.com/AliyaAsanova/OOP_project/blob/master/test_reservation_dao.py) : Test script for ReservationDAO. Adds a sample reservation and prints all reservations.
    [test_room_dao.py](https://github.com/AliyaAsanova/OOP_project/blob/master/test_room_dao.py) : Test script for RoomDAO. Adds a test room, then displays all and available rooms.


- # view.py
    [view.py](https://github.com/AliyaAsanova/OOP_project/blob/master/view.py)  : Main GUI logic. Connects buttons from the UI `qtdesign4_ui.py` to actions like viewing rooms, making reservations, etc.

    [qtdesign4.ui](https://github.com/AliyaAsanova/OOP_project/blob/master/qtdesign4.ui)  : UI layout created in Qt Designer. Defines button positions, styles, and structure of the main window

    [qtdesign4_ui.py](https://github.com/AliyaAsanova/OOP_project/blob/master/qtdesign4_ui.py) :  Auto-generated Python code from the .ui file. Used to build the interface with PyQt6.
    
    [dialogs.py](https://github.com/AliyaAsanova/OOP_project/blob/master/dialogs.py) : Contains all functional dialog windows (Make Reservation, Update, Cancel, Add Room, View Reservations) with forms and tables.



- # DB
    [hotel_reservation.db](https://github.com/AliyaAsanova/OOP_project/blob/master/hotel_reservation.db)

 - # resources
    [images](https://github.com/AliyaAsanova/OOP_project/tree/master/images)
 
 - # README.md
    [README.md](https://github.com/AliyaAsanova/OOP_project/blob/master/README.md)

- # main.py 
    [main.py](https://github.com/AliyaAsanova/OOP_project/blob/master/main.py) : Launches the application. Initializes the PyQt6 app and opens the main window (HotelReservationApp)




##  🖼️ UML Class diagram
![image](images/uml.png)




## 📊 Database Reports
!["1"](images/report.png)
!["2"](images/report1.png)
!["3"](images/customer.png)
!["4"](images/reservations.png)
!["5"](images/rooms.png)


## Weekly Meeting Documentation
[Meeting Documentation](https://docs.google.com/document/d/1_htmtroq5o1iu5VNKjSZXFNl-JBeMTzT/edit?usp=drivesdk&ouid=108611784893782046760&rtpof=true&sd=true)


## Presentation 
[Presentation](https://www.canva.com/design/DAGjwX11IKM/P5UfgfNe-QNC-kTOExqvpQ/edit?utm_content=DAGjwX11IKM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)



## Screenshots
!["Main Window"](images/screenshot1.mainwindow.png)
![](images/view_rooms.png)
![](images/make_reservation.png)
![](images/make_reservation1.png)
![](images/make_reservation2.png)
![](images/view_reservations.png)
![](images/add_room.png)
![](images/rooms1.png)
![](images/update.png)
![](images/cancel.png)
![](images/cancel1.png)




## Commit History
![image](images/commits.png)


## GitHub Repository
https://github.com/AliyaAsanova/OOP_project


