class Animal:
    def __init__(self, genus, name, year_of_birth, weight=None, habitat=None):
        self.genus = genus
        self.name = name
        self.year_of_birth = year_of_birth
        self.weight = weight  # in kilograms, optional
        self.habitat = habitat  # optional

    def get_age(self, year):
        """Calculate the age of the animal in a given year."""
        return year - self.year_of_birth

    def get_info(self):
        """Return a string with the animal's name and genus."""
        return f"{self.name} is a {self.genus}"

    def display_details(self):
        """Display detailed information about the animal."""
        details = f"Name: {self.name}\n" \
                  f"Genus: {self.genus}\n" \
                  f"Year of Birth: {self.year_of_birth}\n"
        if self.weight is not None:
            details += f"Weight: {self.weight} kg\n"
        if self.habitat is not None:
            details += f"Habitat: {self.habitat}\n"
        return details

def find_oldest_animal(animals, current_year):
    """Find the oldest animal from a list of animals."""
    oldest_animal = None
    max_age = -1
    
    for animal in animals:
        age = animal.get_age(current_year)
        if age > max_age:
            max_age = age
            oldest_animal = animal
            
    return oldest_animal

def write_animals_to_file(animals, filename):
    """Write the names and genera of animals to a text file."""
    with open(filename, 'w') as file:
        for animal in animals:
            file.write(f"{animal.name}, {animal.genus}\n")

# Create instances of Animal
animals = [
    Animal("elephant", "Dumbo", 2005, weight=6000, habitat="Savannah"),
    Animal("dog", "Balto", 2012, weight=30, habitat="Urban"),
    Animal("python", "Kaa", 2018, weight=50, habitat="Jungle"),
    Animal("fox", "Foxy", 2010, weight=8, habitat="Forest"),
    Animal("lion", "Simba", 2015, weight=190, habitat="Savannah"),
    Animal("parrot", "Polly", 2020, weight=1, habitat="Tropical Rainforest")
]

# Print information about each animal
print("Animal Information:\n")
for animal in animals:
    print(animal.get_info())
    print(animal.display_details())
    print("-" * 40)

# Find and display the age of each animal in 2023
current_year = 2023
print("Animal Ages in 2023:\n")
for animal in animals:
    age = animal.get_age(current_year)
    print(f"{animal.name} is {age} years old.")

# Find and display the oldest animal
oldest_animal = find_oldest_animal(animals, current_year)
if oldest_animal:
    oldest_age = oldest_animal.get_age(current_year)
    print("\nOldest Animal:")
    print(f"Name: {oldest_animal.name}, Genus: {oldest_animal.genus}, Age: {oldest_age} years")

# Write animal names and genera to a text file
write_animals_to_file(animals, 'animals.txt')
print("\nAnimal names and genera have been written to 'animals.txt'.")
