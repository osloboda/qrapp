from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Paragraph, Table
from reportlab.lib import colors
from reportlab.lib.enums import *
from reportlab.lib.colors import blue
from reportlab.pdfbase import pdfmetrics 
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.barcode import code39, code128, code93
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
from qr import QrCodeWidget

def pdfGEN(template, Certificate, LastName, FirstName, product):
    pdfmetrics.registerFont(TTFont('OpenSans', 'OpenSans-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSansCondensed.ttf'))
    pdfmetrics.registerFont(TTFont('OpenSans2', 'OpenSans-Bold.ttf'))
    c = canvas.Canvas('/tmp/{}.pdf'.format(Certificate + template), pagesize=A4, bottomup=False)  # alternatively use bottomup=False
    width, height = A4
    c.setFillColorRGB(0,0,255)

    if template == "certificate":
        TEXT = """дійсно брав(ла) участь у
        Всеукраїнському міждисциплінарному практично-орієнтованому тренінгу "PainControl - мистецтво
        контролювати біль" 30 січня 2020 року у м. Івано-Франківськ
        та отримав(ла) 15 балів безперервного професійного розвитку"""

        styles = getSampleStyleSheet()
        ptext = "№ " + Certificate  # № CERTIFICATE
        style = styles["Normal"]
        style.alignment = 1
        style.fontName = "OpenSans"
        style.fontSize = 20
        style.textColor = blue
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 160*mm, 50*mm)
        p.drawOn(c, 24*mm, 138*mm)

        ptext = "підтверджує те, що"
        style.fontSize = 18
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 160*mm, 50*mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 24*mm, 147*mm)    # position of text / where to draw

        ptext = LastName
        style.fontName = "DejaVuSans"
        style.fontSize = 38
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 160*mm, 50*mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 24*mm, 174*mm)    # position of text / where to draw

        ptext = FirstName
        style.fontSize = 32
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 160*mm, 15*mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 24*mm, 188*mm)    # position of text / where to draw

        style.fontName = "OpenSans"
        style.fontSize = 14
        style.leading = 20
        p = Paragraph(TEXT, style=style)
        p.wrapOn(c, 160*mm, 100*mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 24*mm, 172*mm)  # size of 'textbox' for linebreaks etc.

        qr_code = QrCodeWidget("https://pain.in.ua/checkcert/?cert=" + Certificate)
        bounds = qr_code.getBounds()
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
        d = Drawing(65, 65, transform=[65./width,0,0,65./height,0,0])
        d.add(qr_code)
        renderPDF.draw(d, c, 170*mm, 260*mm)

        c.save()

    if template == "certificate1":
        cert = Certificate
        if product == "econom":
            cert += "1"
            TEXT = """дійсно брав(ла) участь у 
            практично-орієнтованому тренінгу
            “Зимова школа з діагностики болю”
            31 січня-2 лютого 2020 року, м. Яремче
            та отримав(ла) 25 балів до свого
            портфоліо безперервної професійної освіти"""
        if product == "standart":
            cert += "2"
            TEXT = """дійсно брав(ла) участь у
            тренінгу з оволодіння практичними навичками
            “Суглобовий синдром: діагностика та лікування”
            31 січня 2020 року, м. Яремче
            та отримав(ла) 15 балів до свого
            портфоліо безперервної професійної освіти"""
        if product == "premium":
            cert += "3"
            TEXT = """дійсно брав(ла) участь у
            тренінгу з оволодіння практичними навичками
            “Застосування препаратів канабісу в медицині болю”
            2 лютого 2020 року, м. Яремче
            та отримав(ла) 15 балів до свого
            портфоліо безперервної професійної освіти"""

        styles = getSampleStyleSheet()
        ptext = "№ " + cert # № CERTIFICATE
        style = styles["Normal"]
        style.alignment = 1
        style.fontName = "OpenSans"
        style.fontSize = 20
        style.textColor = blue
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 160*mm, 50*mm)
        p.drawOn(c, 24*mm, 138*mm)

        ptext = "підтверджує те, що"
        style.fontSize = 18
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 160*mm, 50*mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 24*mm, 147*mm)    # position of text / where to draw

        ptext = LastName
        style.fontName = "DejaVuSans"
        style.fontSize = 38
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 160*mm, 50*mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 24*mm, 174*mm)    # position of text / where to draw

        ptext = FirstName
        style.fontSize = 32
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 160*mm, 15*mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 24*mm, 188*mm)    # position of text / where to draw

        style.fontName = "OpenSans"
        style.fontSize = 14
        style.leading = 20
        p = Paragraph(TEXT, style=style)
        p.wrapOn(c, 160*mm, 100*mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 24*mm, 172*mm)  # size of 'textbox' for linebreaks etc.

        qr_code = QrCodeWidget("https://pain.in.ua/checkcert/?cert=" + cert)
        bounds = qr_code.getBounds()
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
        d = Drawing(65, 65, transform=[65./width,0,0,65./height,0,0])
        d.add(qr_code)
        renderPDF.draw(d, c, 170*mm, 260*mm)

        c.save()

    if template == "certificate2":
        cert = Certificate
        if product == "econom":
            cert += "1"
            TEXT = """дійсно брав(ла) участь у 
               практично-орієнтованому тренінгу
               “Зимова школа з діагностики болю”
               2-4 лютого 2020 року, м. Яремче
               та отримав(ла) 25 балів до свого
               портфоліо безперервної професійної освіти"""
        if product == "standart":
            cert += "2"
            TEXT = """дійсно брав(ла) участь у
            тренінгу з оволодіння практичними навичками
            “Застосування препаратів канабісу в медичній практиці”
            3 лютого 2020 року, м. Яремче
            та отримав(ла) 15 балів до свого
            портфоліо безперервної професійної освіти"""
        if product == "premium":
            cert += "3"
            TEXT = """дійсно брав(ла) участь у
            тренінгу з оволодіння практичними навичкамиі
            “Больовий синдром в практиці ревматолога”
            4 лютого 2020 року, м. Яремче
            та отримав(ла) 15 балів до свого
            портфоліо безперервної професійної освіти"""

        styles = getSampleStyleSheet()
        ptext = "№ " + cert  # № CERTIFICATE
        style = styles["Normal"]
        style.alignment = 1
        style.fontName = "OpenSans"
        style.fontSize = 20
        style.textColor = blue
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 160 * mm, 50 * mm)
        p.drawOn(c, 24 * mm, 138 * mm)

        ptext = "підтверджує те, що"
        style.fontSize = 18
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 160 * mm, 50 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 24 * mm, 147 * mm)  # position of text / where to draw

        ptext = LastName
        style.fontName = "DejaVuSans"
        style.fontSize = 38
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 160 * mm, 50 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 24 * mm, 174 * mm)  # position of text / where to draw

        ptext = FirstName
        style.fontSize = 32
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 160 * mm, 15 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 24 * mm, 188 * mm)  # position of text / where to draw

        style.fontName = "OpenSans"
        style.fontSize = 14
        style.leading = 20
        p = Paragraph(TEXT, style=style)
        p.wrapOn(c, 160 * mm, 100 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 24 * mm, 172 * mm)  # size of 'textbox' for linebreaks etc.

        qr_code = QrCodeWidget("https://pain.in.ua/checkcert/?cert=" + cert)
        bounds = qr_code.getBounds()
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
        d = Drawing(65, 65, transform=[65. / width, 0, 0, 65. / height, 0, 0])
        d.add(qr_code)
        renderPDF.draw(d, c, 170 * mm, 260 * mm)

        c.save()

    if template == "certificate3":
        cert = Certificate
        if product == "econom":
            cert += "1"
            TEXT = """дійсно брав(ла) участь у
            практично-орієнтованому тренінгу
            “Зимова школа з хронічного болю”
            4-6 лютого 2020 року, м. Яремче
            та отримав(ла) 25 балів до свого
            портфоліо безперервної професійної освіти"""
        if product == "standart":
            cert += "2"
            TEXT = """дійсно брав(ла) участь у
            тренінгу з оволодіння практичними навичками
            “Місце канабіноїдів в медицині болю”
            5 лютого 2020 року, м. Яремче
            та отримав(ла) 15 балів до свого
            портфоліо безперервної професійної освіти"""
        if product == "premium":
            cert += "3"
            TEXT = """дійсно брав(ла) участь у
            тренінгу з оволодіння практичними навичками
            “Біль в спині з точки зору ревматолога”
            6 лютого 2020 року, м. Яремче
            та отримав(ла) 15 балів до свого
            портфоліо безперервної професійної освіти"""

        styles = getSampleStyleSheet()
        ptext = "№ " + cert  # № CERTIFICATE
        style = styles["Normal"]
        style.alignment = 1
        style.fontName = "OpenSans"
        style.fontSize = 20
        style.textColor = blue
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 160 * mm, 50 * mm)
        p.drawOn(c, 24 * mm, 138 * mm)

        ptext = "підтверджує те, що"
        style.fontSize = 18
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 160 * mm, 50 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 24 * mm, 147 * mm)  # position of text / where to draw

        ptext = LastName
        style.fontName = "DejaVuSans"
        style.fontSize = 38
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 160 * mm, 50 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 24 * mm, 174 * mm)  # position of text / where to draw

        ptext = FirstName
        style.fontSize = 32
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 160 * mm, 15 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 24 * mm, 188 * mm)  # position of text / where to draw

        style.fontName = "OpenSans"
        style.fontSize = 14
        style.leading = 20
        p = Paragraph(TEXT, style=style)
        p.wrapOn(c, 160 * mm, 100 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 24 * mm, 172 * mm)  # size of 'textbox' for linebreaks etc.

        qr_code = QrCodeWidget("https://pain.in.ua/checkcert/?cert=" + cert)
        bounds = qr_code.getBounds()
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
        d = Drawing(65, 65, transform=[65. / width, 0, 0, 65. / height, 0, 0])
        d.add(qr_code)
        renderPDF.draw(d, c, 170 * mm, 260 * mm)

        c.save()

    if template == "certificate4":
        cert = Certificate
        if product == "econom":
            cert += "1"
            TEXT = """дійсно брав(ла) участь у
            практично-орієнтованому тренінгу
            “Зимова школа УАВБ з болю”
            6-8 лютого 2020 року, м. Яремче
            та отримав(ла) 25 балів до свого
            портфоліо безперервної професійної освіти"""
        if product == "standart":
            cert += "2"
            TEXT = """дійсно брав(ла) участь у
            тренінгу з оволодіння практичними навичками
            “Застосування препаратів канабісу в медицині болю”
            6 лютого 2020 року, м. Яремче
            та отримав(ла) 15 балів до свого
            портфоліо безперервної професійної освіти"""
        if product == "premium":
            cert += "3"
            TEXT = """дійсно брав(ла) участь у
            тренінгу з оволодіння практичними навичками
            “Дискогенні попереково-крижові радикулопатії”
            7 лютого 2020 року, м. Яремче
            та отримав(ла) 15 балів до свого
            портфоліо безперервної професійної освіти"""

        styles = getSampleStyleSheet()
        ptext = "№ " + cert  # № CERTIFICATE
        style = styles["Normal"]
        style.alignment = 1
        style.fontName = "OpenSans"
        style.fontSize = 20
        style.textColor = blue
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 160 * mm, 50 * mm)
        p.drawOn(c, 24 * mm, 138 * mm)

        ptext = "підтверджує те, що"
        style.fontSize = 18
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 160 * mm, 50 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 24 * mm, 147 * mm)  # position of text / where to draw

        ptext = LastName
        style.fontName = "DejaVuSans"
        style.fontSize = 38
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 160 * mm, 50 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 24 * mm, 174 * mm)  # position of text / where to draw

        ptext = FirstName
        style.fontSize = 32
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 160 * mm, 15 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 24 * mm, 188 * mm)  # position of text / where to draw

        style.fontName = "OpenSans"
        style.fontSize = 14
        style.leading = 20
        p = Paragraph(TEXT, style=style)
        p.wrapOn(c, 160 * mm, 100 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 24 * mm, 172 * mm)  # size of 'textbox' for linebreaks etc.

        qr_code = QrCodeWidget("https://pain.in.ua/checkcert/?cert=" + cert)
        bounds = qr_code.getBounds()
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
        d = Drawing(65, 65, transform=[65. / width, 0, 0, 65. / height, 0, 0])
        d.add(qr_code)
        renderPDF.draw(d, c, 170 * mm, 260 * mm)

        c.save()


    if template == "badge":
        ptext = LastName
        styles = getSampleStyleSheet()
        style = styles["Normal"]
        style.textColor = blue
        style.alignment = 1
        style.fontName = "DejaVuSans"
        style.fontSize = 23
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 0 * mm, 138 * mm)  # position of text / where to draw

        ptext = FirstName
        style.fontSize = 15
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 0 * mm, 149 * mm)

        ptext = Certificate
        style.fontSize = 7
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 25 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 76 * mm, 155 * mm)

        qr_code = QrCodeWidget(Certificate)
        bounds = qr_code.getBounds()
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
        d = Drawing(42, 42, transform=[42. / width, 0, 0, 42. / height, 0, 0])
        d.add(qr_code)
        renderPDF.draw(d, c, 81 * mm, 142 * mm)

        c.save()

    if template == "badge1":
        ptext = LastName
        styles = getSampleStyleSheet()
        style = styles["Normal"]
        style.textColor = blue
        style.alignment = 1
        style.fontName = "DejaVuSans"
        style.fontSize = 24
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.стики
        p.drawOn(c, 0 * mm, 131 * mm)  # position of text / where to draw

        ptext = FirstName
        style.fontSize = 16
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 0 * mm, 135 * mm)

        ptext = Certificate
        style.fontSize = 10
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 24 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 38 * mm, 116 * mm)

        qr_code = QrCodeWidget(Certificate)
        bounds = qr_code.getBounds()
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
        d = Drawing(78, 78, transform=[78. / width, 0, 0, 78. / height, 0, 0])
        d.add(qr_code)
        renderPDF.draw(d, c, 36 * mm, 90 * mm)

        c.save()

    if template == "badge2":
        ptext = LastName
        styles = getSampleStyleSheet()
        style = styles["Normal"]
        style.textColor = blue
        style.alignment = 1
        style.fontName = "DejaVuSans"
        style.fontSize = 24
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.стики
        p.drawOn(c, 0 * mm, 131 * mm)  # position of text / where to draw

        ptext = FirstName
        style.fontSize = 16
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 0 * mm, 135 * mm)

        ptext = Certificate
        style.fontSize = 10
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 24 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 38 * mm, 116 * mm)

        qr_code = QrCodeWidget(Certificate)
        bounds = qr_code.getBounds()
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
        d = Drawing(78, 78, transform=[78. / width, 0, 0, 78. / height, 0, 0])
        d.add(qr_code)
        renderPDF.draw(d, c, 36 * mm, 90 * mm)

        c.save()

    if template == "badge3":
        ptext = LastName
        styles = getSampleStyleSheet()
        style = styles["Normal"]
        style.textColor = blue
        style.alignment = 1
        style.fontName = "DejaVuSans"
        style.fontSize = 24
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.стики
        p.drawOn(c, 0 * mm, 131 * mm)  # position of text / where to draw

        ptext = FirstName
        style.fontSize = 16
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 0 * mm, 135 * mm)

        ptext = Certificate
        style.fontSize = 10
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 24 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 38 * mm, 116 * mm)

        qr_code = QrCodeWidget(Certificate)
        bounds = qr_code.getBounds()
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
        d = Drawing(78, 78, transform=[78. / width, 0, 0, 78. / height, 0, 0])
        d.add(qr_code)
        renderPDF.draw(d, c, 36 * mm, 90 * mm)

        c.save()

    if template == "badge4":
        ptext = LastName
        styles = getSampleStyleSheet()
        style = styles["Normal"]
        style.textColor = blue
        style.alignment = 1
        style.fontName = "DejaVuSans"
        style.fontSize = 24
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.стики
        p.drawOn(c, 0 * mm, 131 * mm)  # position of text / where to draw

        if product == "premium":
            ptext = "PREMIUM"
            p = Paragraph(".", style=ParagraphStyle(name='Table', fontName='DejaVuSans', fontSize=14, aligment=TA_CENTER, leading=37,
                                      backColor=colors.green, textColor=colors.green))
            p.wrapOn(c, 97 * mm, 100 * mm)  # size of 'textbox' for linebreaks etc.
            p.drawOn(c, 0 * mm, 141 * mm)
            p = Paragraph(ptext,
                          style=ParagraphStyle(name='Table', fontName='DejaVuSans', fontSize=14, aligment=TA_CENTER,
                                               leading=37,
                                               backColor=colors.green, textColor=colors.white))
            p.wrapOn(c, 50 * mm, 100 * mm)  # size of 'textbox' for linebreaks etc.
            p.drawOn(c, 40 * mm, 141 * mm)

        if product == "standart":
            ptext = "STANDART"
            p = Paragraph(".", style=ParagraphStyle(name='Table', fontName='DejaVuSans', fontSize=14, aligment=TA_CENTER, leading=37,
                                      backColor=colors.blue, textColor=colors.blue))
            p.wrapOn(c, 97 * mm, 100 * mm)  # size of 'textbox' for linebreaks etc.
            p.drawOn(c, 0 * mm, 141 * mm)
            p = Paragraph(ptext,
                          style=ParagraphStyle(name='Table', fontName='DejaVuSans', fontSize=14, aligment=TA_CENTER,
                                               leading=37,
                                               backColor=colors.blue, textColor=colors.white))
            p.wrapOn(c, 50 * mm, 100 * mm)  # size of 'textbox' for linebreaks etc.
            p.drawOn(c, 38 * mm, 141 * mm)

        if product == "econom":
            ptext = "ECONOM"
            p = Paragraph(ptext,
                          style=ParagraphStyle(name='Table', fontName='DejaVuSans', fontSize=14, aligment=TA_CENTER,
                                               leading=37, textColor=colors.blue))
            p.wrapOn(c, 50 * mm, 100 * mm)  # size of 'textbox' for linebreaks etc.
            p.drawOn(c, 40 * mm, 141 * mm)

        ptext = FirstName
        style.fontSize = 16
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 0 * mm, 135 * mm)

        ptext = Certificate
        style.fontSize = 10
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 24 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 38 * mm, 116 * mm)

        qr_code = QrCodeWidget(Certificate)
        bounds = qr_code.getBounds()
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
        d = Drawing(78, 78, transform=[78. / width, 0, 0, 78. / height, 0, 0])
        d.add(qr_code)
        renderPDF.draw(d, c, 36 * mm, 90 * mm)

        c.save()

