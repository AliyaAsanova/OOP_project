
from room_dao import RoomDAO

dao = RoomDAO()


dao.add_room("Double", 6500)


rooms = dao.get_all_rooms()
for room in rooms:
    print(room)


print("Available rooms:")
print(dao.get_available_rooms())

dao.close()
