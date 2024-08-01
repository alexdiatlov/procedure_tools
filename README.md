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
                 [-m quick(mode:no-auction)] [-s tender_create.json]
                 [-w edr-qualification] [-e SEED]
                 [--reviewer-token REVIEWER_TOKEN] [--bot-token BOT_TOKEN]
                 [--debug]
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
                         - aboveThreshold
                         - aboveThreshold.features
                         - aboveThreshold.lcc
                         - aboveThresholdEU
                         - aboveThresholdEU.features
                         - aboveThresholdEU.lcc
                         - aboveThresholdUA
                         - aboveThresholdUA.features
                         - aboveThresholdUA.lcc
                         - belowThreshold
                         - belowThreshold.central
                         - belowThreshold.features
                         - closeFrameworkAgreementUA
                         - closeFrameworkAgreementUA.central
                         - competitiveDialogueEU
                         - competitiveDialogueUA
                         - competitiveDialogueUA.features
                         - esco
                         - esco.features
                         - negotiation
                         - negotiation.quick
                         - reporting
                         - simple.defense

  -m quick(mode:no-auction), --submission quick(mode:no-auction)
                        value for submissionMethodDetails, one of:
                         - quick
                         - quick(mode:no-auction)
                         - quick(mode:fast-auction)
                         - quick(mode:fast-forward)

  -s tender_create.json, --stop tender_create.json
                        data file name to stop after

  -w edr-qualification, --wait edr-qualification
                        wait for event, one or many of (divided by comma):
                         - edr-qualification
                         - edr-pre-qualification

  -e SEED, --seed SEED  faker seed

  --reviewer-token REVIEWER_TOKEN
                        reviewer token

  --bot-token BOT_TOKEN
                        bot token

  --debug               Show requests and responses
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
[02:54:27] Using seed 165011

[02:54:27] Initializing tenders client

[02:54:27] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[02:54:27] Starting new HTTPS connection (1): lb-api-sandbox-2.prozorro.gov.ua:443
[02:54:28] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/11" 200 887419
[02:54:28] Response status code: 200

[02:54:28] Client time delta with server: -842 milliseconds

[02:54:28] Initializing contracts client

[02:54:28] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[02:54:29] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/11" 200 887419
[02:54:30] Response status code: 200

[02:54:30] Client time delta with server: -1631 milliseconds

[02:54:30] Initializing plans client

[02:54:30] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[02:54:30] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/11" 200 887419
[02:54:31] Response status code: 200

[02:54:31] Client time delta with server: -1132 milliseconds

[02:54:31] Initializing ds client

[02:54:31] Using client time delta with server: -1631 milliseconds

[02:54:31] Creating plan...

[02:54:31] Processing data file: plan_create.json

[02:54:31] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans
[02:54:31] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans HTTP/11" 201 4202
[02:54:31] Response status code: 201

[02:54:31] Plan created:
 - id 				95abb1390c4e44e6947fd058d3a2f2e8
 - token 			a3704908075f4ff6a18fd2ae49c9bcaa
 - transfer 			25cdb892c9704139b6f661144ed88e89
 - status 			draft

[02:54:31] Patching plan...

[02:54:31] Processing data file: plan_patch.json

[02:54:31] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/95abb1390c4e44e6947fd058d3a2f2e8?acc_token=a3704908075f4ff6a18fd2ae49c9bcaa
[02:54:31] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/plans/95abb1390c4e44e6947fd058d3a2f2e8?acc_token=a3704908075f4ff6a18fd2ae49c9bcaa HTTP/11" 200 4101
[02:54:31] Response status code: 200

[02:54:31] Plan patched:
 - id 				95abb1390c4e44e6947fd058d3a2f2e8
 - status 			scheduled

[02:54:31] Creating tender...

[02:54:31] Processing data file: tender_create.json

[02:54:31] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/95abb1390c4e44e6947fd058d3a2f2e8/tenders
[02:54:31] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans/95abb1390c4e44e6947fd058d3a2f2e8/tenders HTTP/11" 201 7169
[02:54:31] Response status code: 201

