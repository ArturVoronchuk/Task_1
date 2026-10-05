import pytest

from bun import Bun

class TestBun:

    @pytest.mark.parametrize(
        "name",
        [
            "Black Hole Bun",
            "The Red Giant Bun",
            "Star Bun",
        ]
    )
    def test_get_name_returns_stored_name(self, name):
        bun = Bun(name, 100.0)
        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "price",
        [
            200.0,
            150.0,
            199.0,
        ]
    )
    def test_get_price_returns_stored_price(self, price):
        bun = Bun("Black Hole Bun", price)
        assert bun.get_price() == price