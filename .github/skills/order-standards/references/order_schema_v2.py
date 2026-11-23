from pydantic import BaseModel, ConfigDict, Field, field_validator


class Order(BaseModel):
    model_config = ConfigDict(extra="forbid")

    order_id: int = Field(gt=0)
    customer_name: str = Field(min_length=2)
    total: float = Field(gt=0)

    @field_validator("customer_name")
    @classmethod
    def validate_name(cls, value):
        if not value.strip():
            raise ValueError("Имя не должно быть пустым")
        return value
