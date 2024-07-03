from faker import Faker


faker = Faker('pt_br')

print(faker.name())
print(faker.address())