from pydantic import BaseModel, ConfigDict, Field, field_validator


class RefundRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    order_id: int = Field(gt=0)
    reason: str = Field(min_length=10)
    refund_amount: float = Field(gt=0)

    @field_validator("reason")
    @classmethod
    def validate_reason(cls, value):
        if not value.strip():
            raise ValueError("Причина возврата не может быть пустой")
        return value
