from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Paragraph, Table
from reportlab.lib import colors
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
    c = canvas.Canvas('../Рабочий стол/{}.pdf'.format(Certificate + template), pagesize=A4, bottomup=False)  # alternatively use bottomup=False
    width, height = A4
    c.setFillColorRGB(0,0,255)

    if template == "certificate":
        TEXT = """дійсно брав(ла) участь у
        Всеукраїнському міждисциплінарному практично-
        орієнтованому тренінгу "PainControl - мистецтво
        контролювати біль" 15 листопада 2019 року у м. Львів
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
        style.fontSize = 23
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.стики
        p.drawOn(c, 0 * mm, 138 * mm)  # position of text / where to draw

        ptext = FirstName
        style.fontSize = 15
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 0 * mm, 143 * mm)

        ptext = "Практично-орієнтований тренінг"
        style.fontSize = 10
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 0 * mm, 93 * mm)
        
        ptext = '"Зимова школа з діагностики болю"'
        style.fontSize = 11
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 0 * mm, 99 * mm)

        ptext = '31.01-02.02.2020'
        style.fontSize = 13
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 20 * mm, 170 * mm)

        ptext = Certificate
        style.fontSize = 7
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 25 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 38 * mm, 123 * mm)
        p.drawOn(c, 38 * mm, 123 * mm)

        qr_code = QrCodeWidget(Certificate)
        bounds = qr_code.getBounds()
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
        d = Drawing(58, 58, transform=[58. / width, 0, 0, 58. / height, 0, 0])
        d.add(qr_code)
        renderPDF.draw(d, c, 40 * mm, 105 * mm)
        renderPDF.draw(d, c, 40 * mm, 105 * mm)

        c.save()

    if template == "badge2":
        ptext = LastName
        styles = getSampleStyleSheet()
        style = styles["Normal"]
        style.textColor = blue
        style.alignment = 1
        style.fontName = "DejaVuSans"
        style.fontSize = 23
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.стики
        p.drawOn(c, 0 * mm, 138 * mm)  # position of text / where to draw

        ptext = FirstName
        style.fontSize = 15
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 0 * mm, 143 * mm)

        ptext = "Практично-орієнтований тренінг"
        style.fontSize = 10
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 0 * mm, 93 * mm)

        ptext = '"Зимова школа з лікування болю"'
        style.fontSize = 11
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 0 * mm, 99 * mm)

        ptext = '02.02-04.02.2020'
        style.fontSize = 13
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 20 * mm, 170 * mm)

        ptext = Certificate
        style.fontSize = 7
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 25 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 38 * mm, 123 * mm)
        p.drawOn(c, 38 * mm, 123 * mm)

        qr_code = QrCodeWidget(Certificate)
        bounds = qr_code.getBounds()
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
        d = Drawing(58, 58, transform=[58. / width, 0, 0, 58. / height, 0, 0])
        d.add(qr_code)
        renderPDF.draw(d, c, 40 * mm, 105 * mm)
        renderPDF.draw(d, c, 40 * mm, 105 * mm)

        c.save()

    if template == "badge3":
        ptext = LastName
        styles = getSampleStyleSheet()
        style = styles["Normal"]
        style.textColor = blue
        style.alignment = 1
        style.fontName = "DejaVuSans"
        style.fontSize = 23
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.стики
        p.drawOn(c, 0 * mm, 138 * mm)  # position of text / where to draw

        ptext = FirstName
        style.fontSize = 15
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 0 * mm, 143 * mm)

        ptext = "Практично-орієнтований тренінг"
        style.fontSize = 10
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 0 * mm, 93 * mm)

        ptext = '"Зимова школа з хронічного болю"'
        style.fontSize = 11
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 0 * mm, 99 * mm)

        ptext = '04.02-06.02.2020'
        style.fontSize = 13
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 20 * mm, 170 * mm)

        ptext = Certificate
        style.fontSize = 7
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 25 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 38 * mm, 123 * mm)
        p.drawOn(c, 38 * mm, 123 * mm)

        qr_code = QrCodeWidget(Certificate)
        bounds = qr_code.getBounds()
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
        d = Drawing(58, 58, transform=[58. / width, 0, 0, 58. / height, 0, 0])
        d.add(qr_code)
        renderPDF.draw(d, c, 40 * mm, 105 * mm)
        renderPDF.draw(d, c, 40 * mm, 105 * mm)

        c.save()

    if template == "badge4":
        ptext = LastName
        styles = getSampleStyleSheet()
        style = styles["Normal"]
        style.textColor = blue
        style.alignment = 1
        style.fontName = "DejaVuSans"
        style.fontSize = 23
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.стики
        p.drawOn(c, 0 * mm, 138 * mm)  # position of text / where to draw

        if product == "premium":
            c.setFillColorRGB(0, 255, 0)

            ptext = "PREMIUM"
            style.fontSize = 15
            p = Paragraph(ptext, style=style)
            p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
            p.drawOn(c, 0 * mm, 133 * mm)

        ptext = FirstName
        style.fontSize = 15
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 0 * mm, 143 * mm)

        ptext = "Практично-орієнтований тренінг"
        style.fontSize = 10
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 0 * mm, 93 * mm)

        ptext = 'Зимова школа з болю "Winter Pain School"'
        style.fontSize = 11
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 0 * mm, 99 * mm)

        ptext = '06.02-08.02.2020'
        style.fontSize = 13
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 100 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 20 * mm, 170 * mm)

        ptext = Certificate
        style.fontSize = 7
        p = Paragraph(ptext, style=style)
        p.wrapOn(c, 24 * mm, 11 * mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 38 * mm, 124 * mm)

        qr_code = QrCodeWidget(Certificate)
        bounds = qr_code.getBounds()
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
        d = Drawing(58, 58, transform=[58. / width, 0, 0, 58. / height, 0, 0])
        d.add(qr_code)
        renderPDF.draw(d, c, 40 * mm, 105 * mm)
        renderPDF.draw(d, c, 40 * mm, 105 * mm)

        c.save()

