import pytest
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.fixture
def star_bun():
    return  Bun("Star Bun", 110.0)

@pytest.fixture
def tomato_ingredient():
    return Ingredient(INGREDIENT_TYPE_FILLING, "томат", 5.0)

@pytest.fixture
def cheese_ingredient():
    return Ingredient(INGREDIENT_TYPE_FILLING, "сыр", 10.0)

@pytest.fixture
def sauce_ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE,"кисло-сладкий", 3.0)