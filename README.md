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
                         - aboveThreshold.multilot
                         - aboveThreshold.multilot.features
                         - aboveThreshold.multilot.lcc
                         - aboveThresholdEU
                         - aboveThresholdEU.lcc
                         - aboveThresholdEU.multilot
                         - aboveThresholdEU.multilot.features
                         - aboveThresholdEU.multilot.lcc
                         - aboveThresholdEU.plan
                         - aboveThresholdEU.tender
                         - aboveThresholdUA
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
                         - competitiveDialogueUA.multilot.features
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
[10:19:41] Using seed 729118

[10:19:41] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[10:19:41] Starting new HTTPS connection (1): lb-api-sandbox-2.prozorro.gov.ua:443
[10:19:42] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 913378
[10:19:42] Response status code: 200

[10:19:42] Client time delta with server: 0 seconds

[10:19:42] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[10:19:42] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 913378
[10:19:42] Response status code: 200

[10:19:42] Client time delta with server: 0 seconds

[10:19:42] Creating plan...

[10:19:42] Processing data file: plan_create.json

[10:19:42] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans
[10:19:42] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans HTTP/1.1" 201 4186
[10:19:42] Response status code: 201

[10:19:42] Plan created:
 - id 				c4f857b46eef49caa501975500a8232c
 - token 			5c2f3c197a4d4dd79b00baa3554591a2
 - transfer 			d08fbaf8eda64f60b51cb570fca6913e
 - status 			draft

[10:19:42] Patching plan...

[10:19:42] Processing data file: plan_patch.json

[10:19:42] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/c4f857b46eef49caa501975500a8232c?acc_token=5c2f3c197a4d4dd79b00baa3554591a2
[10:19:42] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/plans/c4f857b46eef49caa501975500a8232c?acc_token=5c2f3c197a4d4dd79b00baa3554591a2 HTTP/1.1" 200 4085
[10:19:42] Response status code: 200

[10:19:42] Plan patched:
 - id 				c4f857b46eef49caa501975500a8232c
 - status 			scheduled

[10:19:42] Creating tender...

[10:19:42] Processing data file: tender_create.json

[10:19:42] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/c4f857b46eef49caa501975500a8232c/tenders
[10:19:42] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans/c4f857b46eef49caa501975500a8232c/tenders HTTP/1.1" 201 7315
[10:19:42] Response status code: 201

[10:19:42] Tender created:
 - id 				29282737053046b8af285c9d22eb9390
 - token 			7cf8142387834497bfa911a38d044d31
 - transfer 			62b2eb00d9c2401d88549af317561670
 - status 			draft
 - tenderID 			UA-2023-07-19-000078-a
 - procurementMethodType 	closeFrameworkAgreementUA

[10:19:42] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/29282737053046b8af285c9d22eb9390
[10:19:42] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/tenders/29282737053046b8af285c9d22eb9390 HTTP/1.1" 200 7210
[10:19:42] Response status code: 200

[10:19:42] Processing data file: tender_document.txt

[10:19:42] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:19:42] Starting new HTTPS connection (1): upload-docs-sandbox-2.prozorro.gov.ua:443
[10:19:43] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 575
[10:19:43] Response status code: 200

[10:19:43] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/29282737053046b8af285c9d22eb9390/documents?acc_token=7cf8142387834497bfa911a38d044d31
[10:19:43] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/29282737053046b8af285c9d22eb9390/documents?acc_token=7cf8142387834497bfa911a38d044d31 HTTP/1.1" 201 544
[10:19:43] Response status code: 201

[10:19:43] Create tender criteria...

[10:19:43] Processing data file: criteria_create.json

[10:19:43] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/29282737053046b8af285c9d22eb9390/criteria?acc_token=7cf8142387834497bfa911a38d044d31
[10:19:43] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/29282737053046b8af285c9d22eb9390/criteria?acc_token=7cf8142387834497bfa911a38d044d31 HTTP/1.1" 201 53725
[10:19:43] Response status code: 201

[10:19:43] Tender criteria created:
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

[10:19:43] Patching tender...

[10:19:43] Processing data file: tender_patch.json

[10:19:43] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/29282737053046b8af285c9d22eb9390?acc_token=7cf8142387834497bfa911a38d044d31
[10:19:43] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/tenders/29282737053046b8af285c9d22eb9390?acc_token=7cf8142387834497bfa911a38d044d31 HTTP/1.1" 200 61577
[10:19:43] Response status code: 200

[10:19:43] Tender patched:
 - id 				29282737053046b8af285c9d22eb9390
 - status 			active.tendering

[10:19:43] Skipping complaints creating: bot and reviewer tokens are required

[10:19:43] Creating bids...

