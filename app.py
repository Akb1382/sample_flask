from flask import Flask ,redirect , url_for , request , render_template , json

app = Flask(__name__)

@app.route("/")

@app.route("/login/" , methods = ['GET','POST'])
def login() :
    if request.method == "POST" :
        #username = request.args.get('username')
        #email = request.args.get('email')
        username = request.form['username']
        email = request.form['email']
        StudentNumber = request.form['StudentNumber']
        data = {
            'username':username,
            'email':email,
            'StudentNumber':StudentNumber
        }
    with open('data.json' , 'w') as file :
        json.dump(data,file)

    return f"login page - username : {username} and email : {email} and StudentNumber : {StudentNumber}"

if __name__ == "__main__" :
    app.run(debug = True)
