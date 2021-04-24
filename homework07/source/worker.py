# worker.py
import time
from jobs import q, update_job_status


for jid in q.consume():
    update_job_status(jid, 'in progress')
    # todo - replace with real job
    time.sleep(15)
    update_job_status(jid, 'complete')
# @q.worker
# def execute_job(jid):
#     update_job_status(jid, 'in progress')
#     # todo - replace with real job
#     time.sleep(15)
#     update_job_status(jid, 'complete')
