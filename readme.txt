Facebook Messenger ChatBot Link(Expired):

https://m.me/107058280888966?ref=Welcome%20Message

Tech Stack:
  Facebook Messenger
  ChatFuel
  Zapier
  Python

Sample inputs : 
“Can I play games in my Acer predator helios?”
“Can I upgrade ram in my acer chromebook?”

For this prototype, we have added FAQ for 10 laptops.
Please include product name in the query to get specific answers for the product. 

Products supported : 
Acer aspire 5
Acer chromebook
Acer predator helios
apple macbook air
Lenovo Ideapad L340
Lenovo Flex
Asus chromebook
HP 2019
HP 2020

Note:
  Used to search Laptop FAQ.


Organization Id: 32e0ad6f-7935-48df-a08b-a5157e30fff1
Client ID: 4e16bf7c-5352-4c77-ae6d-46bbd8b2f920
Client Secret: LolhCf7Jk4ZsspSCFW0WrZGpMEqdkN19cEiXtb-f9fs
token: fa8c712dd1104d5493655f78fad40868

Train Search:

curl -X POST -d '{"query": "exit formalities","pageSize": 1,"pageNumber": 1,"languageCode":"en-US","documentType": "Faq","searchOnDraftDocuments": "True"}' -H "Content-Type: application/json" -H "Authorization: Bearer vtCnhh1xP2GC6yC4kKpEmqQQ6KRK1-_Dn_DU8B564LLy6mPw0LJAEuthgSqU_KX-e9BxKFTZ1oFTj8EINFxWqw" "https://api.mypurecloud.com/api/v2/knowledge/knowledgebases/0b5e39f5-ed1d-4e07-a60d-990cbc93fa6d/search" 

other formats
curl -X POST  -d "@data.json" -H "Content-Type: application/json" -H "Authorization: Bearer vtCnhh1xP2GC6yC4kKpEmqQQ6KRK1-_Dn_DU8B564LLy6mPw0LJAEuthgSqU_KX-e9BxKFTZ1oFTj8EINFxWqw" "https://api.mypurecloud.com/api/v2/knowledge/knowledgebases/0b5e39f5-ed1d-4e07-a60d-990cbc93fa6d/search" 

curl -X POST -H "Authorization: Bearer vtCnhh1xP2GC6yC4kKpEmqQQ6KRK1-_Dn_DU8B564LLy6mPw0LJAEuthgSqU_KX-e9BxKFTZ1oFTj8EINFxWqw" "https://api.mypurecloud.com/api/v2/knowledge/knowledgebases/0b5e39f5-ed1d-4e07-a60d-990cbc93fa6d/search" 

NER Link:

curl -X POST "https://piiapi.genesysappliedresearch.com/api/v1/resolve" -H  "accept: application/json" -H  "token: fa8c712dd1104d5493655f78fad40868" -H  "Content-Type: application/json" -d "{  \"text\": \"my name is tony bates and i work for genesys\",  \"expected_tags\": [    \"ORG\",    \"PERSON\"  ]}"
