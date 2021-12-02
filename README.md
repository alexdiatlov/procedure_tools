# procedure_tools

## Install

Clone and install with pip
```
cd procedure_tools

pip install -e .
```

## Usage
```
usage: procedure [-h] [-v] [-a 460800] [-p /api/0/] [-d aboveThresholdUA]
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

  -v, --version         show program's version number and exit

  -a 460800, --acceleration 460800
                        acceleration multiplier

  -p /api/0/, --path /api/0/
                        api path

  -d aboveThresholdUA, --data aboveThresholdUA
                        data files, custom path or one of:
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
                        value for submissionMethodDetails, one of:
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
[01:59:28] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[01:59:28] Starting new HTTPS connection (1): lb-api-sandbox-2.prozorro.gov.ua:443
[01:59:28] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 991876
[01:59:28] Response status code: 200

[01:59:28] Client time delta with server: 0 seconds

[01:59:28] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[01:59:28] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 991876
[01:59:28] Response status code: 200

[01:59:28] Client time delta with server: 0 seconds

[01:59:28] Creating plan...

[01:59:28] Processing data file: plan_create.json

[01:59:28] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans
[01:59:28] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans HTTP/1.1" 201 4186
[01:59:28] Response status code: 201

[01:59:28] Plan created:
 - id 				4169342cddac4598aa7b573a07d9831b
 - token 			80b2f9d730034b08ac0b565df27dfc0a
 - transfer 			d4743acbc6644a01ab06319b7b86d224

[01:59:28] Creating tender...

[01:59:28] Processing data file: tender_create.json

[01:59:28] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/4169342cddac4598aa7b573a07d9831b/tenders
[01:59:29] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans/4169342cddac4598aa7b573a07d9831b/tenders HTTP/1.1" 201 7149
[01:59:29] Response status code: 201

[01:59:29] Tender created:
 - id 				5844ed17149e4ec78208c6cdee373be5
 - token 			47dea070b09041e5995b496a598aec46
 - transfer 			8fcde451b3cb48c5bfd87876819191bf
 - status 			draft
 - tenderID 			UA-2021-12-02-000087-b
 - procurementMethodType 	closeFrameworkAgreementUA

[01:59:29] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/5844ed17149e4ec78208c6cdee373be5
[01:59:29] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/tenders/5844ed17149e4ec78208c6cdee373be5 HTTP/1.1" 200 7044
[01:59:29] Response status code: 200

[01:59:29] Create tender criteria...

[01:59:29] Processing data file: criteria_create.json

[01:59:29] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/5844ed17149e4ec78208c6cdee373be5/criteria?acc_token=47dea070b09041e5995b496a598aec46
[01:59:29] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/5844ed17149e4ec78208c6cdee373be5/criteria?acc_token=47dea070b09041e5995b496a598aec46 HTTP/1.1" 201 53725
[01:59:29] Response status code: 201

[01:59:29] Tender criteria created:
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

[01:59:29] Patching tender...

[01:59:29] Processing data file: tender_patch.json

[01:59:29] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/5844ed17149e4ec78208c6cdee373be5?acc_token=47dea070b09041e5995b496a598aec46
[01:59:30] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/tenders/5844ed17149e4ec78208c6cdee373be5?acc_token=47dea070b09041e5995b496a598aec46 HTTP/1.1" 200 60965
[01:59:30] Response status code: 200

[01:59:30] Tender status patched:
 - id 				5844ed17149e4ec78208c6cdee373be5
 - status 			active.tendering

[01:59:30] Creating bids...

[01:59:30] Processing data file: bid_document.txt

[01:59:30] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[01:59:30] Starting new HTTPS connection (1): upload-docs-sandbox-2.prozorro.gov.ua:443
[01:59:30] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 588
[01:59:30] Response status code: 200

[01:59:30] Processing data file: bid_create_0.json

[01:59:30] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/5844ed17149e4ec78208c6cdee373be5/bids
[01:59:30] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/5844ed17149e4ec78208c6cdee373be5/bids HTTP/1.1" 201 1949
[01:59:30] Response status code: 201

[01:59:30] Bid created:
 - id 				e6faff946d7a47cca03ac1243a4156a5
 - token 			9f422b55c3fc4c8ba4323dd3fe866c69
 - status 			draft

[01:59:30] Processing data file: bid_document.txt

[01:59:30] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[01:59:30] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 586
[01:59:30] Response status code: 200

[01:59:30] Processing data file: bid_create_1.json

[01:59:30] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/5844ed17149e4ec78208c6cdee373be5/bids
[01:59:31] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/5844ed17149e4ec78208c6cdee373be5/bids HTTP/1.1" 201 2052
[01:59:31] Response status code: 201

[01:59:31] Bid created:
 - id 				62901f94cdaa48bebf71876d28307b7f
 - token 			74e46433f0d746d6b79dd9ebf3e3501b
 - status 			draft

[01:59:31] Processing data file: bid_document.txt

[01:59:31] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[01:59:31] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 582
[01:59:31] Response status code: 200

[01:59:31] Processing data file: bid_create_2.json

[01:59:31] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/5844ed17149e4ec78208c6cdee373be5/bids
[01:59:31] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/5844ed17149e4ec78208c6cdee373be5/bids HTTP/1.1" 201 2054
[01:59:31] Response status code: 201

[01:59:31] Bid created:
 - id 				5212ae6a1b7d4c70b2679e282e4a971c
 - token 			bbc958b1394145f4bea1ce4afa691d30
 - status 			draft

[01:59:31] Processing data file: bid_document.txt

[01:59:31] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[01:59:31] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 582
[01:59:31] Response status code: 200

[01:59:31] Processing data file: bid_create_3.json

[01:59:31] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/5844ed17149e4ec78208c6cdee373be5/bids
[01:59:31] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/5844ed17149e4ec78208c6cdee373be5/bids HTTP/1.1" 201 2048
[01:59:31] Response status code: 201

[01:59:31] Bid created:
 - id 				646d0dbaceff490d90126e99b7df9b10
 - token 			1efb2f112f5743d18651695ca7ce9b15
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
