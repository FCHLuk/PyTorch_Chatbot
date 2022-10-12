from flask import Flask, render_template, request, jsonify

from chat import get_response, get_no_understand_flag
from email_handler import check_emails, send_email

app= Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text =request.get_json().get("message")
    #TODO: check if text is valid
    no_understand =get_no_understand_flag()
    print ("no_understand is ")
    print ( no_understand )
    if no_understand == True:
      if check_emails (text) == "emails":
        send_email (text)
        message = {"answer":"Thank you! Someone will get back to you"}
        return jsonify(message)
      else:
        response = get_response(text)    
    else:
      response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
  #  app.run(debug=False, host='0.0.0.0', port=8888)
