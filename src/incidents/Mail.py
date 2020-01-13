import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename
from src.config.Configurator import Configurator as config
from src.log.Logger import logger


def sendMail(content, files=None):
    if str(config.get("mail", "smpt_use")) != "true":
        return

    s = smtplib.SMTP(host=config.get("mail", "smpt_host"), port=config.get("mail", "smtp_port"))
    s.starttls()
    logger.debug("Log in to " + config.get("mail", "smpt_host") + " for sending e-mail")
    try:
        s.login(config.get("mail", "smtp_user"), config.get("mail", "smtp_pass"))
    except smtplib.SMTPAuthenticationError:
        logger.error("Error in Login to SMTP Server")
        return

    msg = MIMEMultipart()  # create a message
    msg['From'] = config.get("mail", "mail_from")
    msg['To'] = config.get("mail", "mail_receiver")
    msg['Subject'] = config.get("mail", "mail_subject")

    # add in the message body
    msg.attach(MIMEText(content, 'plain'))
    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        logger.debug("Adding file to e-mail " + basename(f))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg
