from flask import Flask, render_template, request, redirect, session, flash, url_for
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import mysql.connector

app = Flask(__name__)
app.secret_key = "secret"

UPLOAD_FOLDER = "static/uploads/"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the model
model = load_model("model/vgg16_skin_cancer.h5")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="skin_cancer_db"
)

cursor = db.cursor(dictionary=True, buffered=True)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (user, pwd))
        result = cursor.fetchone()

        if result:
            session["user"] = user
            flash("Connexion réussie ✔", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Identifiants incorrects ✘", "danger")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if "user" not in session:
        return redirect(url_for("login"))
    
    if request.method == "POST":
        try:
            name = request.form["name"]
            age = request.form["age"]
            file = request.files["image"]

            if file.filename == "":
                flash("Veuillez choisir une image", "warning")
                return redirect(url_for("predict"))

            filename = file.filename.replace(" ", "_") 
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)

           
            img = image.load_img(path, target_size=(224, 224))
            img = image.img_to_array(img) / 255.0
            img = np.expand_dims(img, axis=0)

            pred = float(model.predict(img)[0][0])
            
           
            if pred > 0.5:
                result = "Maligne"
                confidence = round(pred * 100, 2)
            else:
                result = "Bénigne"
                confidence = round((1 - pred) * 100, 2)

           
            web_img_path = f"uploads/{filename}"
            query = """
                INSERT INTO patients (name, age, result, probability, image_path)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (name, age, result, confidence, web_img_path))
            db.commit()

            flash("Analyse effectuée avec succès ✔", "success")
            
            return render_template("results.html", 
                                   result=result, 
                                   prob=confidence, 
                                   img=web_img_path)

        except Exception as e:
            print(f"Error: {e}")
            flash("Erreur lors du traitement système ✘", "danger")
            return redirect(url_for("predict"))

    return render_template("predict.html")

@app.route("/patients")
def patients():
    if "user" not in session:
        return redirect(url_for("login"))
    
    
    local_cursor = db.cursor(dictionary=True)
    local_cursor.execute("SELECT * FROM patients ORDER BY id DESC")
    all_patients = local_cursor.fetchall()
    return render_template("patients.html", patients=all_patients)

@app.route("/logout")
def logout():
    session.clear()
    flash("Vous avez été déconnecté", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)