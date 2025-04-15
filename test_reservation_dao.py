from reservation_dao import ReservationDAO

dao = ReservationDAO()


dao.create_reservation(
    name="Aliya",
    surname="Asanova",
    email="aliya@example.com",
    mobile="0700123456",
    room_id=1,
    check_in="2025-04-20",
    check_out="2025-04-23",
    cost=19500.0  
)


reservations = dao.get_all_reservations()
for res in reservations:
    print(res)

dao.close()
