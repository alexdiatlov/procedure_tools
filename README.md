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
                         - aboveThresholdEU
                         - aboveThresholdEU.lcc
                         - aboveThresholdEU.multilot
                         - aboveThresholdEU.multilot.features
                         - aboveThresholdEU.multilot.lcc
                         - aboveThresholdEU.plan
                         - aboveThresholdEU.tender
                         - aboveThresholdUA
                         - aboveThresholdUA.defense
                         - aboveThresholdUA.features
                         - aboveThresholdUA.lcc
                         - aboveThresholdUA.multilot
                         - aboveThresholdUA.multilot.features
                         - aboveThresholdUA.multilot.lcc
                         - belowThreshold
                         - belowThreshold.central
                         - belowThreshold.features
                         - belowThreshold.multilot
                         - closeFrameworkAgreementUA
                         - closeFrameworkAgreementUA.central
                         - competitiveDialogueEU
                         - competitiveDialogueEU.multilot
                         - competitiveDialogueUA
                         - competitiveDialogueUA.multilot
                         - esco
                         - esco.features
                         - esco.multilot
                         - negotiation
                         - negotiation.multilot
                         - negotiation.quick
                         - negotiation.quick.multilot
                         - reporting
                         - simple.defense
                         - simple.defense.multilot

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
[02:18:39] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[02:18:39] Starting new HTTPS connection (1): lb-api-sandbox-2.prozorro.gov.ua:443
[02:18:39] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 991876
[02:18:39] Response status code: 200

[02:18:39] Client time delta with server: 0 seconds

[02:18:39] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[02:18:39] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 991876
[02:18:40] Response status code: 200

[02:18:40] Client time delta with server: 0 seconds

[02:18:40] Creating plan...

[02:18:40] Processing data file: plan_create.json

[02:18:40] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans
[02:18:40] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans HTTP/1.1" 201 4186
[02:18:40] Response status code: 201

[02:18:40] Plan created:
 - id 				193b5e27db214f289d3dfcee6f361de0
 - token 			52ee4ced7c9247d5b607c99a9d4ac8c0
 - transfer 			a3633b4b3ddf4329b1321c48b2e74c22

[02:18:40] Creating tender...

[02:18:40] Processing data file: tender_create.json

[02:18:40] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/193b5e27db214f289d3dfcee6f361de0/tenders
[02:18:40] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans/193b5e27db214f289d3dfcee6f361de0/tenders HTTP/1.1" 201 7149
[02:18:40] Response status code: 201

[02:18:40] Tender created:
 - id 				f30829d5c5ed4149a7bffa0e25daa404
 - token 			f22841ace407475a8f2b05f922d074ba
 - transfer 			c0a0ba3c918a4249b95e9ded437a1154
 - status 			draft
 - tenderID 			UA-2021-12-02-000106-a
 - procurementMethodType 	closeFrameworkAgreementUA

[02:18:40] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/f30829d5c5ed4149a7bffa0e25daa404
[02:18:40] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/tenders/f30829d5c5ed4149a7bffa0e25daa404 HTTP/1.1" 200 7044
[02:18:40] Response status code: 200

[02:18:40] Create tender criteria...

[02:18:40] Processing data file: criteria_create.json

[02:18:40] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/f30829d5c5ed4149a7bffa0e25daa404/criteria?acc_token=f22841ace407475a8f2b05f922d074ba
[02:18:41] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/f30829d5c5ed4149a7bffa0e25daa404/criteria?acc_token=f22841ace407475a8f2b05f922d074ba HTTP/1.1" 201 53725
[02:18:41] Response status code: 201

[02:18:41] Tender criteria created:
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

[02:18:41] Patching tender...

[02:18:41] Processing data file: tender_patch.json

[02:18:41] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/f30829d5c5ed4149a7bffa0e25daa404?acc_token=f22841ace407475a8f2b05f922d074ba
[02:18:41] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/tenders/f30829d5c5ed4149a7bffa0e25daa404?acc_token=f22841ace407475a8f2b05f922d074ba HTTP/1.1" 200 60965
[02:18:41] Response status code: 200

[02:18:41] Tender status patched:
 - id 				f30829d5c5ed4149a7bffa0e25daa404
 - status 			active.tendering

[02:18:41] Creating bids...

[02:18:41] Processing data file: bid_document.txt

[02:18:41] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[02:18:41] Starting new HTTPS connection (1): upload-docs-sandbox-2.prozorro.gov.ua:443
[02:18:42] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 582
[02:18:42] Response status code: 200

[02:18:42] Processing data file: bid_create_0.json

[02:18:42] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/f30829d5c5ed4149a7bffa0e25daa404/bids
[02:18:42] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/f30829d5c5ed4149a7bffa0e25daa404/bids HTTP/1.1" 201 1951
[02:18:42] Response status code: 201

[02:18:42] Bid created:
 - id 				66d6cda0fcfb425bbaf8572859598a13
 - token 			da53c3de7e534b93b9c810eb9ff2f440
 - status 			draft

[02:18:42] Processing data file: bid_document.txt

[02:18:42] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[02:18:42] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 598
[02:18:42] Response status code: 200

[02:18:42] Processing data file: bid_create_1.json

[02:18:42] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/f30829d5c5ed4149a7bffa0e25daa404/bids
[02:18:42] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/f30829d5c5ed4149a7bffa0e25daa404/bids HTTP/1.1" 201 2050
[02:18:42] Response status code: 201

[02:18:42] Bid created:
 - id 				65bb64d93cb44024b9978ed4854c0c69
 - token 			d5db28d5242c4f29a3236a6340408ef3
 - status 			draft

[02:18:42] Processing data file: bid_document.txt

[02:18:42] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[02:18:43] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 576
[02:18:43] Response status code: 200

[02:18:43] Processing data file: bid_create_2.json

[02:18:43] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/f30829d5c5ed4149a7bffa0e25daa404/bids
[02:18:43] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/f30829d5c5ed4149a7bffa0e25daa404/bids HTTP/1.1" 201 2052
[02:18:43] Response status code: 201

[02:18:43] Bid created:
 - id 				432bca4f42e2470c95a6443fb31a8f75
 - token 			12a36dbe814d4394b7ed20444af215a4
 - status 			draft

[02:18:43] Processing data file: bid_document.txt

[02:18:43] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[02:18:43] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 572
[02:18:43] Response status code: 200

[02:18:43] Processing data file: bid_create_3.json

[02:18:43] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/f30829d5c5ed4149a7bffa0e25daa404/bids
[02:18:43] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/f30829d5c5ed4149a7bffa0e25daa404/bids HTTP/1.1" 201 2050
[02:18:43] Response status code: 201

[02:18:43] Bid created:
 - id 				ee0ea4be4eef4a3a997e9db465657863
 - token 			a60aefce523240e68551ab7a3caa8061
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
