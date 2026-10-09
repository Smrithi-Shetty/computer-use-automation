from pydantic import BaseModel

class CapabilityInput(BaseModel):
    employee_name: str

class CapabilityOutput(BaseModel):
    success: bool
    employee_id: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    message: str | None = None