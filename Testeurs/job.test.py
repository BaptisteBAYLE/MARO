import sys
sys.path.append('./src')
from job import Job



job = Job(0, [54, 79, 16, 66, 58])

## Test 1 ##
if job.duree == [54, 79, 16, 66, 58]:
    print('test job #1 passed')
else:
    print('test job #1 failed')

## Test 2 ##
job.set_debut(0, 10)
if job.debut == [10] + [None] * 4:
    print('test job #2 passed')
else:
    print('test job #2 failed')
