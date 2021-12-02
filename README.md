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
[12:04:13] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[12:04:13] Starting new HTTPS connection (1): lb-api-sandbox-2.prozorro.gov.ua:443
[12:04:13] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 991876
[12:04:13] Response status code: 200

[12:04:13] Client time delta with server: 0 seconds

[12:04:13] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[12:04:13] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 991876
[12:04:13] Response status code: 200

[12:04:13] Client time delta with server: 0 seconds

[12:04:13] Creating plan...

[12:04:13] Processing data file: plan_create.json

[12:04:13] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans
[12:04:13] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans HTTP/1.1" 201 4186
[12:04:13] Response status code: 201

[12:04:13] Plan created:
 - id 				9c221c191012496ab41a98d11e7c244d
 - token 			956f0e930f89497ab7542b0f4fee0046
 - transfer 			8d8a0b2f92f24f52bbaee075d9b99847

[12:04:13] Creating tender...

[12:04:13] Processing data file: tender_create.json

[12:04:13] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/9c221c191012496ab41a98d11e7c244d/tenders
[12:04:13] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans/9c221c191012496ab41a98d11e7c244d/tenders HTTP/1.1" 201 7149
[12:04:13] Response status code: 201

[12:04:13] Tender created:
 - id 				65fd6b342f784c769798fdef6014a926
 - token 			9e6ae082836b4bb79c2dee8816be9ff3
 - transfer 			bc7e8af0a5404404919e908cc4721fde
 - status 			draft
 - tenderID 			UA-2021-12-02-000208-a
 - procurementMethodType 	closeFrameworkAgreementUA

[12:04:13] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/65fd6b342f784c769798fdef6014a926
[12:04:13] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/tenders/65fd6b342f784c769798fdef6014a926 HTTP/1.1" 200 7044
[12:04:13] Response status code: 200

[12:04:13] Create tender criteria...

[12:04:13] Processing data file: criteria_create.json

[12:04:13] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/65fd6b342f784c769798fdef6014a926/criteria?acc_token=9e6ae082836b4bb79c2dee8816be9ff3
[12:04:13] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/65fd6b342f784c769798fdef6014a926/criteria?acc_token=9e6ae082836b4bb79c2dee8816be9ff3 HTTP/1.1" 201 53725
[12:04:13] Response status code: 201

[12:04:13] Tender criteria created:
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

[12:04:13] Patching tender...

[12:04:13] Processing data file: tender_patch.json

[12:04:13] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/65fd6b342f784c769798fdef6014a926?acc_token=9e6ae082836b4bb79c2dee8816be9ff3
[12:04:14] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/tenders/65fd6b342f784c769798fdef6014a926?acc_token=9e6ae082836b4bb79c2dee8816be9ff3 HTTP/1.1" 200 60965
[12:04:14] Response status code: 200

[12:04:14] Tender status patched:
 - id 				65fd6b342f784c769798fdef6014a926
 - status 			active.tendering

[12:04:14] Creating bids...

[12:04:14] Processing data file: bid_document.txt

[12:04:14] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:04:14] Starting new HTTPS connection (1): upload-docs-sandbox-2.prozorro.gov.ua:443
[12:04:14] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 574
[12:04:14] Response status code: 200

[12:04:14] Processing data file: bid_create_0.json

[12:04:14] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/65fd6b342f784c769798fdef6014a926/bids
[12:04:14] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/65fd6b342f784c769798fdef6014a926/bids HTTP/1.1" 201 1951
[12:04:14] Response status code: 201

[12:04:14] Bid created:
 - id 				1f52484f554748bdbe8462e747ce1978
 - token 			f79a84d4a36c4811a5037afea5669750
 - status 			draft

[12:04:14] Processing data file: bid_document.txt

[12:04:14] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:04:14] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 584
[12:04:14] Response status code: 200

[12:04:14] Processing data file: bid_create_1.json

[12:04:14] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/65fd6b342f784c769798fdef6014a926/bids
[12:04:14] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/65fd6b342f784c769798fdef6014a926/bids HTTP/1.1" 201 2048
[12:04:14] Response status code: 201

[12:04:14] Bid created:
 - id 				e306b9fab8834e4897d49ee13465b7dc
 - token 			8e7dd6e1819944d09f9c372595d6a2bb
 - status 			draft

[12:04:14] Processing data file: bid_document.txt

[12:04:14] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:04:14] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 584
[12:04:14] Response status code: 200

[12:04:14] Processing data file: bid_create_2.json

[12:04:14] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/65fd6b342f784c769798fdef6014a926/bids
[12:04:15] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/65fd6b342f784c769798fdef6014a926/bids HTTP/1.1" 201 2060
[12:04:15] Response status code: 201

[12:04:15] Bid created:
 - id 				d2dfff80cf7b47398c73872c31a7bf04
 - token 			f0f9a34209ca40dd9ef910a959e75750
 - status 			draft

[12:04:15] Processing data file: bid_document.txt

[12:04:15] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:04:15] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 582
[12:04:15] Response status code: 200

[12:04:15] Processing data file: bid_create_3.json

[12:04:15] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/65fd6b342f784c769798fdef6014a926/bids
[12:04:15] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/65fd6b342f784c769798fdef6014a926/bids HTTP/1.1" 201 2056
[12:04:15] Response status code: 201

[12:04:15] Bid created:
 - id 				ac3e666ef0794351bd839265b84ca28f
 - token 			3df527d591664912909435acf878eaea
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
