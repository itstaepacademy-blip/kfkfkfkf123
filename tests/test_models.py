import pytest
from pydantic import ValidationError
from src.models import RefundRequest



def test_valid_refund():
    refund = RefundRequest(
        order_id=1,
        reason="Товар пришел с повреждением",
        refund_amount=500,
    )
    assert refund.order_id == 1
    assert refund.refund_amount == 500



def test_short_reason():
    with pytest.raises(ValidationError):
        RefundRequest(order_id=1, reason="Плохо", refund_amount=500)



def test_invalid_amount():
    with pytest.raises(ValidationError):
        RefundRequest(order_id=1, reason="Хочу вернуть товар обратно", refund_amount=0)
