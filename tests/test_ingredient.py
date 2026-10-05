import pytest

from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestIngredient:

    @pytest.mark.parametrize(
        "name",
        [
            "томат", "сыр", "бекон"
        ]
    )
    def test_get_name_returns_stored_ingredient_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, name,100.0)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize(
        "price",
        [
            100.0,
            250.0,
            333.0,
        ]
    )
    def test_get_price_returns_stored_ingredient_price(self, price):
        ingredient = Ingredient("начинка","сыр", price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize(
        "ingredient_type",
        [
            INGREDIENT_TYPE_FILLING,
            INGREDIENT_TYPE_SAUCE
        ]
    )
    def test_get_type_returns_stored_ingredient_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type,"сыр",100)
        assert ingredient.get_type() == ingredient_type