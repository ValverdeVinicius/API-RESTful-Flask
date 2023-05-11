# -*- coding: utf-8 -*-
import requests
import json

request = requests.get("http://localhost:5000/tema")
temas = json.loads(request.content)

for t in temas:
    print(str(t['tema_id'])+"::"+t['tema_nome'])