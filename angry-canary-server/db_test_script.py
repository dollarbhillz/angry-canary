from server import db
from server import BuildRun
from server import BuildInstance
from server import BuildResult
from datetime import datetime

db.create_all()

success_run = BuildRun(builder_name="success_run",start_time=datetime.utcnow(),
        end_time=datetime.utcnow())

success_instance_1 = BuildInstance(build_run_id=success_run.id, 
        pod_name="s_pod_1", start_time=datetime.utcnow(),
        end_time=datetime.utcnow())

success_instance_2 = BuildInstance(build_run_id=success_run.id,
        pod_name="s_pod_2", start_time=datetime.utcnow(), 
        end_time=datetime.utcnow())

success_instance_3 = BuildInstance(build_run_id=success_run.id,
        pod_name="s_pod_3", start_time=datetime.utcnow(), 
        end_time=datetime.utcnow())


success_result_1 = BuildResult(build_instance_id=success_instance_1.id, 
        success=True, reason="it worked")

success_result_2 = BuildResult(build_instance_id=success_instance_2.id, 
        success=True, reason="it worked")

success_result_3 = BuildResult(build_instance_id=success_instance_3.id, 
        success=True, reason="it worked")

db.session.add(success_run)

db.session.add(success_instance_1)
db.session.add(success_instance_2)
db.session.add(success_instance_3)

db.session.commit()
