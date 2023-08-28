# Necessary imports
import os
import io
from werkzeug.utils import secure_filename

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    String,
    LargeBinary
)

from flask import (
    Flask,
    request,
    render_template,
    abort,
    send_file,
    make_response
)

# Initializing Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
db = SQLAlchemy(app)

# Creating the SQLAlchemy model for the file table
class File(db.Model):
    __tablename__ = 'file'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime(timezone=True), server_default=func.now())
    name = Column(String(100), nullable=False)
    data = Column(LargeBinary, nullable=False)

# Creating the table in the database
with app.app_context():
    db.create_all()

# Registering the internal server error (500 code) handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.jinja'), 500

# Index route allows user to upload new files as well as to see and download
# any files already present in the database
@app.route('/', methods=['GET', 'POST'])
def index():
    files = None

    try:
        if request.method == 'POST':
            for file in request.files.getlist('files'):
                obj = File(name=secure_filename(file.filename), data=file.read())
                db.session.add(obj)
            
            db.session.commit()

        files = [(x.id, x.name, x.date) for x in db.session.query(File).all()]

    except Exception as e:
        print(e)
        abort(500)
    
    return render_template('index.jinja', files=files)

# Download route handles file downloads
@app.route('/download/<id>', methods=['GET'])
def download(id):
    obj = db.session.query(File).filter(File.id == id).first()
    return send_file(io.BytesIO(obj.data), download_name=obj.name, as_attachment=True)

# Running the Flask app on all hosts (important for Docker)
if __name__ == '__main__':
    app.run(host='0.0.0.0')
