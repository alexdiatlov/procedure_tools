# procedure_tools

## Install

Clone and install with pip
```
cd procedure_tools

pip install -e .
```

## Usage
```
usage: procedure [-h] [-a 460800] [-p /api/0/] [-d aboveThresholdUA]
                 [-m quickmode:no-auction] [-s tender_create.json]
                 [-w edr-qualification]
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
                        'esco.multilot', 'belowThreshold', 'aboveThresholdUA',
                        'aboveThresholdEU.plan', 'closeFrameworkAgreementUA',
                        'belowThreshold.multilot', 'aboveThresholdEU.tender',
                        'negotiation.quick', 'esco',
                        'closeFrameworkAgreementUA.central',
                        'aboveThresholdUA.defense', 'competitiveDialogueEU',
                        'aboveThresholdEU.multilot', 'belowThreshold.central',
                        'negotiation', 'aboveThresholdEU']
  -m quick(mode:no-auction), --submission quick(mode:no-auction)
                        value for submissionMethodDetails one of ['quick',
                        'quick(mode:no-auction)', 'quick(mode:fast-forward)']
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
Creating plan...

Processing data file: plan_create.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/0/plans

Plan created:
 - id 				7a1e5958f2eb42f0a327a67910db21bc
 - token 			f290eeb086e34fd3bbaea4c849e25102
 - transfer 			96975c715d754f86bf2f12a937d6fbc7

Creating tender...

Processing data file: tender_create.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/0/plans/7a1e5958f2eb42f0a327a67910db21bc/tenders

Tender created:
 - id 				4dc6fd5b6fa043f4b2e69a993cff5884
 - token 			478af6654a2c49ca81d75b19a890ccc3
 - transfer 			6845ebae48e449368189bf1ad4fcc300
 - status 			active.tendering
 - tenderID 			UA-2020-03-03-000035-b
 - procurementMethodType 	closeFrameworkAgreementUA

[GET] https://lb-api-sandbox.prozorro.gov.ua/api/0/tenders/4dc6fd5b6fa043f4b2e69a993cff5884

Creating bids...

Processing data file: bid_create_0.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/0/tenders/4dc6fd5b6fa043f4b2e69a993cff5884/bids

Bid created:
 - id 				76a407a32df642c6a6cfb389af99b094
 - token 			c38eb3d1d4b54065ad87efd5082dc2af
 - status 			pending

Processing data file: bid_create_1.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/0/tenders/4dc6fd5b6fa043f4b2e69a993cff5884/bids

Bid created:
 - id 				484626e97cf147bda58ee7fc13ea6ec4
 - token 			1ab697e77d0a466cba36f2e062634367
 - status 			pending

Processing data file: bid_create_2.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/0/tenders/4dc6fd5b6fa043f4b2e69a993cff5884/bids

Bid created:
 - id 				72ceaeb6d8a14540850809c81bc3bd15
 - token 			45ad216b5df34e869377e592d1f9238b
 - status 			pending

Processing data file: bid_create_3.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/0/tenders/4dc6fd5b6fa043f4b2e69a993cff5884/bids

Bid created:
 - id 				9bac3481a06c4b61920b7b618e85e1ed
 - token 			074ce1e8d68e46d7b080489321b0180e
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
