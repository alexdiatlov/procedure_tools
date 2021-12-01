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
                 host token ds_host ds_username ds_password

positional arguments:

  host                  CDB API Host

  token                 CDB API Token

  ds_host               DS API Host

  ds_username           DS API Username

  ds_password           DS API Password

options:

  -h, --help            show this help message and exit

  -a 460800, --acceleration 460800
                        acceleration multiplier

  -p /api/0/, --path /api/0/
                        api path

  -d aboveThresholdUA, --data aboveThresholdUA
                        data files path custom or one of:
                         - aboveThresholdUA.multilot
                         - competitiveDialogueUA
                         - reporting
                         - competitiveDialogueEU.multilot
                         - esco.multilot
                         - negotiation.quick.multilot
                         - belowThreshold
                         - aboveThresholdUA.multilot.lcc
                         - aboveThresholdUA
                         - aboveThresholdEU.multilot.features
                         - aboveThresholdUA.multilot.features
                         - aboveThresholdEU.plan
                         - aboveThresholdEU.lcc
                         - simple.defense.multilot
                         - closeFrameworkAgreementUA
                         - belowThreshold.multilot
                         - aboveThresholdEU.tender
                         - negotiation.quick
                         - esco
                         - aboveThresholdEU.multilot.lcc
                         - closeFrameworkAgreementUA.central
                         - aboveThresholdUA.defense
                         - belowThreshold.features
                         - negotiation.multilot
                         - simple.defense
                         - competitiveDialogueEU
                         - aboveThresholdEU.multilot
                         - belowThreshold.central
                         - aboveThresholdUA.features
                         - competitiveDialogueUA.multilot
                         - negotiation
                         - esco.features
                         - aboveThresholdUA.lcc
                         - aboveThresholdEU

  -m quick(mode:no-auction), --submission quick(mode:no-auction)
                        value for submissionMethodDetails one of:
                         - quick
                         - quick(mode:no-auction)
                         - quick(mode:fast-forward)

  -s tender_create.json, --stop tender_create.json
                        data file name to stop after

  -w edr-qualification, --wait edr-qualification
                        wait for event, one or many of (divided by comma):
                         - edr-qualification
                         - edr-pre-qualification
```

## Usage example

Create with default data
```
procedure https://lb-api-sandbox-2.prozorro.gov.ua broker_api_token https://upload-docs-sandbox-2.prozorro.gov.ua broker_ds_username broker_ds_password --acceleration=1000000 --path=/api/0/ --data=closeFrameworkAgreementUA
```

Create with default data and stop after specific data file
```
procedure https://lb-api-sandbox-2.prozorro.gov.ua broker_api_token https://upload-docs-sandbox-2.prozorro.gov.ua broker_ds_username broker_ds_password --acceleration=1000000 --path=/api/0/ --data=closeFrameworkAgreementUA
```

Create with custom data files (relative path)
```
procedure https://lb-api-sandbox-2.prozorro.gov.ua broker_api_token https://upload-docs-sandbox-2.prozorro.gov.ua broker_ds_username broker_ds_password --acceleration=1000000 --path=/api/0/ --data=customdata/closeFrameworkAgreementUA
```

Create with custom data files (absolute path)
```
procedure https://lb-api-sandbox-2.prozorro.gov.ua broker_api_token https://upload-docs-sandbox-2.prozorro.gov.ua broker_ds_username broker_ds_password --acceleration=1000000 --path=/api/0/ --data=/Users/JonhDoe/customdata/closeFrameworkAgreementUA
```

Create with custom data files (absolute path, Windows)
```
procedure https://lb-api-sandbox-2.prozorro.gov.ua broker_api_token https://upload-docs-sandbox-2.prozorro.gov.ua broker_ds_username broker_ds_password --acceleration=1000000 --path=/api/0/ --data=C:\Users\JonhDoe\customdata\closeFrameworkAgreementUA
```

## Output example
```
procedure https://lb-api-sandbox-2.prozorro.gov.ua broker_api_token https://upload-docs-sandbox-2.prozorro.gov.ua broker_ds_username broker_ds_password --acceleration=1000000 --path=/api/0/ --data=closeFrameworkAgreementUA --stop=bid_create_4.json
```
```
[01:13:09] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[01:13:09] Starting new HTTPS connection (1): lb-api-sandbox-2.prozorro.gov.ua:443
[01:13:09] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 991876
[01:13:10] Response status code: 200

[01:13:10] Client time delta with server: 0 seconds

[01:13:10] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[01:13:10] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 991876
[01:13:10] Response status code: 200

[01:13:10] Client time delta with server: 0 seconds

[01:13:10] Creating plan...

[01:13:10] Processing data file: plan_create.json

[01:13:10] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans
[01:13:10] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans HTTP/1.1" 201 4186
[01:13:10] Response status code: 201

[01:13:10] Plan created:
 - id 				e9b998bf17d14865976c79b952eeb649
 - token 			e4e1bd3cddaa4e61805ef0757f342cce
 - transfer 			ef024bd83c724a59bd2c1121d1bed4dc

[01:13:10] Creating tender...

[01:13:10] Processing data file: tender_create.json

[01:13:10] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/e9b998bf17d14865976c79b952eeb649/tenders
[01:13:10] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans/e9b998bf17d14865976c79b952eeb649/tenders HTTP/1.1" 201 7149
[01:13:10] Response status code: 201

[01:13:10] Tender created:
 - id 				023e715d61ee4ac29678eb3a8983b8d4
 - token 			216519abae9f4df980af85194053407f
 - transfer 			ce597a9ba2bd41f0bb3555299483900a
 - status 			draft
 - tenderID 			UA-2021-12-02-000062-b
 - procurementMethodType 	closeFrameworkAgreementUA

