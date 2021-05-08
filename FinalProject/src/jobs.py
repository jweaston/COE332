# jobs.py
import uuid 
import os
from hotqueue import HotQueue
from redis import StrictRedis

redis_ip = os.environ.get('REDIS_IP')
if not redis_ip:
    raise Exception()


q = HotQueue("queue", host=redis_ip, port=6379, db=1)
jobdb = StrictRedis(host=redis_ip, port=6379, db=0)
propertydb = StrictRedis(host=redis_ip, port=6379, db=2)


def _generate_jid():
    return str(uuid.uuid4())

def _generate_job_key(jid):
    return 'job.{}'.format(jid)

def _instantiate_job(jid, status, jtype, selector):
    if type(jid) == str:
        return {'id': jid,
                'status': status,
                'jtype': jtype,
                'selector': selector
        }
    return {'id': jid.decode('utf-8'),
            'status': status.decode('utf-8'),
            'jtype': jtype.decode('utf-8'),
            'selector': selector.decode('utf-8')
    }

def _save_job(job_key, job_dict):
    """Save a job object in the Redis database."""
    jobdb.hmset(job_key, job_dict)

def _queue_job(jid):
    """Add a job to the redis queue."""
    q.put(jid)

def add_job(jtype, selector, status="submitted"):
    """Add a job to the redis queue."""
    jid = _generate_jid()
    job_dict = _instantiate_job(jid, status, jtype, selector)
    # update call to save_job:
    _save_job(_generate_job_key(jid), job_dict)
    # update call to queue_job:
    _queue_job(jid)
    return job_dict

def update_job_status(jid, new_status, worker_ip):
    """Update the status of job with job id `jid` to status `status`."""
    jid, status, jtype, selector = jobdb.hmget(_generate_job_key(jid), 'id', 'status', 'jtype', 'selector')
    job = _instantiate_job(jid, status, jtype, selector)
    if job:
        job['status'] = new_status
        job['worker_ip'] = worker_ip
        _save_job(_generate_job_key(job['id']), job)
    else:
        raise Exception()
