from faker import Faker


faker = Faker('pt_br')

dicionario = {
    "Nome" : faker.name(),
    "Idade" : faker.random_int(min = 18, max = 60),
    "Cidade" : faker.city()
}

print(dicionario)