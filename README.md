# procedure_tools

## Usage
```
usage: procedure [-h] [-a 460800] [-p /api/0/] [-d aboveThresholdUA]
                 [-s tender_create.json]
                 host token

positional arguments:
  host                  api host
  token                 api token

optional arguments:
  -h, --help            show this help message and exit
  -a 460800, --acceleration 460800
                        acceleration multiplier
  -p /api/0/, --path /api/0/
                        api path
  -d aboveThresholdUA, --data aboveThresholdUA
                        data files path custom or one of
                        ['competitiveDialogueUA', 'reporting',
                        'belowThreshold', 'aboveThresholdUA',
                        'closeFrameworkAgreementUA', 'negotiation.quick',
                        'esco', 'aboveThresholdUA.defense',
                        'competitiveDialogueEU', 'negotiation',
                        'aboveThresholdEU']
  -s tender_create.json, --stop tender_create.json
                        data file name to stop after
```

## Usage example

Create with default data
```
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/2.4/ --data=closeFrameworkAgreementUA
```

Create with default data and stop after specific data file
```
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/2.4/ --data=closeFrameworkAgreementUA
```

Create with custom data files (relative path)
```
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/2.4/ --data=customdata/closeFrameworkAgreementUA
```

Create with custom data files (absolute path)
```
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/2.4/ --data=/Users/JonhDoe/customdata/closeFrameworkAgreementUA
```

Create with custom data files (absolute path, Windows)
```
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/2.4/ --data=C:\Users\JonhDoe\customdata\closeFrameworkAgreementUA
```

## Output example
```
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/2.4/ --data=closeFrameworkAgreementUA --stop=bid_create_4.json
```
```
Creating tender...

Processing data file: tender_create.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/2.4/tenders

Tender created:
 - id 				3269fa06cf924a55b41050ad821dfbec
 - token 			06ef94ec051e48c9bc422ad8f0e9bdcc
 - status 			active.tendering
 - tenderID 			UA-2019-03-12-000023-a
 - procurementMethodType 	closeFrameworkAgreementUA

[GET] https://lb-api-sandbox.prozorro.gov.ua/api/2.4/tenders/3269fa06cf924a55b41050ad821dfbec

Creating bids...

Processing data file: bid_create_0.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/2.4/tenders/3269fa06cf924a55b41050ad821dfbec/bids

Bid created:
 - id 				9fb3b46ed01b4f43ae0680b64caa575b
 - token 			b618a62652ca4e8d9c3c859fbad50acc
 - status 			pending

Processing data file: bid_create_1.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/2.4/tenders/3269fa06cf924a55b41050ad821dfbec/bids

Bid created:
 - id 				2b35c2b5988a43fa94304bfa52d8e0c4
 - token 			ca1d9861f253497c8db2df1202cec9ce
 - status 			pending

Processing data file: bid_create_2.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/2.4/tenders/3269fa06cf924a55b41050ad821dfbec/bids

Bid created:
 - id 				c3c90c6fb5834d4a9a15279adff1377c
 - token 			b402aa97df2346ef869d8cf6c5a61cbc
 - status 			pending

Processing data file: bid_create_3.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/2.4/tenders/3269fa06cf924a55b41050ad821dfbec/bids

Bid created:
 - id 				393ce5a7e709449ba1b6cef0c051ee10
 - token 			52a36c9a532944f3b872affbee128332
 - status 			pending

```
