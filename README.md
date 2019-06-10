# procedure_tools

## Install

Clone and install with pip
```
cd procedure_tools

pip install -r requirements.txt

pip install -e .
```

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
 - id 				8a38696b6edb463a8163a7e7505cefe9
 - token 			9566dc04793a47ab9e7e7914173d3f11
 - status 			active.tendering
 - tenderID 			UA-2019-05-30-000029-b
 - procurementMethodType 	closeFrameworkAgreementUA

[GET] https://lb-api-sandbox.prozorro.gov.ua/api/0/tenders/8a38696b6edb463a8163a7e7505cefe9

Creating bids...

Processing data file: bid_create_0.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/0/tenders/8a38696b6edb463a8163a7e7505cefe9/bids

Bid created:
 - id 				9c09823ffebf4b7e8c4953adaec0dfd3
 - token 			994d92bfc1494a3e9092c12b156c9426
 - status 			pending

Processing data file: bid_create_1.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/0/tenders/8a38696b6edb463a8163a7e7505cefe9/bids

Bid created:
 - id 				1567b035074242ffa60dc0d4cf8634f1
 - token 			54ee03e690604533844052f44af4f5ef
 - status 			pending

Processing data file: bid_create_2.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/0/tenders/8a38696b6edb463a8163a7e7505cefe9/bids

Bid created:
 - id 				9570a4a354ad4be6ba80a59c3523ff23
 - token 			5668ee9da9fb4509b9a839f806f3109d
 - status 			pending

Processing data file: bid_create_3.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/0/tenders/8a38696b6edb463a8163a7e7505cefe9/bids

Bid created:
 - id 				9dac2d8cb8b8428aaec8a236927c9f5e
 - token 			0e1cdca6518049cf9e23e8ddf60b9fc0
 - status 			pending

```

## Update readme

Pass API token as parameter to README.sh
```
./README.sh 59fcc88692e341a2a4a0c184db282e83
```

## Run tests

```
HOST=https://lb-api-sandbox.prozorro.gov.ua TOKEN=59fcc88692e341a2a4a0c184db282e83 python setup.py test
```