[02:54:31] Tender created:
 - id 				f433072d5e314f49ba17baf8f17e1185
 - token 			57ef798e177f49b88694644492384414
 - transfer 			701691cce52c4d569c56c93d49fd5e6e
 - status 			draft
 - tenderID 			UA-2024-08-01-000005-a
 - procurementMethodType 	closeFrameworkAgreementUA

[02:54:31] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/f433072d5e314f49ba17baf8f17e1185
[02:54:31] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/tenders/f433072d5e314f49ba17baf8f17e1185 HTTP/11" 200 7064
[02:54:31] Response status code: 200

[02:54:31] Processing data file: tender_document.txt

[02:54:31] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[02:54:31] Starting new HTTPS connection (1): upload-docs-sandbox-2.prozorro.gov.ua:443
[02:54:32] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/11" 200 603
[02:54:32] Response status code: 200

[02:54:32] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/f433072d5e314f49ba17baf8f17e1185/documents?acc_token=57ef798e177f49b88694644492384414
[02:54:32] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/f433072d5e314f49ba17baf8f17e1185/documents?acc_token=57ef798e177f49b88694644492384414 HTTP/11" 201 546
[02:54:32] Response status code: 201

[02:54:32] Create tender criteria...

[02:54:32] Processing data file: criteria_create.json

[02:54:32] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/f433072d5e314f49ba17baf8f17e1185/criteria?acc_token=57ef798e177f49b88694644492384414
[02:54:32] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/f433072d5e314f49ba17baf8f17e1185/criteria?acc_token=57ef798e177f49b88694644492384414 HTTP/11" 201 53697
[02:54:32] Response status code: 201

[02:54:32] Tender criteria created:
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

[02:54:32] Processing data file: tender_notice.p7s

[02:54:32] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[02:54:32] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/11" 200 579
[02:54:32] Response status code: 200

[02:54:32] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/f433072d5e314f49ba17baf8f17e1185/documents?acc_token=57ef798e177f49b88694644492384414
[02:54:32] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/f433072d5e314f49ba17baf8f17e1185/documents?acc_token=57ef798e177f49b88694644492384414 HTTP/11" 201 564
[02:54:32] Response status code: 201

[02:54:32] Patching tender...

[02:54:32] Processing data file: tender_patch.json

[02:54:32] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/f433072d5e314f49ba17baf8f17e1185?acc_token=57ef798e177f49b88694644492384414
[02:54:33] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/tenders/f433072d5e314f49ba17baf8f17e1185?acc_token=57ef798e177f49b88694644492384414 HTTP/11" 200 61933
[02:54:33] Response status code: 200

[02:54:33] Tender patched:
 - id 				f433072d5e314f49ba17baf8f17e1185
 - status 			active.tendering

[02:54:33] Skipping complaints creating: bot and reviewer tokens are required

[02:54:33] Creating bids...

[02:54:33] Processing data file: bid_document.txt

[02:54:33] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[02:54:33] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/11" 200 582
[02:54:33] Response status code: 200

[02:54:33] Processing data file: bid_confidential_document.txt

[02:54:33] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[02:54:33] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/11" 200 591
[02:54:33] Response status code: 200

[02:54:33] Processing data file: bid_eligibility_document.txt

[02:54:33] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[02:54:33] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/11" 200 592
[02:54:33] Response status code: 200

[02:54:33] Processing data file: bid_financial_document.txt

[02:54:33] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[02:54:33] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/11" 200 588
[02:54:33] Response status code: 200

[02:54:33] Processing data file: bid_qualification_document.txt

[02:54:33] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[02:54:33] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/11" 200 608
[02:54:33] Response status code: 200

[02:54:33] Processing data file: bid_create_0.json

[02:54:33] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/f433072d5e314f49ba17baf8f17e1185/bids
[02:54:33] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/f433072d5e314f49ba17baf8f17e1185/bids HTTP/11" 403 141
[02:54:33] Response status code: 403

[02:54:33] Response text:

[02:54:33] {"status": "error", "errors": [{"location": "body", "name": "data", "description": "Can't add bid in current (unsuccessful) tender status"}]}

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
