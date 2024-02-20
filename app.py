from flask import Flask, render_template, request, url_for, flash, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'website'
app.config['SESSION_TYPE'] = ''
app.config['SECRET_KEY'] = 'super secret key'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template("index.html");


@app.route('/about')
def about():
    return render_template("about.html");


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    status = True
    if request.method == "POST":
        details = request.form
        name = details['name']
        email = details['email']
        number = details['number']
        message = details['message']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contact(name, email, number, message) VALUES (%s, %s, %s, %s)",
                    (name, email, number, message))
        mysql.connection.commit()
        cur.close()
        return render_template("contact.html");
    else:
        return render_template("contact.html");


@app.route('/course')
def course():
    return render_template("course.html");


@app.route('/notice', methods=['POST', 'GET'])
def notice():
    status = True
    if request.method == "POST":
        details = request.form
        image = 'static/images/notice/' + details['image']
        descr = details['descr']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO notice(image, description) VALUES (%s, %s)", (image, descr))
        mysql.connection.commit()
        cur.close()
        return render_template('notice.html');
    else:
        return render_template('notice.html');


@app.route('/webinar', methods=['POST', 'GET'])
def webinar():
    status = True
    if request.method == "POST":
        details = request.form
        name = details['name']
        image = 'static/images/webinar/' + details['image']
        image1 = 'static/images/webinar/' + details['image1']
        image2 = 'static/images/webinar/' + details['image2']
        image3 = 'static/images/webinar/' + details['image3']
        descr = details['descr']
        guest = details['guest']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO webinar(name, image, image1, image2, image3, description, guest) VALUES (%s, %s, %s, %s, %s, %s, %s)", (name, image, image1, image2, image3, descr, guest))
        mysql.connection.commit()
        cur.close()

        return render_template('webinar.html');
    else:
        return render_template('webinar.html');


@app.route('/feedback', methods=['POST', 'GET'])
def feedback():
    status = True
    if request.method == "POST":
        details = request.form
        name = details['name']
        contact_no = details['contact']
        email = details['email']
        feedbacks = details['feedback']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO feedback(name, contact_no, email, feedback) VALUES (%s, %s, %s, %s)",
                    (name, contact_no, email, feedbacks))
        mysql.connection.commit()
        cur.close()
        flash('Submited', 'success')
        return redirect(url_for('feedback'))
    return render_template('feedback.html');


@app.route('/technoparv', methods=['POST', 'GET'])
def technoparv():
    status = True
    if request.method == "POST":
        details = request.form
        year = details['year']
        image = 'static/images/technoparv/' + details['image']
        image1 = 'static/images/technoparv/' + details['image1']
        image2 = 'static/images/technoparv/' + details['image2']
        image3 = 'static/images/technoparv/' + details['image3']
        image4 = 'static/images/technoparv/' + details['image4']
        image5 = 'static/images/technoparv/' + details['image5']
        image6 = 'static/images/technoparv/' + details['image6']
        image7 = 'static/images/technoparv/' + details['image7']
        image8 = 'static/images/technoparv/' + details['image8']
        image9 = 'static/images/technoparv/' + details['image9']
        image10 = 'static/images/technoparv/' + details['image10']
        image11 = 'static/images/technoparv/' + details['image11']
        descr = details['descr']
        guest = details['guest']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO technoparv(year, image, image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, descr, guest) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (year, image, image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, descr, guest))
        mysql.connection.commit()
        cur.close()
        return render_template("technoparv.html");
    else:
        return render_template("technoparv.html");


@app.route('/placement', methods=['POST', 'GET'])
def placement():
    status = True
    if request.method == "POST":
        details = request.form
        student_name = details['stud_name']
        company_name = details['company_name']
        image = 'static/images/placement/' + details['image']
        descr = details['descr']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO placement(student_name, company_name, image, description) VALUES (%s, %s, %s, %s)",
                    (student_name, company_name, image, descr))
        mysql.connection.commit()
        cur.close()
        return render_template('placement.html');
    else:
        return render_template('placement.html');


@app.route('/addevents')
def addevents():
    return render_template("addevents.html");

# login page
@app.route('/login', methods=['POST', 'GET'])
def login():
    status = True
    if request.method == "POST":
        details = request.form
        upass = details['upass']
        name = details['Name']
        if ((name=="Admin") and (upass=="Password")):
            return render_template('homepage.html');
        else:
            return render_template('index.html');
    else:
        return render_template('index.html');


@app.route('/homepage')
def homepage():
    return render_template("homepage.html");


@app.route('/noticeview', methods=['POST', 'GET'])
def noticeview():
    cur = mysql.connection.cursor();
    cur.execute("select * from notice");
    data = cur.fetchall();
    return render_template('notice_view.html', value=data);


@app.route('/eventview', methods=['POST', 'GET'])
def eventview():
    return render_template('event_view.html');

@app.route('/placementview', methods=['POST', 'GET'])
def placementview():
    cur = mysql.connection.cursor();
    cur.execute("select * from placement");
    data = cur.fetchall();
    return render_template('placement_view.html', value=data);


@app.route('/webinarview', methods=['POST', 'GET'])
def webinarview():
    cur = mysql.connection.cursor();
    cur.execute("select * from webinar");
    data = cur.fetchall();
    return render_template('webinar_view.html', value=data);

@app.route('/technoparvview', methods=['POST', 'GET'])
def technoparvview():
    cur = mysql.connection.cursor();
    cur.execute("select * from technoparv");
    data = cur.fetchall();
    return render_template('technoparv_view.html', value=data);

@app.route('/feedbackview', methods=['POST', 'GET'])
def feedbackview():
    cur = mysql.connection.cursor();
    cur.execute("select * from feedback");
    data = cur.fetchall();
    return render_template('feedback_view.html', value=data);

@app.route('/contactview', methods=['POST', 'GET'])
def contactview():
    cur = mysql.connection.cursor();
    cur.execute("select * from contact");
    data = cur.fetchall();
    return render_template('contact_view.html', value=data);


# main driver function
if __name__ == '__main__':
    app.debug = True
    app.run()



