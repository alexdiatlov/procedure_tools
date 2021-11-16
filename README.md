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
                        data files path custom or one of
                        ['aboveThresholdUA.multilot', 'competitiveDialogueUA',
                        'reporting', 'esco.multilot', 'belowThreshold',
                        'aboveThresholdUA.multilot.lcc', 'aboveThresholdUA',
                        'aboveThresholdEU.multilot.features',
                        'aboveThresholdUA.multilot.features',
                        'aboveThresholdEU.plan', 'aboveThresholdEU.lcc',
                        'closeFrameworkAgreementUA',
                        'belowThreshold.multilot', 'aboveThresholdEU.tender',
                        'negotiation.quick', 'esco',
                        'aboveThresholdEU.multilot.lcc',
                        'closeFrameworkAgreementUA.central',
                        'aboveThresholdUA.defense', 'belowThreshold.features',
                        'simple.defense', 'competitiveDialogueEU',
                        'aboveThresholdEU.multilot', 'belowThreshold.central',
                        'aboveThresholdUA.features', 'negotiation',
                        'esco.features', 'aboveThresholdUA.lcc',
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
[13:14:15] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[13:14:15] Starting new HTTPS connection (1): lb-api-sandbox-2.prozorro.gov.ua:443
[13:14:15] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 1204862
[13:14:15] Response status code: 200

[13:14:15] Client time delta with server: 0 seconds

[13:14:15] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[13:14:15] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 1204862
[13:14:16] Response status code: 200

[13:14:16] Client time delta with server: -1 seconds

[13:14:16] Creating plan...

[13:14:16] Processing data file: plan_create.json

[13:14:16] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans
[13:14:16] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans HTTP/1.1" 201 4135
[13:14:16] Response status code: 201

[13:14:16] Plan created:
 - id 				aafa2d2ef06a4bfea5546a875db539f4
 - token 			8490d873a5844e62b8329738ed72ec63
 - transfer 			1e7ea892e5d647c498af661b97ed7e80

[13:14:16] Creating tender...

[13:14:16] Processing data file: tender_create.json

[13:14:16] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/aafa2d2ef06a4bfea5546a875db539f4/tenders
[13:14:16] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans/aafa2d2ef06a4bfea5546a875db539f4/tenders HTTP/1.1" 201 7149
[13:14:16] Response status code: 201

[13:14:16] Tender created:
 - id 				0c34a62d9f274a83b11b2cf569eacdce
 - token 			66c92ea15684493382ac1a224c438f6a
 - transfer 			9a2a74aa6d3444c1b1cfb639cbe355ff
 - status 			draft
 - tenderID 			UA-2021-11-16-000088-a
 - procurementMethodType 	closeFrameworkAgreementUA

[13:14:16] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/0c34a62d9f274a83b11b2cf569eacdce
[13:14:16] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/tenders/0c34a62d9f274a83b11b2cf569eacdce HTTP/1.1" 200 7044
[13:14:16] Response status code: 200

[13:14:16] Create tender criteria...

[13:14:16] Processing data file: criteria_create.json

[13:14:16] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/0c34a62d9f274a83b11b2cf569eacdce/criteria?acc_token=66c92ea15684493382ac1a224c438f6a
[13:14:16] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/0c34a62d9f274a83b11b2cf569eacdce/criteria?acc_token=66c92ea15684493382ac1a224c438f6a HTTP/1.1" 201 53725
[13:14:16] Response status code: 201

[13:14:16] Tender criteria created:
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

[13:14:16] Patching tender...

[13:14:16] Processing data file: tender_patch.json

[13:14:16] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/0c34a62d9f274a83b11b2cf569eacdce?acc_token=66c92ea15684493382ac1a224c438f6a
[13:14:17] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/tenders/0c34a62d9f274a83b11b2cf569eacdce?acc_token=66c92ea15684493382ac1a224c438f6a HTTP/1.1" 200 60965
[13:14:17] Response status code: 200

[13:14:17] Tender status patched:
 - id 				0c34a62d9f274a83b11b2cf569eacdce
 - status 			active.tendering

[13:14:17] Creating bids...

[13:14:17] Processing data file: bid_document.txt

[13:14:17] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[13:14:17] Starting new HTTPS connection (1): upload-docs-sandbox-2.prozorro.gov.ua:443
[13:14:19] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 582
[13:14:19] Response status code: 200

[13:14:19] Processing data file: bid_create_0.json

[13:14:19] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/0c34a62d9f274a83b11b2cf569eacdce/bids
[13:14:19] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/0c34a62d9f274a83b11b2cf569eacdce/bids HTTP/1.1" 201 1947
[13:14:19] Response status code: 201

[13:14:19] Bid created:
 - id 				f8f728cbac90467088653f3f2e531da6
 - token 			8a85707c203f4f4491721980bde20fe8
 - status 			draft

[13:14:19] Processing data file: bid_document.txt

[13:14:19] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[13:14:21] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 576
[13:14:21] Response status code: 200

[13:14:21] Processing data file: bid_create_1.json

[13:14:21] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/0c34a62d9f274a83b11b2cf569eacdce/bids
[13:14:21] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/0c34a62d9f274a83b11b2cf569eacdce/bids HTTP/1.1" 201 2050
[13:14:21] Response status code: 201

[13:14:21] Bid created:
 - id 				5e68e7b8abd74a7487270b53c25773a7
 - token 			ac1cfc77db514a879f743b395cc15c7d
 - status 			draft

[13:14:21] Processing data file: bid_document.txt

[13:14:21] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[13:14:21] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 580
[13:14:21] Response status code: 200

[13:14:21] Processing data file: bid_create_2.json

[13:14:21] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/0c34a62d9f274a83b11b2cf569eacdce/bids
[13:14:21] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/0c34a62d9f274a83b11b2cf569eacdce/bids HTTP/1.1" 201 2048
[13:14:21] Response status code: 201

[13:14:21] Bid created:
 - id 				56baecfca88b49b6bea1440dc8a379d1
 - token 			dfd457f8a4af425c84368999e1e4f942
 - status 			draft

[13:14:21] Processing data file: bid_document.txt

[13:14:21] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[13:14:21] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 586
[13:14:21] Response status code: 200

[13:14:21] Processing data file: bid_create_3.json

[13:14:21] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/0c34a62d9f274a83b11b2cf569eacdce/bids
[13:14:21] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/0c34a62d9f274a83b11b2cf569eacdce/bids HTTP/1.1" 201 2050
[13:14:21] Response status code: 201

[13:14:21] Bid created:
 - id 				9b4a7b9c306540fc9b2b66ffc6f715c5
 - token 			97b8054bab6d434b8b88bf9cace5864d
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
