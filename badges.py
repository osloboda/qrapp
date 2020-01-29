from pdfgeneratorapi import PDFGenerator
from flask import Flask, request
import urllib.request
import os.path

app = Flask(__name__)

pdf_client = PDFGenerator(api_key='3b15840d3d328bfc401f3d2836c22e7f85ae0c65e1021caa75f089b15d982656', api_secret='61f7a3d8a339211f317c4cec69e15613c702cc3955172371ed8b38f9e82be656')
pdf_client.set_workspace('oleg.slobodyanyuk@pain.in.ua')

@app.route('/')
def going():
    content = {"Certificate": request.args.get('Certificate'), "First": request.args.get('first'), "Last": request.args.get('last'), "template": request.args.get('template'), "printer": request.args.get('printer'), "bus": request.args.get("bus")}
    new_pdf = pdf_client.create_document(template_id=content['template'], data=content, document_format="pdf", response_format="url")
    urllib.request.urlretrieve(new_pdf.response, '/home/osloboda/Рабочий стол/cappadocia3/{}.pdf'.format(str(content["Last"]) + " " + str(content["Certificate"])))
    if True == os.path.exists('/home/osloboda/Рабочий стол/cappadocia3/{}.pdf'.format(str(content["Last"]) + " " + str(content["Certificate"]))):
        return "OK"
    else:
        return "NOOOOOOOOOOOOOOOOOO"

if __name__ == '__main__':
	app.run()

