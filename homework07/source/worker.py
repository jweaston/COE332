# worker.py
import os
import time
from jobs import q, update_job_status

worker_ip = os.environ.get('WORKER_IP')
if not worker_ip:
    raise Exception()

for jid in q.consume():
    update_job_status(jid, 'in progress', worker_ip)
    # todo - replace with real job
    time.sleep(15)
    update_job_status(jid, 'complete', worker_ip)

# @q.worker
# def execute_job(jid):
#     update_job_status(jid, 'in progress')
#     # todo - replace with real job
#     time.sleep(15)
#     update_job_status(jid, 'complete')
