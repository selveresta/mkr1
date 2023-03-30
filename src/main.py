import random

# список країн та їх населення
countries = {
    "Ukraine": 42000000,
    "USA": 328000000,
    "China": 1430000000,
    "India": 1360000000,
    "Russia": 144000000,
    "Brazil": 212000000,
    "Japan": 126000000,
    "Germany": 83000000,
    "France": 67000000,
    "Italy": 60000000,
}

# рік, з якого починаються дані
start_year = 2000

# кількість років, про які є дані
num_years = 20

filename = "population.txt"

# створити словник для зберігання даних про країни та їх населення
country_data = {}


def generate_population(countries, start_year, num_years):
    # відкрити файл для запису даних
    with open("population.txt", "w") as f:

        # згенерувати дані про населення країн
        for country, population in countries.items():
            for year in range(start_year, start_year + num_years):
                # згенерувати показник народжуваності
                birth_rate = random.uniform(1.0, 5.0)

                # згенерувати показник смертності
                death_rate = random.uniform(0.5, 2.0)

                # розрахувати приріст населення за рік
                population_increase = int(population * 
                                          (birth_rate - death_rate) / 100)

                # оновити населення країни
                population += population_increase

                # записати дані про населення країни в файл
                f.write(f"{country},{year},{population}\n")


def read_file(filename, country_data):
    with open(filename) as file:
        for line in file:
            # розділити рядок на назву країни, рік та населення
            country, year, population = line.strip().split(",")

            # перетворити рік та населення зі строкового типу 
            # на цілочисельний тип
            year = int(year)
            population = int(population)

            # додати дані до словника
            if country in country_data:
                country_data[country][year] = population
            else:
                country_data[country] = {year: population}


# відкрити файл та прочитати дані про населення країн
generate_population(countries, start_year, num_years)

read_file(filename, country_data)

# print(country_data)


def print_change_population():
    for country in country_data:
        years = sorted(country_data[country].keys())
        population_changes = []
        for i in range(1, len(years)):
            change = (
                country_data[country][years[i]] 
                - country_data[country][years[i - 1]]
            )
            population_changes.append(change)
        print(f"{country}: {population_changes}")


print_change_population()
