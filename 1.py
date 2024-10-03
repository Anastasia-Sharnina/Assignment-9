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

