from reportlab.pdfgen import canvas
import smtplib
from email.message import EmailMessage


# =========================
# Create Demo PDF
# =========================

pdf_file = "Invoice_Demo.pdf"



print("PDF created:", pdf_file)


# =========================
# Email Settings
# =========================

sender = "marketingj786@gmail.com"
receiver = "keithyvheaiv@gmail.com"

msg = EmailMessage()

msg["Subject"] = "Urgent: Invoice Attached - Security Demo"
msg["From"] = sender
msg["To"] = receiver


msg.set_content("""
Hello, 

This is Jane from Paypal Support Team.
                
Please review the attached invoice.

We notice a big amount of purchase from your account.

The file below is the copy of your recent invoice.
                
Download and open the attached PDF to view the details.

Paypal Security Training Team
""")


# =========================
# Attach PDF
# =========================

with open(pdf_file, "rb") as file:

    msg.add_attachment(
        file.read(),
        maintype="application",
        subtype="pdf",
        filename=pdf_file
    )


# =========================
# Send Email
# =========================

with smtplib.SMTP_SSL(
    "smtp.gmail.com",
    465
) as smtp:

    smtp.login(
        sender,
        "hspt izzj fpek agwv"
    )

    smtp.send_message(msg)


print("Demo email sent successfully!")