from payment.models.payment_model import PaymentForm
from hashlib import sha256
from helpers import createEventsCalendar
import json

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

    # x_extra1 is the courts that the user selected
    courts = json.loads(form.x_extra1)
    name = form.x_customer_name
    lastname = form.x_customer_lastname

    # if x_signature == signature:
    print(form.x_extra1)
    if form.x_cod_response:
        courts = json.loads(form.x_extra1)
    else:
        return {"error": "Firma no valida"}
    x_cod_response = form.x_cod_response
    if x_cod_response == '1':
        print("transacción aprobada")
        for court in courts['courts']:
            event = {
                'summary': f'Reserva de cancha de {name} {lastname}',
                'start': f"{court['date']}T{court['hour']}:00:00-05:00",
                'end': f"{court['date']}T{court['hour'] + 1}:00:00-05:00",
                'time_zone': 'America/Chicago',
                'court': court['description']
            }
            createEventsCalendar.create_events_calendar(event)
        return {"message": "transacción aprobada"}
    elif x_cod_response == '2':
        print("transacción rechazada")
        return {"error": "transacción rechazada"}
    elif x_cod_response == '3':
        print("transacción pendiente")
        return {"error": "transacción pendiente"}
    else:
        print("transacción fallida")
        return {"error": "transacción fallida"}
    # else:
    #     print("Firma no valida")
    #     return {"error": "Firma no valida"}
