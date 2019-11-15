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
                        'aboveThresholdUA.defense', 'competitiveDialogueEU',
                        'aboveThresholdEU.multilot', 'negotiation',
                        'aboveThresholdEU']
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
 - id 				7a899d8e1bb34b899a2f8fa0f5e3d76f
 - token 			e07415a256874cdb83e5777eac35db6d
 - transfer 			d1d72d21b8184e75b4907e1835fc0ad3

Creating tender...

Processing data file: tender_create.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/0/plans/7a899d8e1bb34b899a2f8fa0f5e3d76f/tenders

Tender created:
 - id 				2987d162c52c4f0e846725326031f735
 - token 			e050e32d70294c218301ab1b1124f90d
 - transfer 			2c4e551d11144e72a8da0425873411da
 - status 			active.tendering
 - tenderID 			UA-2019-11-15-000036-c
 - procurementMethodType 	closeFrameworkAgreementUA

[GET] https://lb-api-sandbox.prozorro.gov.ua/api/0/tenders/2987d162c52c4f0e846725326031f735

Creating bids...

Processing data file: bid_create_0.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/0/tenders/2987d162c52c4f0e846725326031f735/bids

Bid created:
 - id 				e0348642e0fb4f069d491e603c94ceac
 - token 			c7f64d7f92004d39ae3e83fa7c91ffc8
 - status 			pending

Processing data file: bid_create_1.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/0/tenders/2987d162c52c4f0e846725326031f735/bids

Bid created:
 - id 				9b455e37e9cb4b2d83cb2bc588843b36
 - token 			a76941ab75924e5db8d9a803c1c314fd
 - status 			pending

Processing data file: bid_create_2.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/0/tenders/2987d162c52c4f0e846725326031f735/bids

Bid created:
 - id 				e06e76626e5a4e16b6954249564824ee
 - token 			6ceb4967ce0d4486a06013be6597eda2
 - status 			pending

Processing data file: bid_create_3.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/0/tenders/2987d162c52c4f0e846725326031f735/bids

Bid created:
 - id 				be04ed5b1c1e4fe1934839054bc07e74
 - token 			0316c655f0fd46ce9640eb0d1d730d7d
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
