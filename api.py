import json

output = [{'id': 123, 'hello': 'world'}]

url = "https://piiapi.genesysappliedresearch.com/api/v1/resolve"
headers = {"token": "fa8c712dd1104d5493655f78fad40868", "Content-Type": "application/json" }
payload =  {"text": input_data['q1'],  "expected_tags": [ "ORG", "PERSON"]}

d = json.dumps(payload)
r = requests.post(url,data=d,headers=headers)

st = ""
for i in range(len(r.json()['resolved_result'])):
    st += (" "+r.json()['resolved_result'][i]['text'])

#print(st)
url = "https://api.mypurecloud.com/api/v2/knowledge/knowledgebases/dcfcb801-9f25-4d1d-899e-bde3b341c9b8/search"
headers = { 'Content-Type': 'application/json', "Authorization": "Bearer Of3b6hIhhZEXuPKALclPzagbx3uXEYTJv7Tb4C94YM1rUGSam1wp2LDYzry7dsyNcNnPWKCKP8a6rZxdRuk5Aw" }
payload =  {
      "query": st,
      "pageSize": 1,
      "pageNumber": 1,
      "languageCode":"en-US",
      "documentType": "Faq",
      "searchOnDraftDocuments": "True"
    }

d = json.dumps(payload)
r = requests.post(url,data= d,headers=headers)

if 'results' in r.json() and len(r.json()['results']) > 0:
    output[0]['id1'] = r.json()['results'][0]['faq']['answer']
else:
    output[0]['id1'] = "Sorry, We don't have that in our database right now. We will register your question and we will get to you soon."
