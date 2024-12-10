from datetime import date

import pytest

from src.models.person import Person


@pytest.fixture
def adult():
    """Fixture for an adult Person instance."""
    return Person(firstname="Zoé", name="Michel", birth=date(1990, 5, 15), city="Paris")


@pytest.fixture
def minor():
    """Fixture for a Person instance representing a minor."""
    return Person(firstname="James", name="Doodle", birth=date(2015, 4, 21), city="London")


@pytest.fixture
def elder():
    """Fixture for a Person instance representing an elderly person."""
    return Person(firstname="Jack-Etienne", name="Popolo", birth=date(1938, 1, 1), city="London")


@pytest.fixture
def person_list(adult, minor, elder):
    """Fixture for a list of Person instances."""
    return [adult, minor, elder]