[01:13:10] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/023e715d61ee4ac29678eb3a8983b8d4
[01:13:10] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/tenders/023e715d61ee4ac29678eb3a8983b8d4 HTTP/1.1" 200 7044
[01:13:10] Response status code: 200

[01:13:10] Create tender criteria...

[01:13:10] Processing data file: criteria_create.json

[01:13:10] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/023e715d61ee4ac29678eb3a8983b8d4/criteria?acc_token=216519abae9f4df980af85194053407f
[01:13:11] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/023e715d61ee4ac29678eb3a8983b8d4/criteria?acc_token=216519abae9f4df980af85194053407f HTTP/1.1" 201 53725
[01:13:11] Response status code: 201

[01:13:11] Tender criteria created:
 - classification.id 				CRITERION.EXCLUSION.CONVICTIONS.PARTICIPATION_IN_CRIMINAL_ORGANISATION
 - classification.id 				CRITERION.EXCLUSION.CONVICTIONS.FRAUD
 - classification.id 				CRITERION.EXCLUSION.CONVICTIONS.CORRUPTION
 - classification.id 				CRITERION.EXCLUSION.CONVICTIONS.CHILD_LABOUR-HUMAN_TRAFFICKING
 - classification.id 				CRITERION.EXCLUSION.CONTRIBUTIONS.PAYMENT_OF_TAXES
 - classification.id 				CRITERION.EXCLUSION.BUSINESS.BANKRUPTCY
 - classification.id 				CRITERION.EXCLUSION.MISCONDUCT.MARKET_DISTORTION
 - classification.id 				CRITERION.EXCLUSION.CONFLICT_OF_INTEREST.MISINTERPRETATION
 - classification.id 				CRITERION.EXCLUSION.NATIONAL.OTHER
 - classification.id 				CRITERION.OTHER.BID.LANGUAGE

[01:13:11] Patching tender...

[01:13:11] Processing data file: tender_patch.json

[01:13:11] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/023e715d61ee4ac29678eb3a8983b8d4?acc_token=216519abae9f4df980af85194053407f
[01:13:11] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/tenders/023e715d61ee4ac29678eb3a8983b8d4?acc_token=216519abae9f4df980af85194053407f HTTP/1.1" 200 60965
[01:13:11] Response status code: 200

[01:13:11] Tender status patched:
 - id 				023e715d61ee4ac29678eb3a8983b8d4
 - status 			active.tendering

[01:13:11] Creating bids...

[01:13:11] Processing data file: bid_document.txt

[01:13:11] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[01:13:11] Starting new HTTPS connection (1): upload-docs-sandbox-2.prozorro.gov.ua:443
[01:13:11] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 572
[01:13:11] Response status code: 200

[01:13:11] Processing data file: bid_create_0.json

[01:13:11] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/023e715d61ee4ac29678eb3a8983b8d4/bids
[01:13:12] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/023e715d61ee4ac29678eb3a8983b8d4/bids HTTP/1.1" 201 1949
[01:13:12] Response status code: 201

[01:13:12] Bid created:
 - id 				eca73031338f4cd795bf8ea0b3d4e55b
 - token 			000469d8cfc248a2a282d881250e51e4
 - status 			draft

[01:13:12] Processing data file: bid_document.txt

[01:13:12] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[01:13:12] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 568
[01:13:12] Response status code: 200

[01:13:12] Processing data file: bid_create_1.json

[01:13:12] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/023e715d61ee4ac29678eb3a8983b8d4/bids
[01:13:12] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/023e715d61ee4ac29678eb3a8983b8d4/bids HTTP/1.1" 201 2052
[01:13:12] Response status code: 201

[01:13:12] Bid created:
 - id 				7a63c750f9c542c28383897fb78865ce
 - token 			e2c070be2eff4bf39caaa2f78c7ef989
 - status 			draft

[01:13:12] Processing data file: bid_document.txt

[01:13:12] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[01:13:12] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 578
[01:13:12] Response status code: 200

[01:13:12] Processing data file: bid_create_2.json

[01:13:12] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/023e715d61ee4ac29678eb3a8983b8d4/bids
[01:13:12] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/023e715d61ee4ac29678eb3a8983b8d4/bids HTTP/1.1" 201 2050
[01:13:12] Response status code: 201

[01:13:12] Bid created:
 - id 				cd0495865e454ed3b36a0480fee9289d
 - token 			6a56d304ea60454db61b070b28ecc668
 - status 			draft

[01:13:12] Processing data file: bid_document.txt

[01:13:12] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[01:13:13] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 586
[01:13:13] Response status code: 200

[01:13:13] Processing data file: bid_create_3.json

[01:13:13] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/023e715d61ee4ac29678eb3a8983b8d4/bids
[01:13:13] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/023e715d61ee4ac29678eb3a8983b8d4/bids HTTP/1.1" 201 2056
[01:13:13] Response status code: 201

[01:13:13] Bid created:
 - id 				3ba6759193e84af4a8797da639183710
 - token 			8d010b9528d64171bce5b1afc8b91a1e
 - status 			draft

```

## Update readme

Pass API token as parameter to README.sh
```
API_HOST=https://lb-api-sandbox-2.prozorro.gov.ua API_TOKEN=broker_api_token DS_HOST=https://upload-docs-sandbox-2.prozorro.gov.ua DS_USERNAME=broker_ds_username DS_PASSWORD=broker_ds_password ./README.sh
```

## Run tests

```

API_HOST=https://lb-api-sandbox-2.prozorro.gov.ua API_TOKEN=broker_api_token DS_HOST=https://upload-docs-sandbox-2.prozorro.gov.ua DS_USERNAME=broker_ds_username DS_PASSWORD=broker_ds_password python setup.py test
```
