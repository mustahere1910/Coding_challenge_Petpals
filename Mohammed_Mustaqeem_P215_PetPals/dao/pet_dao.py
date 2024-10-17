from entity.pet import Pet

class PetDAO:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def fetch_available_pets(self):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM Pets WHERE Available_for_adaption = 1")
            pets = cursor.fetchall()
            return [Pet(*pet) for pet in pets]
        except Exception as e:
            print(f"Error fetching available pets: {e}")
            return []

    def add_pet(self, pet: Pet) -> bool:  
        try:
            cursor = self.db_connection.cursor()
            query = "INSERT INTO Pets (Pet_id, Name, Age, Breed, Type, Shelter_id, Available_for_adaption) VALUES (?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (pet.pet_id, pet.name, pet.age, pet.breed, pet.pet_type, pet.shelter_id, pet.available_for_adoption))
            self.db_connection.commit()
            return True
        except Exception as e:
            print(f"Error while adding pet: {e}")
            return False

