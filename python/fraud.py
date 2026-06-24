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
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>PayFlex — Phishing Simulation (Training Demo)</title>
<style>
  :root{
    --ink:#1b1f23;
    --paper:#f6f3ed;
    --card:#ffffff;
    --flex-blue:#1455a6;
    --flex-blue-deep:#0d3a73;
    --alert:#b3261e;
    --alert-bg:#fdecea;
    --flag:#c9501c;
    --line:#e3ded2;
    --muted:#6b6458;
  }
  *{box-sizing:border-box;}
  body{
    margin:0;
    background:var(--paper);
    font-family:'Trebuchet MS', 'Segoe UI', sans-serif;
    color:var(--ink);
    padding:32px 16px 80px;
  }

  /* ---- Training banner ---- */
  .sim-banner{
    max-width:640px;
    margin:0 auto 18px;
    background:var(--alert);
    color:#fff;
    padding:12px 18px;
    border-radius:8px;
    font-size:13px;
    font-weight:700;
    letter-spacing:.04em;
    text-transform:uppercase;
    display:flex;
    align-items:center;
    gap:10px;
  }
  .sim-banner svg{flex:none;}

  /* ---- Email shell ---- */
  .email-shell{
    max-width:640px;
    margin:0 auto;
    background:var(--card);
    border:1px solid var(--line);
    border-radius:10px;
    overflow:hidden;
    box-shadow:0 18px 40px -22px rgba(20,85,166,.35);
    position:relative;
  }

  .email-header{
    background:linear-gradient(135deg,var(--flex-blue),var(--flex-blue-deep));
    padding:22px 28px;
    display:flex;
    align-items:center;
    gap:10px;
  }
  .logo-mark{
    width:30px;height:30px;border-radius:7px;
    background:#fff;
    display:flex;align-items:center;justify-content:center;
    font-weight:800;color:var(--flex-blue-deep);font-size:16px;
    font-family:Georgia, serif;
  }
  .logo-word{color:#fff;font-weight:700;font-size:18px;letter-spacing:.01em;}
  .logo-word b{font-weight:800;}

  .meta-row{
    padding:14px 28px;
    border-bottom:1px solid var(--line);
    font-size:12px;
    color:var(--muted);
    display:flex;
    justify-content:space-between;
  }

  .email-body{padding:30px 28px 10px;}
  .greeting{margin:0 0 16px;font-size:15px;}

  .alert-box{
    background:var(--alert-bg);
    border:1px solid #f2c4c0;
    border-left:4px solid var(--alert);
    border-radius:6px;
    padding:14px 16px;
    margin:0 0 20px;
    font-size:14px;
    display:flex;
    gap:10px;
    align-items:flex-start;
  }
  .alert-box svg{flex:none;margin-top:2px;}

  p{font-size:14.5px;line-height:1.65;color:#2c2f33;}

  .invoice-card{
    border:1px solid var(--line);
    border-radius:8px;
    padding:18px 20px;
    margin:18px 0 26px;
    background:#fbfaf7;
  }
  .invoice-row{
    display:flex;
    justify-content:space-between;
    font-size:13.5px;
    padding:6px 0;
    border-bottom:1px dashed var(--line);
  }
  .invoice-row:last-child{border-bottom:none;font-weight:700;color:var(--flex-blue-deep);}

  .cta-wrap{text-align:center;margin:8px 0 28px;}
  .cta-btn{
    display:inline-block;
    background:var(--flex-blue);
    color:#fff !important;
    text-decoration:none;
    font-weight:700;
    font-size:14.5px;
    padding:13px 30px;
    border-radius:6px;
    box-shadow:0 10px 22px -10px rgba(20,85,166,.55);
  }
  .cta-sub{font-size:11.5px;color:var(--muted);margin-top:10px;}

  .signoff{font-size:14px;margin-top:8px;}
  .team-name{font-weight:700;color:var(--flex-blue-deep);}

  .email-footer{
    padding:18px 28px 24px;
    font-size:11px;
    color:var(--muted);
    border-top:1px solid var(--line);
    background:#fbfaf7;
  }

  /* ---- Red flag annotations ---- */
  .flag{
    position:relative;
    outline:2px dashed var(--flag);
    outline-offset:4px;
    border-radius:4px;
  }
  .flag-tag{
    position:absolute;
    right:-12px;
    top:-12px;
    transform:translateX(100%);
    background:var(--flag);
    color:#fff;
    font-size:10.5px;
    font-weight:700;
    padding:4px 8px;
    border-radius:5px;
    white-space:nowrap;
    box-shadow:0 4px 10px -3px rgba(0,0,0,.3);
  }
  .flag-tag::before{
    content:"";
    position:absolute;
    left:-5px;top:50%;
    transform:translateY(-50%);
    border:5px solid transparent;
    border-right-color:var(--flag);
  }

  @media (max-width:640px){
    .flag-tag{
      position:static;
      transform:none;
      display:inline-block;
      margin-top:8px;
    }
    .flag-tag::before{display:none;}
  }

  /* ---- Legend ---- */
  .legend{
    max-width:640px;
    margin:30px auto 0;
    background:#fff;
    border:1px solid var(--line);
    border-radius:10px;
    padding:20px 24px;
  }
  .legend h2{
    font-size:14px;
    margin:0 0 12px;
    color:var(--flag);
    text-transform:uppercase;
    letter-spacing:.04em;
  }
  .legend ul{margin:0;padding-left:18px;}
  .legend li{font-size:13px;line-height:1.6;color:#2c2f33;margin-bottom:6px;}
  .legend li b{color:var(--ink);}
</style>
</head>
<body>

  <div class="sim-banner">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M12 2 1 21h22L12 2z" stroke="#fff" stroke-width="2" stroke-linejoin="round"/><path d="M12 9v5" stroke="#fff" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="17" r="1" fill="#fff"/></svg>
    Training simulation — PayFlex is a fictional brand, not a real company
  </div>

  <div class="email-shell">

    <div class="email-header">
      <div class="logo-mark">P</div>
      <div class="logo-word">Pay<b>Flex</b></div>
    </div>

    <div class="meta-row">
      <span>From: PayFlex Support &lt;support@payflex-secure-alerts.com&gt;</span>
      <span>Today, 9:14 AM</span>
    </div>

    <div class="email-body">

      <p class="greeting flag">
        Hello,
        <span class="flag-tag">No name used — real senders address you by name</span>
      </p>

      <div class="alert-box flag">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="var(--alert)" stroke-width="2"/><path d="M12 7v6" stroke="var(--alert)" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="16.5" r="1" fill="var(--alert)"/></svg>
        <span>We noticed a large purchase made from your account.</span>
        <span class="flag-tag">Vague urgency — no amount, date, or order ID</span>
      </div>

      <p>This is Jane from the PayFlex Support Team. Please review the attached invoice below.</p>

      <div class="invoice-card flag">
        <div class="invoice-row"><span>Invoice</span><span>#PF-7729</span></div>
        <div class="invoice-row"><span>Date</span><span>—</span></div>
        <div class="invoice-row"><span>Amount</span><span>$0.00</span></div>
        <span class="flag-tag">Empty fields the real company would already know</span>
      </div>

      <p>Download and open the attached PDF to view the full details of this transaction.</p>

      <div class="cta-wrap flag">
        <a href="#" class="cta-btn">Download Invoice (PDF)</a>
        <div class="cta-sub">attachment: Invoice_PF-7729.pdf.exe</div>
        <span class="flag-tag">Disguised file extension — a classic malware delivery trick</span>
      </div>

      <p class="signoff flag">
        <span class="team-name">PayFlex Security Training Team</span>
        <span class="flag-tag">Mismatched signer — "support" rep signs as "security"</span>
      </p>

    </div>

    <div class="email-footer">
      This message was sent as part of a classroom cybersecurity awareness exercise.
      PayFlex is not a real company. Do not reply to or interact with this address.
    </div>

  </div>

  <div class="legend">
    <h2>Why this email is a simulated phishing attempt</h2>
    <ul>
      <li><b>Generic greeting</b> — legitimate companies use your registered name, not "Hello."</li>
      <li><b>Manufactured urgency</b> — a "large purchase" with no specifics pressures quick, unthinking action.</li>
      <li><b>Spoofed-looking sender domain</b> — "payflex-secure-alerts.com" mimics legitimacy but isn't the real domain.</li>
      <li><b>Incomplete invoice data</b> — a real invoice would already show the amount and date.</li>
      <li><b>Disguised attachment</b> — double extensions like <code>.pdf.exe</code> hide an executable as a document.</li>
      <li><b>Inconsistent signer identity</b> — "Support" and "Security Training Team" don't match, a sign of a hastily assembled template.</li>
    </ul>
  </div>

</body>
</html>
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