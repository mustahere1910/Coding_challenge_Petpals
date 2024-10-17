from entity.pet import Pet
from entity.dog import Dog
from entity.cat import Cat
from entity.pet_shelter import PetShelter
from entity.cash_donation import CashDonation
from entity.item_donation import ItemDonation
from entity.adoption_event import AdoptionEvent
from dao.pet_dao import PetDAO
from dao.donation_dao import DonationDAO
from dao.adoption_event_dao import AdoptionEventDAO
from exception.invalid_age_exception import InvalidAgeException
from exception.insufficient_funds_exception import InsufficientFundsException
from exception.file_handling_exception import FileHandlingException
from exception.adaption_exception import AdoptionException

class MainModule:
    def main_menu(self):
        while True:
            print("1. Add Pet")
            print("2. List Available Pets")
            print("3. Record Donation")
            print("4. Manage Adoption Event")
            print("5. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_pet()
            elif choice == "2":
                self.list_available_pets()
            elif choice == "3":
                self.record_donation()
            elif choice == "4":
                self.manage_adoption_event()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_pet(self):
        name = input("Enter pet name: ")
        age = int(input("Enter pet age: "))
        breed = input("Enter pet breed: ")
        if age <= 0:
            raise InvalidPetAgeException("Age must be a positive integer.")
        
        pet = Pet(name, age, breed)
        shelter = PetShelter()
        shelter.add_pet(pet)
        print(f"Added pet: {pet}")

    def list_available_pets(self):
        shelter = PetShelter()
        pets = shelter.list_available_pets()
        for pet in pets:
            print(pet)

    def record_donation(self):
        donor_name = input("Enter donor name: ")
        donation_type = input("Enter donation type (cash/item): ")
        
        if donation_type == "cash":
            amount = float(input("Enter donation amount: "))
            if amount < 10:
                raise InsufficientFundsException("Minimum donation amount is $10.")
            donation = CashDonation(donor_name, amount, "2024-01-01")
            donation.record_donation()
            print("Cash donation recorded.")
        elif donation_type == "item":
            item_type = input("Enter item type: ")
            donation = ItemDonation(donor_name, 0, item_type)
            donation.record_donation()
            print("Item donation recorded.")
        else:
            print("Invalid donation type.")

    def manage_adoption_event(self):
        event = AdoptionEvent()
        participant_name = input("Enter participant name: ")
        participant_type = input("Enter participant type (shelter/adopter): ")
        if participant_type.lower() not in ['shelter', 'adopter']:
            print("Invalid participant type.")
            return
        
        event.register_participant(participant_name, participant_type)
        print(f"Registered {participant_name} as a {participant_type} for the adoption event.")

        # Optionally, you could add logic to display event details or participants here
        print("Current participants:")
        for participant in event.participants:
            print(participant)

if __name__ == "__main__":
    main_module = MainModule()
    main_module.main_menu()
