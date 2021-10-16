from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def login():
    return render_template("login.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["POST"])

def hello():
    name = request.form.get("name")
    lastname = request.form.get("lastname")
    birthday = request.form.get("birthday")
    nacionality = request.form.get("nacionality")
    dni = request.form.get("dni")
    status = request.form.get("status")
    city = request.form.get("city")
    district = request.form.get("district")
    direction = request.form.get("direction")
    postalcode = request.form.get("postalcode")
    phone = request.form.get("phone")
    email = request.form.get("email")

    job = request.form.get("job")
    employer = request.form.get("employer")
    workcity = request.form.get("workcity")
    start = request.form.get("start")
    end = request.form.get("end")
    functions = request.form.get("functions")
    
    namecentereducation = request.form.get("namecentereducation")
    locationcentereducation = request.form.get("locationcentereducation")
    grade = request.form.get("grade")
    fieldstudy = request.form.get("fieldstudy")
    aditionalinformation = request.form.get("aditionalinformation")

    aptitude1 = request.form.get("aptitude1")
    aptitude2 = request.form.get("aptitude2")
    aptitude3 = request.form.get("aptitude3")
    aptitude4 = request.form.get("aptitude4")

    diploma1 = request.form.get("diploma1")
    diploma2 = request.form.get("diploma2")
    diploma3 = request.form.get("diploma3")
    diploma4 = request.form.get("diploma4")
    resume = request.form.get("resume")

    return render_template("hello.html", name=name, lastname=lastname, birthday=birthday, nacionality=nacionality, dni=dni, status=status, city=city, district=district, direction=direction, postalcode=postalcode, phone=phone, email=email, job=job, employer=employer, workcity=workcity, start=start, end=end, functions=functions, namecentereducation=namecentereducation, locationcentereducation=locationcentereducation, grade=grade, fieldstudy=fieldstudy, aditionalinformation=aditionalinformation, aptitude1=aptitude1, aptitude2=aptitude2, aptitude3=aptitude3, aptitude4=aptitude4, diploma1=diploma1, diploma2=diploma2, diploma3=diploma3, diploma4=diploma4, resume=resume)
