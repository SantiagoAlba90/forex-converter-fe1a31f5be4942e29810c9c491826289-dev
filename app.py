from flask import Flask, render_template, request, flash
from forex_python.converter import CurrencyRates, CurrencyCodes

# start app
app = Flask(__name__)
app.secret_key = 'your_secret_key_here' #make sure to replace later sant

c = CurrencyRates
cc = CurrencyCodes

def home():
    if request.method == 'POST':
        from_currency = request.form.get('from_currency').upper()
        to_currency = request.form.get('to_currency').upper()
        amount_str = request.form.get('amount')

    if len(from_currency) !=3 or not from_currency.isaplha() or len(to_currency) != 3 or not to_currency.isaplha():
        flash("Invalid currency codes. Please use three letter code!", 'error')
        return render_template('index.html')
    
    try:
        amount = float(amount.str)
    except ValueError:
        flash("invalid amount input. Enter a valid number.", 'error')
        return render_template('index.html')
    
    response = requests.get(f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}")
        if response.status_code == 200:
            data = response.json()
            if 'result' in data:
                converted_amount = data['result']
                flash(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}", 'success')
            else:
                flash("Conversion failed due to an unknown error.", 'error')
        else:
            flash("API request failed. Please try again later.", 'error')

return render_template('index.html')


if