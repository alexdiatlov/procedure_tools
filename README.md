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
[12:17:30] Using seed 390886

[12:17:30] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[12:17:30] Starting new HTTPS connection (1): lb-api-sandbox-2.prozorro.gov.ua:443
[12:17:30] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 887419
[12:17:30] Response status code: 200

[12:17:30] Client time delta with server: 0 seconds

[12:17:30] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[12:17:31] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 887419
[12:17:31] Response status code: 200

[12:17:31] Client time delta with server: 0 seconds

[12:17:31] Creating plan...

[12:17:31] Processing data file: plan_create.json

[12:17:31] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans
[12:17:31] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans HTTP/1.1" 201 4186
[12:17:31] Response status code: 201

[12:17:31] Plan created:
 - id 				acc910711d9747ec8f1cf86213bbe8a9
 - token 			c088777ceeea4d9587ccd1df0e559b97
 - transfer 			ca0cc9fbd46c4c909bcd9d9cbc0b81d9
 - status 			draft

[12:17:31] Patching plan...

[12:17:31] Processing data file: plan_patch.json

[12:17:31] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/acc910711d9747ec8f1cf86213bbe8a9?acc_token=c088777ceeea4d9587ccd1df0e559b97
[12:17:31] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/plans/acc910711d9747ec8f1cf86213bbe8a9?acc_token=c088777ceeea4d9587ccd1df0e559b97 HTTP/1.1" 200 4085
[12:17:31] Response status code: 200

[12:17:31] Plan patched:
 - id 				acc910711d9747ec8f1cf86213bbe8a9
 - status 			scheduled

[12:17:31] Creating tender...

[12:17:31] Processing data file: tender_create.json

[12:17:31] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/acc910711d9747ec8f1cf86213bbe8a9/tenders
[12:17:31] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans/acc910711d9747ec8f1cf86213bbe8a9/tenders HTTP/1.1" 201 7463
[12:17:31] Response status code: 201

[12:17:31] Tender created:
 - id 				c7e181e9d7654fd0ae5012f93a1b75ed
 - token 			83cf1378587541d49fd12e6062d3d45b
 - transfer 			4704cfa46e5042c0b59f59b8cb9c6aaf
 - status 			draft
 - tenderID 			UA-2024-07-18-000048-a
 - procurementMethodType 	closeFrameworkAgreementUA

[12:17:31] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/c7e181e9d7654fd0ae5012f93a1b75ed
[12:17:31] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/tenders/c7e181e9d7654fd0ae5012f93a1b75ed HTTP/1.1" 200 7358
[12:17:31] Response status code: 200

[12:17:31] Processing data file: tender_document.txt

[12:17:31] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:31] Starting new HTTPS connection (1): upload-docs-sandbox-2.prozorro.gov.ua:443
[12:17:31] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 575
[12:17:31] Response status code: 200

[12:17:31] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/c7e181e9d7654fd0ae5012f93a1b75ed/documents?acc_token=83cf1378587541d49fd12e6062d3d45b
[12:17:31] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/c7e181e9d7654fd0ae5012f93a1b75ed/documents?acc_token=83cf1378587541d49fd12e6062d3d45b HTTP/1.1" 201 544
[12:17:31] Response status code: 201

[12:17:31] Create tender criteria...

[12:17:31] Processing data file: criteria_create.json

[12:17:31] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/c7e181e9d7654fd0ae5012f93a1b75ed/criteria?acc_token=83cf1378587541d49fd12e6062d3d45b
[12:17:33] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/c7e181e9d7654fd0ae5012f93a1b75ed/criteria?acc_token=83cf1378587541d49fd12e6062d3d45b HTTP/1.1" 201 53697
[12:17:33] Response status code: 201

[12:17:33] Tender criteria created:
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

[12:17:33] Processing data file: tender_notice.p7s

[12:17:33] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:33] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 589
[12:17:33] Response status code: 200

[12:17:33] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/c7e181e9d7654fd0ae5012f93a1b75ed/documents?acc_token=83cf1378587541d49fd12e6062d3d45b
[12:17:33] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/c7e181e9d7654fd0ae5012f93a1b75ed/documents?acc_token=83cf1378587541d49fd12e6062d3d45b HTTP/1.1" 201 566
[12:17:33] Response status code: 201

[12:17:33] Patching tender...

[12:17:33] Processing data file: tender_patch.json

[12:17:33] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/c7e181e9d7654fd0ae5012f93a1b75ed?acc_token=83cf1378587541d49fd12e6062d3d45b
[12:17:33] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/tenders/c7e181e9d7654fd0ae5012f93a1b75ed?acc_token=83cf1378587541d49fd12e6062d3d45b HTTP/1.1" 200 62227
[12:17:33] Response status code: 200

[12:17:33] Tender patched:
 - id 				c7e181e9d7654fd0ae5012f93a1b75ed
 - status 			active.tendering

