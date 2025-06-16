import base64
import smtplib
import log
import dao
import pandas as pd
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import unicodedata


class sendEmail:

    def Email(self, params):
        try:

            df_params = pd.DataFrame.from_dict(params, orient="index")
            print(params)


            try:
                email = str(df_params.loc["email", 0])
            except Exception:
                email = ""

            try:
                smtp = str(df_params.loc["smtp", 0])
            except Exception:
                smtp = ""

            try:
                user = str(df_params.loc["user", 0])
            except Exception:
                user = ""

            try:
                password = str(df_params.loc["password", 0])
            except Exception:
                password = ""

            try:
                port = int(df_params.loc["port", 0])
            except Exception:
                port = 0

            try:
                tls = int(df_params.loc["tls", 0])
            except Exception:
                tls = 0

            try:
                dest = str(df_params.loc["dest", 0])
            except Exception:
                dest = ""

            try:
                subject = str(df_params.loc["subject", 0])
            except Exception:
                subject = ""

            try:
                body = str(df_params.loc["body", 0])
            except Exception:
                body = ""

            try:
                files = dao.jsontoObject(df_params.loc["files", 0])
            except Exception:
                files = []

            try:
                signature = str(df_params.loc["signature", 0])
            except Exception:
                signature = ""

            try:
                userdatabit = str(df_params.loc["userdatabit", 0])
            except Exception:
                userdatabit = ""

            try:
                fromname = str(df_params.loc["fromname", 0])
            except Exception:
                fromname = ""

            # Create a multipart message and set headers
            message = MIMEMultipart('alternative')
            message["From"] = formataddr((fromname, email))
            message["To"] = dest
            message["Subject"] = subject
            message['X-Priority'] = '2'
            message["Bcc"] = email
            # Add body to email

            html = """\
            <html>
              <head></head>
              <body>
                <p>
                   {}
                </p>
                <p></p>
                <p></p>
                <p>
                 <img alt="Website" style="border:none;" src="data:image/png;base64, {}" />
                </p>
              </body>
            </html>
            """.format(body.replace("\n","<br>"), signature)

            part = MIMEText(html, 'html')
            message.attach(part)
            for file in files:
                code64 = file[0]
                bytesarq = base64.b64decode(code64, validate=True)
                newfile = "c:/temp/" + userdatabit + file[1]
                filename = unicodedata.normalize('NFKD', file[1]).encode('ASCII', 'ignore').decode('ASCII')
                f = open(newfile, 'wb')
                f.write(bytesarq)
                f.close()
                part = MIMEBase("application", "octet-stream")
                with open(newfile, "rb") as attachment:
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition",
                        f'attachment; filename= "{filename}"',
                    )
                    message.attach(part)


            server = smtplib.SMTP(smtp, port)
            if tls == 1:
                server.starttls()
            server.login(user, password)
            server.sendmail(message['From'], [message['To']], message.as_string().encode('utf-8'),
                            rcpt_options=['NOTIFY=DELAY,FAILURE'])

            return log.geralog(1, 'OK',
                               "Envio de e-mail para o(s) destino(s) {}, realizado(s) com Sucesso !".format(message['To']))
        except Exception as e:

            return log.geralog(-1, 'Erro', "Erro ao enviar email: {}".format(e))
