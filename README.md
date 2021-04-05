# Celery Rabbitmq Experiments

Local tests for Python, Celery and RabbitMQ

#### How to use

1. Install Celery 

```
cd [root project]
python3 -m venv venv
source venv/bin/activate
pip install celery
```

2. Deploy and start local RabbitMQ

```
docker run -d --hostname localhost --name local-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```

Check web interface at: http://localhost:15672/ (guest:guest)

3. Run celery for the tasks 

```
cd [root project]
celery -A tasks worker --loglevel=info
```

4. Open a new terminal and test it:

```
cd [root project]
source venv/bin/activate
python
from tasks import reverse
from time import sleep
result = reverse.delay('iuri'); result.status; sleep(6); result.status
```

#### Acknowledgements
Thanks to Pretty Printed at [https://www.youtube.com/watch?v=THxCy-6EnQM](https://www.youtube.com/watch?v=THxCy-6EnQM)