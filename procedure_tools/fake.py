from faker import Faker
from faker.providers.phone_number import Provider

fake = Faker("uk_UA")
fake_en = Faker("en_US")


class ProzorroPhoneNumberProvider(Provider):
    def prozorro_phone_number(self):
        return f"+{self.msisdn()[1:]}"


fake.add_provider(ProzorroPhoneNumberProvider)
