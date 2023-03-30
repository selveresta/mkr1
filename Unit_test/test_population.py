import pytest

from src.main import countries, generate_population, read_file


@pytest.fixture
def file_fixture(tmp_path):
    return "population.txt"


@pytest.fixture
def countries_fixture():
    return countries


@pytest.mark.parametrize("start_year, num_years", [(2000, 10), (2010, 5)])
def test_generate_population(file_fixture, countries_fixture, start_year, num_years):
    # створити словник для зберігання даних про країни та їх населення
    country_data = {}

    # згенерувати дані про населення країн
    generate_population(countries_fixture, start_year, num_years)

    # прочитати дані з файлу та зберегти їх у словник
    read_file(file_fixture, country_data)

    # перевірити, що кількість років збігається зі значенням num_years
    assert len(next(iter(country_data.values()))) == num_years

    # перевірити, що кількість країн збігається зі значенням len(countries)
    assert len(country_data) == len(countries_fixture)
