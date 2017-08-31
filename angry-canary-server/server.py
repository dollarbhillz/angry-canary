from flask import Flask, jsonify, request
from dateutil import parser
from hawkular.metrics import HawkularMetricsClient, MetricType
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# Provides more robust error messages for the purpose of debugging
#app.config['DEBUG'] = True

# Disable track modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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



# Route to add new BuildRuns into the database 
@app.route('/build_run', methods=['POST'])
def build_run_func():

    build_run = BuildRun(builder_name=request.json['builder_name'],
            start_time=parser.parse(request.json['start_time']),
            end_time=parser.parse(request.json['end_time']))

    db.session.add(build_run)

    db.session.commit()

    return "success"



# Route to add new BuildInstances with associated BuildRun
@app.route('/build_instance', methods=['POST'])
def build_instance_func():
   
    build_name = str(request.json['builder_name'])

    build_id = BuildRun.query.filter_by(builder_name=build_name).first().id

    build_instance = BuildInstance(build_run_id=build_id,
            pod_name=request.json['pod_name'],
            start_time=parser.parse(request.json['start_time']),
            end_time=parser.parse(request.json['end_time']))

    db.session.add(build_instance)

    db.session.commit()

    return "success"


# Route to add new BuildInstances with associated BuildRun
@app.route('/build_result', methods=['POST'])
def build_result_func():
   
    pod = str(request.json['pod_name'])

    instance_id = BuildInstance.query.filter_by(pod_name=pod).first().id

    build_result = BuildResult(build_instance_id=instance_id,
            success=request.json['success'],
            reason=request.json['reason'])

    db.session.add(build_result)

    db.session.commit()

    return "success"


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host='127.0.0.1')
