import pytest

from src.order_processor import save_order, validate_order


def test_valid_order() -> None:
    order = {"product": "Книга", "quantity": 2, "price": 1500}
    assert validate_order(order) is True


@pytest.mark.parametrize(
    "order",
    [
        {"product": "", "quantity": 1, "price": 100},
        {"product": "Книга", "quantity": 0, "price": 100},
        {"product": "Книга", "quantity": -1, "price": 100},
        {"product": "Книга", "quantity": 1, "price": 0},
        {"product": "Книга", "quantity": 1, "price": -10},
        {"quantity": 1, "price": 100},
    ],
)
def test_invalid_orders(order: dict) -> None:
    with pytest.raises(ValueError):
        validate_order(order)


@pytest.mark.parametrize(
    "order",
    [
        {"product": "Книга", "quantity": 1.5, "price": 100},
        {"product": "Книга", "quantity": True, "price": 100},
        {"product": "Книга", "quantity": 1, "price": "сто"},
    ],
)
def test_wrong_data_types(order: dict) -> None:
    with pytest.raises(TypeError):
        validate_order(order)


def test_save_order() -> None:
    storage = []
    order = {"product": "Тетрадь", "quantity": 3, "price": 200}

    result = save_order(order, storage)

    assert result == order
    assert len(storage) == 1
    assert storage[0]["product"] == "Тетрадь"


def test_save_invalid_order_does_not_add_it() -> None:
    storage = []
    order = {"product": "Тетрадь", "quantity": 0, "price": 200}

    with pytest.raises(ValueError):
        save_order(order, storage)

    assert storage == []
