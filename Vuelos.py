from abc import ABC, abstractmethod
import random

class Flight(ABC):
    @abstractmethod
    def get_details(self):
        pass

class DomesticFlight(Flight):
    def __init__(self, destination, departure_time, seats_available):
        self.destination = destination
        self.departure_time = departure_time
        self.seats_available = seats_available

    def get_details(self):
        return f"Domestic Flight to {self.destination} at {self.departure_time}"

    def reserve_seat(self, seat_choice):
        if seat_choice.upper() in self.seats_available:
            self.seats_available.remove(seat_choice.upper())
            return True
        else:
            return False

class FlightFactory(ABC):
    @abstractmethod
    def create_flight(self, destination, departure_time):
        pass

class DomesticFlightFactory(FlightFactory):
    def create_flight(self, destination, departure_time):
        seats_available = ['A', 'B', 'C', 'D']
        return DomesticFlight(destination, departure_time, seats_available)

class FlightDetails:
    def __init__(self, destination, departure_time, arrival_time, cost):
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.cost = cost

class FlightCatalog:
    def __init__(self, factory):
        self.factory = factory
        self.flights = []

    def add_flight(self, flight_details):
        flight = self.factory.create_flight(
            flight_details['destination'],
            flight_details['departure_time']
        )
        self.flights.append((flight, flight_details))

    def show_catalog(self):
        print("Catálogo de vuelos disponibles:")
        for idx, (_, details) in enumerate(self.flights, start=1):
            print(f"Vuelo {idx}: {details['destination']} | Salida: {details['departure_time']} | Llegada: {details['arrival_time']} | Costo: {details['cost']}")

    def reserve_flight(self, idx):
        if 1 <= idx <= len(self.flights):
            flight, flight_details = self.flights[idx - 1]
            print("Detalles del vuelo seleccionado:")
            print(flight.get_details())

            print("Asientos disponibles:")
            for seat in flight_details['seats_available']:
                print(seat, end=" ")
            print()

            seat_choice = input("Seleccione el asiento deseado: ")
            if flight.reserve_seat(seat_choice):
                print(f"Se ha reservado el asiento {seat_choice.upper()} en el vuelo a {flight_details['destination']} con salida a {flight_details['departure_time']} y llegada a {flight_details['arrival_time']} por un costo de {flight_details['cost']}.")
            else:
                print("El asiento seleccionado no está disponible.")

                other_seats = [seat for seat in flight_details['seats_available'] if seat != seat_choice.upper()]
                if other_seats:
                    print("Asientos disponibles alternativos:")
                    for seat in other_seats:
                        print(seat, end=" ")
                    print()
                else:
                    print("No hay más asientos disponibles para este vuelo.")
        else:
            print("Selección inválida.")

def get_user_input():
    origin = input("Ingrese la ciudad de origen: ")
    return origin

def select_flight(catalog):
    idx = input("Ingrese el número del vuelo que desea reservar: ")
    catalog.reserve_flight(int(idx))

def main():
    print("Bienvenido al sistema de reserva de vuelos.")

    origin = get_user_input()

    factory = DomesticFlightFactory()
    catalog = FlightCatalog(factory)
    
    catalog.add_flight({'destination': "México", 'departure_time': "Salida Aeropuerto Hermanos Cerdán: 2024-05-05 08:00", 'arrival_time': "Llegada Aeropuerto Internacional Benidto Juarez: 2024-05-05 11:00", 'cost': "2,689$", 'seats_available': ['A', 'B', 'C','D']})
    catalog.add_flight({'destination': "Chihuahua", 'departure_time': "Salida Aeropuerto Hermanos Cerdán: 2024-05-05 10:00", 'arrival_time': "Llegada Aeropuerto Internacional General Roberto Fierro Villalobos: 2024-05-05 16:00", 'cost': "3,054$", 'seats_available': ['A', 'B', 'C', 'D']})
    catalog.add_flight({'destination': "Baja California Sur", 'departure_time': "Salida Aeropuerto Hermanos Cerdán: 2024-05-05 12:00", 'arrival_time': "Llegada Aeropuerto de la Paz: 2024-05-05 18:00", 'cost': "3,445$", 'seats_available': ['A', 'B', 'C', 'D']})

    catalog.show_catalog()

    select_flight(catalog)

if __name__ == "__main__":
    main()
