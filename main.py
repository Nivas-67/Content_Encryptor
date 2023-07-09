from flask import Flask, render_template
from flask import request
from cipher import CaeserCipher

cipher = CaeserCipher()
app = Flask(__name__, template_folder="templates")

@app.route('/',methods=['GET'])
def MyhomeRoot():
    return render_template('login.html')   

def read_credentials(username, password):
    with open('password.txt', 'r') as file:
        for line in file:
            new_field = line.split("*")
            full_field = new_field[0].split("|")
            stored_username = full_field[0]
            stored_password = full_field[1]
            if username == stored_username and password == stored_password:
                return True
    return False

@app.route('/login',methods=["GET", "POST"])
def login():
    username=request.form["username"]
    password = request.form["password"]
    if read_credentials(username, password):
        return render_template('home1.html')
    else:
        return render_template('error.html')
    
@app.route('/signup',methods=["GET", "POST"])
def signup():
    username=request.form["username"]
    password = request.form["password"]
    with open("password.txt", "a") as file:
        file.write(f"{username}|{password}*\n") 
    return render_template('home.html')
    
@app.route('/encrypt', methods=["GET","POST"])
def encrypt():
    efile = request.form["file"]
    cipher.encrypt(efile)
    return render_template('success.html')

@app.route('/decrypt',methods=["GET","POST"])
def decrypt():
    dfile = request.form["dfile"]
    num = request.form["key_num"]
    value = cipher.decrypt(dfile,num,key_val)
    if value < 1:
        return render_template('error.html')
    else:
        return render_template('success.html')

@app.route('/save',methods=["GET","POST"])
def save():
    text_in = request.form["text_input"]
    global key_val 
    key_val= request.form["key_value"]
    name = request.form["file_name"]
    cipher.save(input_text=text_in,key_num=key_val,file_name=name)
    if(len(text_in)==0 or len(key_val)==0 or len(name)==0):
        return render_template('error.html')
    else:
        return render_template('home1.html')

if __name__ == '__main__':
    app.run(debug=True)