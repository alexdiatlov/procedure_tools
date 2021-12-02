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
[12:09:55] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[12:09:55] Starting new HTTPS connection (1): lb-api-sandbox-2.prozorro.gov.ua:443
[12:09:55] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 991876
[12:09:55] Response status code: 200

[12:09:55] Client time delta with server: 0 seconds

[12:09:55] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[12:09:55] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 991876
[12:09:55] Response status code: 200

[12:09:55] Client time delta with server: 0 seconds

[12:09:55] Creating plan...

[12:09:55] Processing data file: plan_create.json

[12:09:55] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans
[12:09:55] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans HTTP/1.1" 201 4186
[12:09:55] Response status code: 201

[12:09:55] Plan created:
 - id 				3933d444701245199b57b417b6086c74
 - token 			5a1b88b8c55b42d1b0ec991d799d6b94
 - transfer 			3ea142c8b11b4614bd1296db90e79159

[12:09:55] Creating tender...

[12:09:55] Processing data file: tender_create.json

[12:09:55] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/3933d444701245199b57b417b6086c74/tenders
[12:09:55] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans/3933d444701245199b57b417b6086c74/tenders HTTP/1.1" 201 7149
[12:09:55] Response status code: 201

[12:09:55] Tender created:
 - id 				10a29f220ac24a3a9b55c99ad0e2567d
 - token 			48c379cd10474acb962389766ac3e865
 - transfer 			e03e880cde1044ea9f8ed0d9aeca6484
 - status 			draft
 - tenderID 			UA-2021-12-02-000226-b
 - procurementMethodType 	closeFrameworkAgreementUA

[12:09:55] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/10a29f220ac24a3a9b55c99ad0e2567d
[12:09:55] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/tenders/10a29f220ac24a3a9b55c99ad0e2567d HTTP/1.1" 200 7044
[12:09:55] Response status code: 200

[12:09:55] Create tender criteria...

[12:09:55] Processing data file: criteria_create.json

[12:09:55] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/10a29f220ac24a3a9b55c99ad0e2567d/criteria?acc_token=48c379cd10474acb962389766ac3e865
[12:09:56] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/10a29f220ac24a3a9b55c99ad0e2567d/criteria?acc_token=48c379cd10474acb962389766ac3e865 HTTP/1.1" 201 53725
[12:09:56] Response status code: 201

[12:09:56] Tender criteria created:
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

[12:09:56] Patching tender...

[12:09:56] Processing data file: tender_patch.json

[12:09:56] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/10a29f220ac24a3a9b55c99ad0e2567d?acc_token=48c379cd10474acb962389766ac3e865
[12:09:56] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/tenders/10a29f220ac24a3a9b55c99ad0e2567d?acc_token=48c379cd10474acb962389766ac3e865 HTTP/1.1" 200 60965
[12:09:56] Response status code: 200

[12:09:56] Tender status patched:
 - id 				10a29f220ac24a3a9b55c99ad0e2567d
 - status 			active.tendering

[12:09:56] Creating bids...

[12:09:56] Processing data file: bid_document.txt

[12:09:56] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:09:56] Starting new HTTPS connection (1): upload-docs-sandbox-2.prozorro.gov.ua:443
[12:09:56] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 568
[12:09:56] Response status code: 200

[12:09:56] Processing data file: bid_create_0.json

[12:09:56] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/10a29f220ac24a3a9b55c99ad0e2567d/bids
[12:09:56] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/10a29f220ac24a3a9b55c99ad0e2567d/bids HTTP/1.1" 201 1951
[12:09:56] Response status code: 201

[12:09:56] Bid created:
 - id 				41e026fde5654ae2a843611d7dfe2a0b
 - token 			3107cb6cf2d34e06be87c3d9f1bf6b08
 - status 			draft

[12:09:56] Processing data file: bid_document.txt

[12:09:56] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:09:56] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 586
[12:09:56] Response status code: 200

[12:09:56] Processing data file: bid_create_1.json

[12:09:56] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/10a29f220ac24a3a9b55c99ad0e2567d/bids
[12:09:57] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/10a29f220ac24a3a9b55c99ad0e2567d/bids HTTP/1.1" 201 2048
[12:09:57] Response status code: 201

[12:09:57] Bid created:
 - id 				178b1b0a1a3f4a5ca3675b77736d8c60
 - token 			f2a21ca8e65249dd8d65e3aeeca26ebd
 - status 			draft

[12:09:57] Processing data file: bid_document.txt

[12:09:57] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:09:57] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 574
[12:09:57] Response status code: 200

[12:09:57] Processing data file: bid_create_2.json

[12:09:57] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/10a29f220ac24a3a9b55c99ad0e2567d/bids
[12:09:57] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/10a29f220ac24a3a9b55c99ad0e2567d/bids HTTP/1.1" 201 2052
[12:09:57] Response status code: 201

[12:09:57] Bid created:
 - id 				479d452893734dddba2267748c48f917
 - token 			62695d541c504693be7dfa052747f7f5
 - status 			draft

[12:09:57] Processing data file: bid_document.txt

[12:09:57] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:09:57] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 580
[12:09:57] Response status code: 200

[12:09:57] Processing data file: bid_create_3.json

[12:09:57] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/10a29f220ac24a3a9b55c99ad0e2567d/bids
[12:09:57] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/10a29f220ac24a3a9b55c99ad0e2567d/bids HTTP/1.1" 201 2050
[12:09:57] Response status code: 201

[12:09:57] Bid created:
 - id 				f41ea9fde5924094b0673c786711b95f
 - token 			fa3d2da176174916a2ef798dc8cc7fcc
 - status 			draft

```

## Update readme

```
export API_HOST=https://lb-api-sandbox-2.prozorro.gov.ua
export API_TOKEN=broker_api_token
export DS_HOST=https://upload-docs-sandbox-2.prozorro.gov.ua
export DS_USERNAME=broker_ds_username
export DS_PASSWORD=broker_ds_password

./README.sh
```
or
```
API_HOST=https://lb-api-sandbox-2.prozorro.gov.ua API_TOKEN=broker_api_token DS_HOST=https://upload-docs-sandbox-2.prozorro.gov.ua DS_USERNAME=broker_ds_username DS_PASSWORD=broker_ds_password ./README.sh
```

## Run tests

```
export API_HOST=https://lb-api-sandbox-2.prozorro.gov.ua
export API_TOKEN=broker_api_token
export DS_HOST=https://upload-docs-sandbox-2.prozorro.gov.ua
export DS_USERNAME=broker_ds_username
export DS_PASSWORD=broker_ds_password

python setup.py test
```
or
```
API_HOST=https://lb-api-sandbox-2.prozorro.gov.ua API_TOKEN=broker_api_token DS_HOST=https://upload-docs-sandbox-2.prozorro.gov.ua DS_USERNAME=broker_ds_username DS_PASSWORD=broker_ds_password python setup.py test
```
