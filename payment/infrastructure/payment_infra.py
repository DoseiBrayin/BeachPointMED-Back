from payment.models.payment_model import PaymentForm
from hashlib import sha256

async def payment(form: PaymentForm):
    p_cust_id_cliente = '1451626'
    p_key = 'b703746c916ac81495da8c19bc43c0871421815c'

    x_ref_payco = form.x_ref_payco
    x_transaction_id = form.x_transaction_id
    x_amount = form.x_amount
    x_currency_code = form.x_currency_code
    x_signature = form.x_signature

    signature = sha256(f'{p_cust_id_cliente}^{p_key}^{x_ref_payco}^{x_transaction_id}^{x_amount}^{x_currency_code}'.encode()).hexdigest()

    x_response = form.x_response
    x_motivo = form.x_response_reason_text
    x_id_invoice = form.x_id_invoice
    x_autorizacion = form.x_approval_code

    if x_signature == signature:
        x_cod_response = form.x_cod_response
        if x_cod_response == '1':
            return {"message": "transacción aceptada"}
        elif x_cod_response == '2':
            return {"message": "transacción rechazada"}
        elif x_cod_response == '3':
            return {"message": "transacción pendiente"}
        else:
            return {"message": "transacción fallida"}
    else:
        return {"message": "Firma no valida"}