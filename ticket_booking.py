def book_seat(booked, seat):
    if seat in booked:
        print(f"Seat {seat} is already booked.")
    else:
        booked.append(seat)

def cancel_seat(booked, seat):
    if seat in booked:
        booked.remove(seat)
    else:
        print(f"Seat {seat} is not booked.")

def get_available_seats(total, booked):
    return [seat for seat in range(1, total + 1) if seat not in booked]

total_seats = int(input("total_seats= "))

booked_seats_input = input("booked_seats= ")
booked_seats = [int(s.strip()) for s in booked_seats_input.split(",") if s.strip().isdigit()]

book_seat_input = int(input("book_seat= "))
cancel_seat_input = int(input("cancel_seat= "))

book_seat(booked_seats, book_seat_input)
cancel_seat(booked_seats, cancel_seat_input)
available = get_available_seats(total_seats, booked_seats)

print("Available seats:", available)
