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
[11:59:00] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[11:59:00] Starting new HTTPS connection (1): lb-api-sandbox-2.prozorro.gov.ua:443
[11:59:00] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 991876
[11:59:00] Response status code: 200

[11:59:00] Client time delta with server: 0 seconds

[11:59:00] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[11:59:01] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 991876
[11:59:01] Response status code: 200

[11:59:01] Client time delta with server: 0 seconds

[11:59:01] Creating plan...

[11:59:01] Processing data file: plan_create.json

[11:59:01] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans
[11:59:01] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans HTTP/1.1" 201 4186
[11:59:01] Response status code: 201

[11:59:01] Plan created:
 - id 				7c55705a72f94e7389f937f5764fea40
 - token 			a676d25867e8483eb879b37e9e136828
 - transfer 			df83fe34776243efb5bbb7eabea160d7

[11:59:01] Creating tender...

[11:59:01] Processing data file: tender_create.json

[11:59:01] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/7c55705a72f94e7389f937f5764fea40/tenders
[11:59:01] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans/7c55705a72f94e7389f937f5764fea40/tenders HTTP/1.1" 201 7149
[11:59:01] Response status code: 201

[11:59:01] Tender created:
 - id 				a161664c451c4855bb5fbb65e60fd56e
 - token 			c26feb6296e9461abb99a8e5f17addd6
 - transfer 			6513082527454e98b5e37871140ce29a
 - status 			draft
 - tenderID 			UA-2021-12-02-000198-a
 - procurementMethodType 	closeFrameworkAgreementUA

[11:59:01] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/a161664c451c4855bb5fbb65e60fd56e
[11:59:01] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/tenders/a161664c451c4855bb5fbb65e60fd56e HTTP/1.1" 200 7044
[11:59:01] Response status code: 200

[11:59:01] Create tender criteria...

[11:59:01] Processing data file: criteria_create.json

[11:59:01] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/a161664c451c4855bb5fbb65e60fd56e/criteria?acc_token=c26feb6296e9461abb99a8e5f17addd6
[11:59:01] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/a161664c451c4855bb5fbb65e60fd56e/criteria?acc_token=c26feb6296e9461abb99a8e5f17addd6 HTTP/1.1" 201 53725
[11:59:01] Response status code: 201

[11:59:01] Tender criteria created:
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

[11:59:01] Patching tender...

[11:59:01] Processing data file: tender_patch.json

[11:59:01] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/a161664c451c4855bb5fbb65e60fd56e?acc_token=c26feb6296e9461abb99a8e5f17addd6
[11:59:02] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/tenders/a161664c451c4855bb5fbb65e60fd56e?acc_token=c26feb6296e9461abb99a8e5f17addd6 HTTP/1.1" 200 60965
[11:59:02] Response status code: 200

[11:59:02] Tender status patched:
 - id 				a161664c451c4855bb5fbb65e60fd56e
 - status 			active.tendering

[11:59:02] Creating bids...

[11:59:02] Processing data file: bid_document.txt

[11:59:02] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[11:59:02] Starting new HTTPS connection (1): upload-docs-sandbox-2.prozorro.gov.ua:443
[11:59:02] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 580
[11:59:02] Response status code: 200

[11:59:02] Processing data file: bid_create_0.json

[11:59:02] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/a161664c451c4855bb5fbb65e60fd56e/bids
[11:59:02] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/a161664c451c4855bb5fbb65e60fd56e/bids HTTP/1.1" 201 1951
[11:59:02] Response status code: 201

[11:59:02] Bid created:
 - id 				1238a344bc634243bb667ca4d9f779d8
 - token 			8c9de6297368461fb8d6c7d6ff18a6d8
 - status 			draft

[11:59:02] Processing data file: bid_document.txt

[11:59:02] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[11:59:02] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 574
[11:59:02] Response status code: 200

[11:59:02] Processing data file: bid_create_1.json

[11:59:02] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/a161664c451c4855bb5fbb65e60fd56e/bids
[11:59:02] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/a161664c451c4855bb5fbb65e60fd56e/bids HTTP/1.1" 201 2054
[11:59:02] Response status code: 201

[11:59:02] Bid created:
 - id 				75a82db997f64328b64c8c8ee872644b
 - token 			77f9cd0576e1452fb0817a58de4957ea
 - status 			draft

[11:59:02] Processing data file: bid_document.txt

[11:59:02] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[11:59:02] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 580
[11:59:02] Response status code: 200

[11:59:02] Processing data file: bid_create_2.json

[11:59:02] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/a161664c451c4855bb5fbb65e60fd56e/bids
[11:59:02] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/a161664c451c4855bb5fbb65e60fd56e/bids HTTP/1.1" 201 2048
[11:59:02] Response status code: 201

[11:59:02] Bid created:
 - id 				836d70190b4f4b3384c835b1aa73a307
 - token 			bb1ff2fb3a4749228633937da6773486
 - status 			draft

[11:59:02] Processing data file: bid_document.txt

[11:59:02] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[11:59:02] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 592
[11:59:02] Response status code: 200

[11:59:02] Processing data file: bid_create_3.json

[11:59:02] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/a161664c451c4855bb5fbb65e60fd56e/bids
[11:59:02] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/a161664c451c4855bb5fbb65e60fd56e/bids HTTP/1.1" 201 2054
[11:59:02] Response status code: 201

[11:59:02] Bid created:
 - id 				ecbfd619ccd643b390152fa673497003
 - token 			1446c22568cf4404ae126c13a8a3b032
 - status 			draft

```

## Update readme

Pass API token as parameter to README.sh
```
API_HOST=https://lb-api-sandbox-2.prozorro.gov.ua API_TOKEN=broker_api_token DS_HOST=https://upload-docs-sandbox-2.prozorro.gov.ua DS_USERNAME=broker_ds_username DS_PASSWORD=broker_ds_password ./README.sh
```
or
```
export API_HOST=https://lb-api-sandbox-2.prozorro.gov.ua
export API_TOKEN=broker_api_token
export DS_HOST=https://upload-docs-sandbox-2.prozorro.gov.ua
export DS_USERNAME=broker_ds_username
export DS_PASSWORD=broker_ds_password

./README.sh
```

## Run tests

```
API_HOST=https://lb-api-sandbox-2.prozorro.gov.ua API_TOKEN=broker_api_token DS_HOST=https://upload-docs-sandbox-2.prozorro.gov.ua DS_USERNAME=broker_ds_username DS_PASSWORD=broker_ds_password python setup.py test
```
or
```
export API_HOST=https://lb-api-sandbox-2.prozorro.gov.ua
export API_TOKEN=broker_api_token
export DS_HOST=https://upload-docs-sandbox-2.prozorro.gov.ua
export DS_USERNAME=broker_ds_username
export DS_PASSWORD=broker_ds_password

python setup.py test
```
