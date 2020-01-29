pkill -f "celery worker" 
pkill -9 -f script.py
python3 myproject.py &
celery -A myproject.celery worker --loglevel=info &
python2 pagekite.py 5000 yeap.pagekite.me