[10:19:43] Processing data file: bid_document.txt

[10:19:43] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:19:44] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 584
[10:19:44] Response status code: 200

[10:19:44] Processing data file: bid_confidential_document.txt

[10:19:44] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:19:44] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 591
[10:19:44] Response status code: 200

[10:19:44] Processing data file: bid_eligibility_document.txt

[10:19:44] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:19:44] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 582
[10:19:44] Response status code: 200

[10:19:44] Processing data file: bid_financial_document.txt

[10:19:44] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:19:44] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 596
[10:19:44] Response status code: 200

[10:19:44] Processing data file: bid_qualification_document.txt

[10:19:44] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:19:44] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 588
[10:19:44] Response status code: 200

[10:19:44] Processing data file: bid_create_0.json

[10:19:44] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/29282737053046b8af285c9d22eb9390/bids
[10:19:44] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/29282737053046b8af285c9d22eb9390/bids HTTP/1.1" 201 4168
[10:19:44] Response status code: 201

[10:19:44] Bid created:
 - id 				cb670e70559649398c4b253c2c7c1e86
 - token 			9cfa94f4fcf149878d5188aa727c6419
 - status 			draft

[10:19:44] Processing data file: bid_document.txt

[10:19:44] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:19:44] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 580
[10:19:44] Response status code: 200

[10:19:44] Processing data file: bid_confidential_document.txt

[10:19:44] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:19:44] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 597
[10:19:44] Response status code: 200

[10:19:44] Processing data file: bid_eligibility_document.txt

[10:19:44] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:19:45] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 590
[10:19:45] Response status code: 200

[10:19:45] Processing data file: bid_financial_document.txt

[10:19:45] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:19:45] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 596
[10:19:45] Response status code: 200

[10:19:45] Processing data file: bid_qualification_document.txt

[10:19:45] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:19:45] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 582
[10:19:45] Response status code: 200

[10:19:45] Processing data file: bid_create_1.json

[10:19:45] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/29282737053046b8af285c9d22eb9390/bids
[10:19:45] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/29282737053046b8af285c9d22eb9390/bids HTTP/1.1" 201 4267
[10:19:45] Response status code: 201

[10:19:45] Bid created:
 - id 				55699e3ee704402db34b1671016b6e70
 - token 			466d98c24a1e44bcb93fa62cabe5df33
 - status 			draft

[10:19:45] Processing data file: bid_document.txt

[10:19:45] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:19:45] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 576
[10:19:45] Response status code: 200

[10:19:45] Processing data file: bid_confidential_document.txt

[10:19:45] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:19:45] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 595
[10:19:45] Response status code: 200

[10:19:45] Processing data file: bid_eligibility_document.txt

[10:19:45] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:19:45] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 586
[10:19:45] Response status code: 200

[10:19:45] Processing data file: bid_financial_document.txt

[10:19:45] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:19:45] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 578
[10:19:45] Response status code: 200

[10:19:45] Processing data file: bid_qualification_document.txt

[10:19:45] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:19:45] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 592
[10:19:45] Response status code: 200

[10:19:45] Processing data file: bid_create_2.json

[10:19:45] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/29282737053046b8af285c9d22eb9390/bids
[10:19:46] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/29282737053046b8af285c9d22eb9390/bids HTTP/1.1" 201 4263
[10:19:46] Response status code: 201

[10:19:46] Bid created:
 - id 				572722e7867148808b50081f50276c8c
 - token 			d840433fdbe147f88d3e6dca9959bb90
 - status 			draft

[10:19:46] Processing data file: bid_document.txt

[10:19:46] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:19:46] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 580
[10:19:46] Response status code: 200

[10:19:46] Processing data file: bid_confidential_document.txt

[10:19:46] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:19:46] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 597
[10:19:46] Response status code: 200

[10:19:46] Processing data file: bid_eligibility_document.txt

[10:19:46] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:19:46] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 594
[10:19:46] Response status code: 200

[10:19:46] Processing data file: bid_financial_document.txt

[10:19:46] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:19:46] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 590
[10:19:46] Response status code: 200

[10:19:46] Processing data file: bid_qualification_document.txt

[10:19:46] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:19:46] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 586
[10:19:46] Response status code: 200

[10:19:46] Processing data file: bid_create_3.json

[10:19:46] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/29282737053046b8af285c9d22eb9390/bids
[10:19:46] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/29282737053046b8af285c9d22eb9390/bids HTTP/1.1" 201 4263
[10:19:46] Response status code: 201

[10:19:46] Bid created:
 - id 				82d4e5c95ae24eda9c9d00d6241c4872
 - token 			123b906ac0634f00808a224b850ab86d
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
