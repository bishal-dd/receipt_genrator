from .generate_receipt import generate_pdf
from django.shortcuts import HttpResponse


def pdf_generation(data):

    pdf = generate_pdf('receipt_template.html', data)

    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Receipt.pdf"
        content = f"inline; filename={filename}"
        response['Content-Disposition'] = content

        return response

    return HttpResponse("Page Not Found")
