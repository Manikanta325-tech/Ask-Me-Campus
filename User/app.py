import aiml
import os
from flask import Flask, render_template, jsonify, request,redirect, url_for, session



app = Flask(__name__,template_folder='templates')

kernel=aiml.Kernel()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

kernel.learn(os.path.join(BASE_DIR, "User", "std-startup.xml"))
#kernel.learn("./std-startup.xml")
kernel.respond("LOAD AIML B")



@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')




@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():

    if request.method == 'POST':
        the_question = request.form['question']
        print(the_question)

        kernel.resetBrain()
        kernel.learn(os.path.join(BASE_DIR, "User", "std-startup.xml"))
        kernel.respond("load aiml b")

        response = kernel.respond(the_question)
        print(response)

    return jsonify({"response": response })




if __name__ == '__main__':
    app.run(port=5000,debug=True)
