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
	if data['tamplate'] == 'certificate1' or data['tamplate'] == 'certificate2' or data['tamplate'] == 'certificate3' or data['tamplate'] == 'certificate4':
		pdfGEN(template=data['template'], Certificate=data['Certificate'], FirstName=data['First'], LastName=data['Last'], product="econom")
		if (data['printer'] == "First printer"):
			print("OK1")
			os.system("lpr -P EPSON-1 -# 1 /tmp/{}.pdf".format(data['Certificate'] + data['template'] + "econom"))
		else:
			print("OK2")
			os.system("lpr -P EPSON-2 -# 1 /tmp/{}.pdf".format(data['Certificate'] + data['template'] + "econom"))

		if data["product"] == "standart" or data["product"] == "premium":
			pdfGEN(template=data['template'], Certificate=data['Certificate'], FirstName=data['First'], LastName=data['Last'], product="standart")
			if (data['printer'] == "First printer"):
				print("OK1")
				os.system("lpr -P EPSON-1 -# 1 /tmp/{}.pdf".format(data['Certificate'] + data['template'] + "standart"))
			else:
				print("OK2")
				os.system("lpr -P EPSON-2 -# 1 /tmp/{}.pdf".format(data['Certificate'] + data['template'] + "standart"))
		if data["product"] == "premium":
			pdfGEN(template=data['template'], Certificate=data['Certificate'], FirstName=data['First'], LastName=data['Last'], product="premium")
			if (data['printer'] == "First printer"):
				print("OK1")
				os.system("lpr -P EPSON-1 -# 1 /tmp/{}.pdf".format(data['Certificate'] + data['template'] + "premium"))
			else:
				print("OK2")
				os.system("lpr -P EPSON-2 -# 1 /tmp/{}.pdf".format(data['Certificate'] + data['template'] + "premium"))

	if data['tamplate'] == 'badge1' or data['template'] == 'badge2' or data['tamplate'] == 'badge3' or data['tamplate'] == 'badge4':
		pdfGEN(template=data['template'], Certificate=data['Certificate'], FirstName=data['First'],LastName=data['Last'], product=data['product'])
		if (data['printer'] == "First printer"):
			print("OK1")
			os.system("lpr -P EPSON-1 -# 1 /tmp/{}.pdf".format(data['Certificate'] + data['template'] + data['product']))
		else:
			print("OK2")
			os.system("lpr -P EPSON-2 -# 1 /tmp/{}.pdf".format(data['Certificate'] + data['template'] + data['product']))


if __name__ == '__main__':
	app.run(host='0.0.0.0')

