from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Provides more robust error messages for the purpose of debugging
app.config['DEBUG'] = True

# SQLAlchemy Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://angry-canary-app-admin:password@localhost:5432/test'
db = SQLAlchemy(app)


# Schema defining results of a particular build
# Plural?, Camel Case?
class BuildResult(db.Model):
    __tablename__='build_result'

    id = db.Column(db.Integer, primary_key=True)

    # relationship to builder_instance id
    build_instance_id = db.Column(db.Integer, db.ForeignKey('build_instance.id'))

    success = db.Column(db.Boolean)

    reason = db.Column(db.String(50))

    def __repr__(self):
        return '<build_result %d>' % self.id



# Schema defining data about a particualr run of a build
class BuildRun(db.Model):
    __tablename__='build_run'

    id = db.Column(db.Integer, primary_key=True)
    builder_name = db.Column(db.String(50))

    #change to db.DateTime type
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)

    build_instance = db.relationship('BuildInstance', backref='build_run')

    def __repr__(self):
        return '<build_run %d>' % self.id



# Schema defining data about a particualr instance of a build
class BuildInstance(db.Model):
    __tablename__='build_instance'

    id = db.Column(db.Integer, primary_key=True)

    # relates to id of build_run table
    build_run_id = db.Column(db.Integer, db.ForeignKey('build_run.id'))


    pod_name = db.Column(db.String(50))

    #change to db.DateTime type
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)

    build_result = db.relationship('BuildResult',
            backref='build_instance', uselist=False)

    def __repr__(self):
        return '<build_instance %d>' % self.id


# Route hit by worker pods on success of busy work
@app.route('/success')
def success_query():
    return "nice jorb"




# Route hit by worker pods on failure of busy work
@app.route('/fail')
def fail_query():
    return "ur dumb"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
