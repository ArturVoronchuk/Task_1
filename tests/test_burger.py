import pytest

from burger import Burger
from conftest import cheese_ingredient


class TestBurger:

    def test_set_buns_assigns_bun_correctly(self, star_bun):
        burger = Burger()

        burger.set_buns(star_bun)

        assert burger.bun is star_bun

    def test_add_ingredient_stores_the_exact_object(self, cheese_ingredient):
        burger = Burger()

        burger.add_ingredient(cheese_ingredient)

        assert burger.ingredients[0] is cheese_ingredient

    def test_add_ingredient_allows_to_add_multiple_ingredients(self, tomato_ingredient, sauce_ingredient):
        burger = Burger()

        burger.add_ingredient(tomato_ingredient)
        burger.add_ingredient(sauce_ingredient)

        assert len(burger.ingredients) == 2

    def test_remove_ingredient_removes_item(self, tomato_ingredient):
        burger = Burger()

        burger.add_ingredient(tomato_ingredient)
        ingredient_index_to_remove = 0
        burger.remove_ingredient(ingredient_index_to_remove)

        assert len(burger.ingredients) == 0

    def test_move_ingredient_from_index_0_to_2_shifts_others(self, cheese_ingredient, tomato_ingredient, sauce_ingredient):
        burger = Burger()

        first_ingredient = tomato_ingredient
        second_ingredient = sauce_ingredient
        third_ingredient = cheese_ingredient

        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        burger.add_ingredient(third_ingredient)

        burger.move_ingredient(0, 2)

        assert burger.ingredients[0] is second_ingredient
        assert burger.ingredients[1] is third_ingredient
        assert burger.ingredients[2] is first_ingredient

    def test_get_price_correctly_summarizes_the_price_of_added_ingredients(self, star_bun, tomato_ingredient, sauce_ingredient):
        burger = Burger()

        burger.set_buns(star_bun)

        burger.add_ingredient(tomato_ingredient)
        burger.add_ingredient(sauce_ingredient)

        actual_price = burger.get_price()
        expected_price = (star_bun.get_price() * 2) + tomato_ingredient.get_price() + sauce_ingredient.get_price()

        assert actual_price == expected_price

    @pytest.mark.parametrize(
        "expected_receipt",
        [
            "(==== Star Bun ====)\n"
            "= filling томат =\n"
            "= sauce кисло-сладкий =\n"
            "= filling сыр =\n"
            "(==== Star Bun ====)\n"
            "\n"
            "Price: 238.0"
        ]
    )
    def test_get_receipt_returns_correct_format(self, star_bun, tomato_ingredient, sauce_ingredient, cheese_ingredient, expected_receipt):
        burger = Burger()
        burger.set_buns(star_bun)
        burger.add_ingredient(tomato_ingredient)
        burger.add_ingredient(sauce_ingredient)
        burger.add_ingredient(cheese_ingredient)

        assert burger.get_receipt() == expected_receipt

    @pytest.mark.parametrize(
        "expected_receipt",
        [
            "(==== Star Bun ====)\n"
            "(==== Star Bun ====)\n"
            "\n"
            "Price: 220.0"
        ]
    )
    def test_get_receipt_with_no_ingredients_includes_only_buns_and_price(self, star_bun, expected_receipt):
        burger = Burger()
        burger.set_buns(star_bun)

        assert burger.get_receipt() == expected_receipt