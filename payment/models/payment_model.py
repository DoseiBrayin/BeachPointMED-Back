from pydantic import BaseModel

class PaymentForm(BaseModel):
    x_ref_payco: str
    x_transaction_id: str
    x_amount: str
    x_currency_code: str
    x_signature: str
    numOrder: str
    valueOrder: str
    x_response: str
    x_response_reason_text: str
    x_id_invoice: str
    x_approval_code: str
    x_cod_response: str
