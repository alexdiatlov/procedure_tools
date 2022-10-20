# procedure_tools

## Install

1. Clone
2. Navigate to cloned folder:
```
cd procedure_tools
```
3. Install with pip
* vanilla:
```
pip install -e .
```
* colorized output:
```
pip install -e .[color]
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
                         - aboveThreshold.multilot
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
procedure https://lb-api-sandbox-2.prozorro.gov.ua broker_api_token https://upload-docs-sandbox-2.prozorro.gov.ua broker_ds_username broker_ds_password --acceleration=1000000 --path=/api/0/ --data=closeFrameworkAgreementUA --stop=bid_create_3.json
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
[13:22:15] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[13:22:15] Starting new HTTPS connection (1): lb-api-sandbox-2.prozorro.gov.ua:443
[13:22:15] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 869934
[13:22:16] Response status code: 200

[13:22:16] Client time delta with server: -1 seconds

[13:22:16] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[13:22:16] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 869934
[13:22:16] Response status code: 200

[13:22:16] Client time delta with server: 0 seconds

[13:22:16] Creating plan...

[13:22:16] Processing data file: plan_create.json

[13:22:16] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans
[13:22:16] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans HTTP/1.1" 201 4186
[13:22:16] Response status code: 201

[13:22:16] Plan created:
 - id 				108a891037ff41b8a1b1cebc8ca8df36
 - token 			7909743800e24dd286238e6f1844dc7a
 - transfer 			d690634f131246559fe9df336900b216
 - status 			draft

[13:22:16] Patching plan...

[13:22:16] Processing data file: plan_patch.json

[13:22:16] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/108a891037ff41b8a1b1cebc8ca8df36?acc_token=7909743800e24dd286238e6f1844dc7a
[13:22:16] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/plans/108a891037ff41b8a1b1cebc8ca8df36?acc_token=7909743800e24dd286238e6f1844dc7a HTTP/1.1" 200 4085
[13:22:16] Response status code: 200

[13:22:16] Plan patched:
 - id 				108a891037ff41b8a1b1cebc8ca8df36
 - status 			scheduled

[13:22:16] Creating tender...

[13:22:16] Processing data file: tender_create.json

[13:22:16] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/108a891037ff41b8a1b1cebc8ca8df36/tenders
[13:22:17] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans/108a891037ff41b8a1b1cebc8ca8df36/tenders HTTP/1.1" 201 7201
[13:22:17] Response status code: 201

[13:22:17] Tender created:
 - id 				b92ebe34a1a04126a384dc616cdc7f97
 - token 			26062ca3e924409199e5f4b4988d180c
 - transfer 			74b93afe8279444e8a23c884ddf58ffd
 - status 			draft
 - tenderID 			UA-2022-10-20-000081-a
 - procurementMethodType 	closeFrameworkAgreementUA

[13:22:17] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/b92ebe34a1a04126a384dc616cdc7f97
[13:22:17] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/tenders/b92ebe34a1a04126a384dc616cdc7f97 HTTP/1.1" 200 7096
[13:22:17] Response status code: 200

[13:22:17] Processing data file: tender_document.txt

[13:22:17] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[13:22:17] Starting new HTTPS connection (1): upload-docs-sandbox-2.prozorro.gov.ua:443
[13:22:17] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 583
[13:22:17] Response status code: 200

[13:22:17] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/b92ebe34a1a04126a384dc616cdc7f97/documents?acc_token=26062ca3e924409199e5f4b4988d180c
[13:22:17] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/b92ebe34a1a04126a384dc616cdc7f97/documents?acc_token=26062ca3e924409199e5f4b4988d180c HTTP/1.1" 201 526
[13:22:17] Response status code: 201

[13:22:17] Create tender criteria...

[13:22:17] Processing data file: criteria_create.json

[13:22:17] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/b92ebe34a1a04126a384dc616cdc7f97/criteria?acc_token=26062ca3e924409199e5f4b4988d180c
[13:22:17] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/b92ebe34a1a04126a384dc616cdc7f97/criteria?acc_token=26062ca3e924409199e5f4b4988d180c HTTP/1.1" 201 53725
[13:22:17] Response status code: 201

[13:22:17] Tender criteria created:
 - classification.id 		CRITERION.EXCLUSION.CONVICTIONS.PARTICIPATION_IN_CRIMINAL_ORGANISATION
 - classification.id 		CRITERION.EXCLUSION.CONVICTIONS.FRAUD
 - classification.id 		CRITERION.EXCLUSION.CONVICTIONS.CORRUPTION
 - classification.id 		CRITERION.EXCLUSION.CONVICTIONS.CHILD_LABOUR-HUMAN_TRAFFICKING
 - classification.id 		CRITERION.EXCLUSION.CONTRIBUTIONS.PAYMENT_OF_TAXES
 - classification.id 		CRITERION.EXCLUSION.BUSINESS.BANKRUPTCY
 - classification.id 		CRITERION.EXCLUSION.MISCONDUCT.MARKET_DISTORTION
 - classification.id 		CRITERION.EXCLUSION.CONFLICT_OF_INTEREST.MISINTERPRETATION
 - classification.id 		CRITERION.EXCLUSION.NATIONAL.OTHER
 - classification.id 		CRITERION.OTHER.BID.LANGUAGE

[13:22:17] Patching tender...

[13:22:17] Processing data file: tender_patch.json

[13:22:17] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/b92ebe34a1a04126a384dc616cdc7f97?acc_token=26062ca3e924409199e5f4b4988d180c
[13:22:18] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/tenders/b92ebe34a1a04126a384dc616cdc7f97?acc_token=26062ca3e924409199e5f4b4988d180c HTTP/1.1" 200 61493
[13:22:18] Response status code: 200

[13:22:18] Tender patched:
 - id 				b92ebe34a1a04126a384dc616cdc7f97
 - status 			active.tendering

[13:22:18] Creating bids...

[13:22:18] Processing data file: bid_document.txt

[13:22:18] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[13:22:18] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 596
[13:22:18] Response status code: 200

[13:22:18] Processing data file: bid_create_0.json

[13:22:18] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/b92ebe34a1a04126a384dc616cdc7f97/bids
[13:22:18] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/b92ebe34a1a04126a384dc616cdc7f97/bids HTTP/1.1" 201 1949
[13:22:18] Response status code: 201

[13:22:18] Bid created:
 - id 				597c53fbe4b641e9bb259457737e84b6
 - token 			3892140650664ea4be60808908454cda
 - status 			draft

[13:22:18] Processing data file: bid_document.txt

[13:22:18] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[13:22:18] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 578
[13:22:18] Response status code: 200

[13:22:18] Processing data file: bid_create_1.json

[13:22:18] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/b92ebe34a1a04126a384dc616cdc7f97/bids
[13:22:18] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/b92ebe34a1a04126a384dc616cdc7f97/bids HTTP/1.1" 201 2050
[13:22:18] Response status code: 201

[13:22:18] Bid created:
 - id 				49fba6f9da504fa9b7e11f6f670a2549
 - token 			d65330e7bab548e689587a859081fcdc
 - status 			draft

[13:22:18] Processing data file: bid_document.txt

[13:22:18] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[13:22:19] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 596
[13:22:19] Response status code: 200

[13:22:19] Processing data file: bid_create_2.json

[13:22:19] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/b92ebe34a1a04126a384dc616cdc7f97/bids
[13:22:19] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/b92ebe34a1a04126a384dc616cdc7f97/bids HTTP/1.1" 201 2054
[13:22:19] Response status code: 201

[13:22:19] Bid created:
 - id 				79c31c0772e9426eabb2fb3be8b4d24b
 - token 			9873fef596904e8288991f9aea7e7e18
 - status 			draft

[13:22:19] Processing data file: bid_document.txt

[13:22:19] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[13:22:20] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 582
[13:22:20] Response status code: 200

[13:22:20] Processing data file: bid_create_3.json

[13:22:20] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/b92ebe34a1a04126a384dc616cdc7f97/bids
[13:22:20] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/b92ebe34a1a04126a384dc616cdc7f97/bids HTTP/1.1" 201 2050
[13:22:20] Response status code: 201

[13:22:20] Bid created:
 - id 				2a67135710c142c0b58416d16e971e35
 - token 			32feba0773e643b3b0f76d1bd3614dd9
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
