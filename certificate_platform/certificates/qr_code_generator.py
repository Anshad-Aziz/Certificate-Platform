import qrcode
from django.conf import settings
from django.core.files.base import ContentFile
from io import BytesIO
from certificates.models import Certificate
import os

def generate_qr_code(certificate):
    verification_url = f"{settings.SITE_URL}/verification/{certificate.certificate_id}/"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(verification_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    filename = f"qr_{certificate.certificate_id}.png"
    certificate.qr_code.save(filename, ContentFile(buffer.getvalue()), save=True)