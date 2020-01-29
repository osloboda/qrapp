import os
from flask import Flask, request
from celery_app import make_celery
from Paincontrol_certificate import pdfGEN

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://guest@localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'amqp://guest@localhost//'
celery = make_celery(app)

@app.route('/')
def parse():
	content = {"Certificate": request.args.get('Certificate'), "First": request.args.get('first'), "Last": request.args.get('last'), "template": request.args.get('template'), "printer": request.args.get('printer'), "product": request.args.get('product')}
	process.delay(content)
	return "OK"

@celery.task(name='app_route.process')
def process(data):
	pdfGEN(template=data['template'], Certificate=data['Certificate'], FirstName=data['First'], LastName=data['Last'], product=data['product'])
	if (data['printer'] == "First printer"):
		print("OK1")
		os.system("lpr -P EPSON-1 -# 1 /tmp/{}.pdf".format(data['Certificate'] + data['template']))
	else:
		print("OK2")
		os.system("lpr -P EPSON-2 -# 1 /tmp/{}.pdf".format(data['Certificate'] + data['template']))
	return "OK"

if __name__ == '__main__':
	app.run(host='0.0.0.0')

