from typing import List
from unittest.mock import Mock

from bun import Bun
from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase():

    def test_available_buns_returns_list_with_correct_buns(self):
        db = Database()
        buns = db.available_buns()

        assert len(buns) == 3

        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100

        assert buns[1].get_name() == "white bun"
        assert buns[1].get_price() == 200

        assert buns[2].get_name() == "red bun"
        assert buns[2].get_price() == 300

    def test_available_ingredients_returns_list_with_correct_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()

        assert len(ingredients) == 6

        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[0].get_price() == 100
        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE

        assert ingredients[1].get_name() == "sour cream"
        assert ingredients[1].get_price() == 200
        assert ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE

        assert ingredients[2].get_name() == "chili sauce"
        assert ingredients[2].get_price() == 300
        assert ingredients[2].get_type() == INGREDIENT_TYPE_SAUCE

        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[3].get_price() == 100
        assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING

        assert ingredients[4].get_name() == "dinosaur"
        assert ingredients[4].get_price() == 200
        assert ingredients[4].get_type() == INGREDIENT_TYPE_FILLING

        assert ingredients[5].get_name() == "sausage"
        assert ingredients[5].get_price() == 300
        assert ingredients[5].get_type() == INGREDIENT_TYPE_FILLING