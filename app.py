"""
SOURCES:
#https://www.youtube.com/watch?v=Z1RJmh_OqeA&ab_channel=freeCodeCamp.org
#https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
#https://stackoverflow.com/questions/27539309/how-do-i-create-a-link-to-another-html-page
"""
from flask import Flask, render_template, flash, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/'
ALLOWED_EXTENSIONS = {'gpx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#set up route to base of app?
@app.route('/' , methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.files)
        # check if post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            print("this")
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('no selected file')
            print("that")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(file.filename)
            print("shit got put into " + UPLOAD_FOLDER)
            #return redirect(url_for('uploaded_file', filename=filename))
            return render_template('index.html')
        else:
            return render_template('submiterror.html')

    # show the form, it wasn't submitted
    return render_template('index.html')

"""
@app.route('/cool_form', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('cool_form.html')
"""

if (__name__ == "__main__"):
    app.secret_key = os.urandom(24)
    #app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug = True)