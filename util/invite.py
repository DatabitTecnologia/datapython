from datetime import datetime, timedelta

import pandas as pd
from icalendar import Calendar, Event, vCalAddress

import log
import json
import base64
import os


class Invite:
    def createInvite(self, params):
        try:
            df_params = pd.DataFrame.from_dict(params, orient="index")

            try:
                semail = str(df_params.loc["email", 0])
            except Exception:
                semail = ""

            try:
                ssummary = str(df_params.loc["summary", 0])
            except Exception:
                ssummary = ""

            try:
                sdescription = str(df_params.loc["description", 0])
            except Exception:
                sdescription = ""

            try:
                slocation = str(df_params.loc["location", 0])
            except Exception:
                slocation = ""

            try:
                sdata = str(df_params.loc["data", 0])
            except Exception:
                sdata = ""

            try:
                shora = str(df_params.loc["hora", 0])
            except Exception:
                shora = ""

            sdatafull = sdata + " " + shora
            dtstart = datetime.strptime(sdatafull, '%m/%d/%Y %H:%M')
            dtend = dtstart + timedelta(minutes=30)

            listemail = semail.split(',')
            icount = 0
            retornofim = ""

            event = Event()
            event.add('summary', ssummary)
            event.add('description', sdescription)
            event.add('location', slocation)
            event.add('dtstart', dtstart)
            event.add('dtend', dtend)
            # Adicionando os participantes
            for participante in semail.split(','):
                attendee = vCalAddress(f'MAILTO:{participante}')
                attendee.params['cn'] = participante.split('@')[0]  # Nome comum do participante
                attendee.params['ROLE'] = 'REQ-PARTICIPANT'  # Papel do participante
                event.add('attendee', attendee)

            cal = Calendar()
            cal.add_component(event)

            ical_content = cal.to_ical()

            with open('c:\\temp\\calendario.ics'.format(icount), 'wb') as f:
                 f.write(ical_content)

            # Gerando Base64
            file_text = open('c:/temp/calendario.ics', 'rb')
            file_read = file_text.read()
            file_encode = str(base64.encodebytes(file_read))
            file_encode = file_encode.replace("b'", "")
            file_encode = file_encode.replace("\\n", "")
            file_encode = file_encode.replace("'", "")

            itamanho = os.path.getsize('c:/temp/calendario.ics')

            retorno = {"arquivo": 'calendario.ics'.format(icount), "base64": file_encode, "email": semail, "tamanho": itamanho}

            return json.dumps(retorno, indent=2)

        except Exception as e:
            return log.geralog(-1, 'Erro', "Problemas na geracao do arquivo: {}".format(e))
