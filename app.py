from flask import Flask, request
from twilio import twiml
import duckduckgo


app = Flask(__name__)

@app.route("/")
def index():

    # Get the text message body sent by Twilio
    search = request.args.get('Body')

    # Grab the ZCI from DuckDuckGo
    text = duckduckgo.get_zci(search, web_fallback=False, urls=False)

    # Make sure the response fits inside one text message
    if len(text) > 160:
        text = text[:157] + '...'

    # Create a TwiML response object
    r = twiml.Response()
    r.sms(text)

    # Return the TwiML
    return str(r)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
