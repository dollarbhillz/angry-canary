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
class Build_Results(db.Model):
    __tablename__='build_results'

    id = db.Column(db.Integer, primary_key=True)

    # relates to id of build_runs table
    build_runs_id = db.Column(db.Integer, db.ForeignKey('build_runs.id'))
    build_runs = db.relationship('Build_Runs',
            backref=db.backref('build_results', lazy='dynamic'))

    # relates to id of builder_instances table
    build_instances_id = db.Column(db.Integer, db.ForeignKey('build_instances.id'))
    build_instances = db.relationship('Build_Instances',
            backref=db.backref('build_results', lazy='dynamic'))


    success = db.Column(db.Boolean)

    reason = db.Column(db.String(50))


    def __init__(self, build_runs_id, build_runs, build_instances_id,
                 build_instances, success, reason):

        self.build_runs_id = build_runs_id
        self.build_runs = build_runs
        self.build_instances_id = build_instances
        self.success = success
        self.reason = reason

    def __repr__(self):
        return '<build_results %d>' % self.id


# Schema defining data about a particualr run of a build
class Build_Runs(db.Model):
    __tablename__='build_runs'

    id = db.Column(db.Integer, primary_key=True)
    builder_name = db.Column(db.String(50))
    start_time = db.Column(db.Integer)
    end_time = db.Column(db.Integer)

    def __init__(self, builder_name, start_time, end_time):
        self.builder_name = builder_name
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return '<build_results %d>' % self.id


# Schema defining data about a particualr instance of a build
class Build_Instances(db.Model):
    __tablename__='build_instances'

    id = db.Column(db.Integer, primary_key=True)

    # relates to id of build_runs table
    build_run_id = db.Column(db.Integer, db.ForeignKey("build_runs.id"))
    build_run = db.relationship("Build_Runs", backref=db.backref('build_runs',
        lazy='dynamic'))

    podname = db.Column(db.String(50))
    start_time = db.Column(db.Integer)
    end_time = db.Column(db.Integer)

    def __init__(self, build_run_id, podname, start_time, end_time):
        self.build_run_id = build_run_id
        self.podname = podname
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return '<build_instances %d>' % self.id


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