[12:17:33] Skipping complaints creating: bot and reviewer tokens are required

[12:17:33] Creating bids...

[12:17:33] Processing data file: bid_document.txt

[12:17:33] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:33] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 574
[12:17:33] Response status code: 200

[12:17:33] Processing data file: bid_confidential_document.txt

[12:17:33] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:33] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 599
[12:17:33] Response status code: 200

[12:17:33] Processing data file: bid_eligibility_document.txt

[12:17:33] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:34] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 584
[12:17:34] Response status code: 200

[12:17:34] Processing data file: bid_financial_document.txt

[12:17:34] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:34] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 600
[12:17:34] Response status code: 200

[12:17:34] Processing data file: bid_qualification_document.txt

[12:17:34] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:34] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 584
[12:17:34] Response status code: 200

[12:17:34] Processing data file: bid_create_0.json

[12:17:34] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/c7e181e9d7654fd0ae5012f93a1b75ed/bids
[12:17:34] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/c7e181e9d7654fd0ae5012f93a1b75ed/bids HTTP/1.1" 201 4114
[12:17:34] Response status code: 201

[12:17:34] Bid created:
 - id 				31f2c12dba8749e18ac4261bf5e823b8
 - token 			e7ee5169718c49258bdadb3f89491587
 - status 			draft

[12:17:34] Processing data file: bid_document.txt

[12:17:34] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:34] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 586
[12:17:34] Response status code: 200

[12:17:34] Processing data file: bid_confidential_document.txt

[12:17:34] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:34] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 591
[12:17:34] Response status code: 200

[12:17:34] Processing data file: bid_eligibility_document.txt

[12:17:34] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:34] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 592
[12:17:34] Response status code: 200

[12:17:34] Processing data file: bid_financial_document.txt

[12:17:34] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:35] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 588
[12:17:35] Response status code: 200

[12:17:35] Processing data file: bid_qualification_document.txt

[12:17:35] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:35] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 600
[12:17:35] Response status code: 200

[12:17:35] Processing data file: bid_create_1.json

[12:17:35] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/c7e181e9d7654fd0ae5012f93a1b75ed/bids
[12:17:35] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/c7e181e9d7654fd0ae5012f93a1b75ed/bids HTTP/1.1" 201 4203
[12:17:35] Response status code: 201

[12:17:35] Bid created:
 - id 				9342fd978f7d4061a41b59a8e43415fe
 - token 			f0a74fa2b06140358fbdc489c005dbbb
 - status 			draft

[12:17:35] Processing data file: bid_document.txt

[12:17:35] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:35] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 578
[12:17:35] Response status code: 200

[12:17:35] Processing data file: bid_confidential_document.txt

[12:17:35] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:35] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 585
[12:17:35] Response status code: 200

[12:17:35] Processing data file: bid_eligibility_document.txt

[12:17:35] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:35] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 588
[12:17:35] Response status code: 200

[12:17:35] Processing data file: bid_financial_document.txt

[12:17:35] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:35] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 586
[12:17:35] Response status code: 200

[12:17:35] Processing data file: bid_qualification_document.txt

[12:17:35] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:36] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 596
[12:17:36] Response status code: 200

[12:17:36] Processing data file: bid_create_2.json

[12:17:36] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/c7e181e9d7654fd0ae5012f93a1b75ed/bids
[12:17:36] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/c7e181e9d7654fd0ae5012f93a1b75ed/bids HTTP/1.1" 201 4197
[12:17:36] Response status code: 201

[12:17:36] Bid created:
 - id 				7485d1314fdb4430b324f34c86aa0288
 - token 			ec7baddae335417580b8ca582084f6e1
 - status 			draft

[12:17:36] Processing data file: bid_document.txt

[12:17:36] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:36] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 584
[12:17:36] Response status code: 200

[12:17:36] Processing data file: bid_confidential_document.txt

[12:17:36] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:36] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 577
[12:17:36] Response status code: 200

[12:17:36] Processing data file: bid_eligibility_document.txt

[12:17:36] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:36] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 592
[12:17:36] Response status code: 200

[12:17:36] Processing data file: bid_financial_document.txt

[12:17:36] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:36] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 574
[12:17:36] Response status code: 200

[12:17:36] Processing data file: bid_qualification_document.txt

[12:17:36] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:17:36] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 590
[12:17:36] Response status code: 200

[12:17:36] Processing data file: bid_create_3.json

[12:17:36] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/c7e181e9d7654fd0ae5012f93a1b75ed/bids
[12:17:36] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/c7e181e9d7654fd0ae5012f93a1b75ed/bids HTTP/1.1" 201 4203
[12:17:36] Response status code: 201

[12:17:36] Bid created:
 - id 				2c45c5b463c94f04aaea8185002cf37d
 - token 			23d79721fb1e4779b97e56dc053f1f46
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
