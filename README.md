# celery-rabbitmq-experiments

Local tests for Python, Celery and RabbitMQ

###

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
>>> from tasks import reverse
>>> reverse.delay('iuri')
<AsyncResult: bb4015f7-a1c6-45b6-9788-36a97ad7e681>
```
