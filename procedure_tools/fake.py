from faker import Faker
from faker.providers.phone_number import Provider


faker = Faker("uk_UA")
faker_en = Faker("en_US")

class ProzorroPhoneNumberProvider(Provider):
    def prozorro_phone_number(self):
        return f'+{self.msisdn()[1:]}'


faker.add_provider(ProzorroPhoneNumberProvider)