from flask import Flask, render_template, request
from utils import get_model
from run_single import encoder, decoder

app = Flask(__name__)
enc, model = get_model(model_name='gpt2')
@app.route("/", methods=["GET"])
def get_form():
    return render_template("form.html")

@app.route("/form", methods=["POST"])
def post_form():
  res = dict(request.form)
  
  try:
	  if res['method'] == 'encrypt':
	    text = encoder(res['message'], res['context'], enc, model)
	  elif res['method'] == 'decrypt':
	  	text = decoder(res['message'], res['context'], enc, model)
	  else: 
	  	text='babalay'
  except Exception as e:
	    text = e
  return render_template("form.html", text=text, context=res['context'])

if __name__ == '__main__':
    app.run(host='0.0.0.0')
