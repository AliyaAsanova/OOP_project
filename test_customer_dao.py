from customer_dao import CustomerDAO

def test_add_multiple_customers():
    db_name = "hotel_reservation.db"
    dao = CustomerDAO(db_name)

    test_customers = [
        ("Aliya", "Testova", "aliya1@mail.com", "0500000001"),
        ("Bakyt", "Uulu", "bakyt@mail.com", "0500000002"),
        ("Cholpon", "Kyrgyz", "cholpon@mail.com", "0500000003"),
        ("Dana", "Nur", "dana@mail.com", "0500000004"),
        ("Eldar", "Tynystanov", "eldar@mail.com", "0500000005"),
    ]

    # Добавим клиентов
    for name, surname, email, mobile in test_customers:
        dao.add_customer(name, surname, email, mobile)

    # Получим всех клиентов
    customers = dao.get_all_customers()

    # Проверим, что все добавленные есть в базе
    for name, surname, email, mobile in test_customers:
        found = any(
            c[1] == name and c[2] == surname and c[3] == email and c[4] == mobile
            for c in customers
        )
        assert found, f"❌ Customer {name} {surname} not found!"
        print(f"✅ {name} {surname} added successfully.")

if __name__ == "__main__":
    test_add_multiple_customers()

