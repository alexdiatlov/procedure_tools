# procedure_tools

## Usage
```
usage: procedure [-h] [-a 460800] [-p /api/0/] [-d aboveThresholdUA]
                 [-s tender_create.json] [-w edr-qualification]
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
  -w edr-qualification, --wait edr-qualification
                        wait for event ('edr-qualification', 'edr-pre-
                        qualification') divided by comma)
```

## Usage example

Create with default data
```
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/0/ --data=closeFrameworkAgreementUA
```

Create with default data and stop after specific data file
```
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/0/ --data=closeFrameworkAgreementUA
```

Create with custom data files (relative path)
```
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/0/ --data=customdata/closeFrameworkAgreementUA
```

Create with custom data files (absolute path)
```
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/0/ --data=/Users/JonhDoe/customdata/closeFrameworkAgreementUA
```

Create with custom data files (absolute path, Windows)
```
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/0/ --data=C:\Users\JonhDoe\customdata\closeFrameworkAgreementUA
```

## Output example
```
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/0/ --data=closeFrameworkAgreementUA --stop=bid_create_4.json
```
```
Creating tender...

Processing data file: tender_create.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/0/tenders

Tender created:
 - id 				9600e1a228c543e0bcab505f702351ae
 - token 			6197f2c9bd08441791b400ef7044b7aa
 - status 			active.tendering
 - tenderID 			UA-2019-03-13-000025-b
 - procurementMethodType 	closeFrameworkAgreementUA

[GET] https://lb-api-sandbox.prozorro.gov.ua/api/0/tenders/9600e1a228c543e0bcab505f702351ae

Creating bids...

Processing data file: bid_create_0.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/0/tenders/9600e1a228c543e0bcab505f702351ae/bids

Bid created:
 - id 				44ad3aefee2949478d9141a45e71057a
 - token 			15b51c36490a431d92a1643201f2e74a
 - status 			pending

Processing data file: bid_create_1.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/0/tenders/9600e1a228c543e0bcab505f702351ae/bids

Bid created:
 - id 				39b3dac17d964987ba4ee46554fd8236
 - token 			78eadc0f70c14d639a5cf2c5a08ecfbd
 - status 			pending

Processing data file: bid_create_2.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/0/tenders/9600e1a228c543e0bcab505f702351ae/bids

Bid created:
 - id 				b7d0f78469244a4f97de4b34e45f6e9d
 - token 			7f05f6128de04b0da47b2a1340a2302d
 - status 			pending

Processing data file: bid_create_3.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/0/tenders/9600e1a228c543e0bcab505f702351ae/bids

Bid created:
 - id 				1f04e17befc948e1b26f7ca1fd7b363a
 - token 			287ff75b35cb400a8c064409bee37466
 - status 			pending

```
