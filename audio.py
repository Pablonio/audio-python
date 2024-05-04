from fastapi import FastAPI, HTTPException, Request
from twilio.rest import Client
from fastapi.responses import JSONResponse

app = FastAPI()

# Configuración de Twilio
account_sid = "AC24a72808ea8d248742bed8cb5422590d"
auth_token = "773eb00dffdc2edb512b0e82aee9c6d3"
twilio_phone_number = "+15087446170"

client = Client(account_sid, auth_token)

def make_call(to: str):
    try:
        # Realizar la llamada utilizando Twilio
        client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',
            to=to,
            from_=twilio_phone_number
        )
    except Exception as e:
        # Manejar errores de Twilio
        raise HTTPException(status_code=500, detail=str(e))

@app.post('/call')
async def call_number(request: Request):
    data = await request.json()
    to = data.get('to')
    if not to:
        raise HTTPException(status_code=400, detail="Falta el número de teléfono 'to' en la solicitud.")
    
    make_call(to)
    return JSONResponse(content={}, status_code=200)

@app.get('/call')
async def call_route():
    make_call('+59175780074')
    return JSONResponse(content={}, status_code=200)
