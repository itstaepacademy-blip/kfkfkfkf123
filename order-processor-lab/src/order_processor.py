"""Простая обработка заказов."""

import logging
from typing import Any

logger = logging.getLogger(__name__)


def validate_order(order: dict[str, Any]) -> bool:
    """Проверяет, что заказ содержит правильные данные."""
    if not isinstance(order, dict):
        raise TypeError("Заказ должен быть словарём")

    required_fields = ("product", "quantity", "price")
    for field in required_fields:
        if field not in order:
            raise ValueError(f"Не хватает поля: {field}")

    product = order["product"]
    quantity = order["quantity"]
    price = order["price"]

    if not isinstance(product, str) or not product.strip():
        raise ValueError("Название товара не должно быть пустым")
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise TypeError("Количество должно быть целым числом")
    if quantity <= 0:
        raise ValueError("Количество должно быть больше нуля")
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        raise TypeError("Цена должна быть числом")
    if price <= 0:
        raise ValueError("Цена должна быть больше нуля")

    return True


def save_order(order: dict[str, Any], storage: list[dict[str, Any]]) -> dict[str, Any]:
    """Проверяет заказ и добавляет его в список заказов."""
    validate_order(order)
    saved_order = order.copy()
    storage.append(saved_order)
    logger.info("Заказ сохранён: %s", saved_order["product"])
    return saved_order
