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

optional arguments:
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
[03:45:30] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[03:45:30] Starting new HTTPS connection (1): lb-api-sandbox-2.prozorro.gov.ua:443
[03:45:30] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 1322994
[03:45:30] Response status code: 200

[03:45:30] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[03:45:31] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 1322994
[03:45:32] Response status code: 200

[03:45:32] Creating plan...

[03:45:32] Processing data file: plan_create.json

[03:45:32] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans
[03:45:32] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans HTTP/1.1" 201 4051
[03:45:32] Response status code: 201

[03:45:32] Plan created:
 - id 				9dd53a52d26c4124beab1d3250cc4884
 - token 			bcdf29e45cdf4ad3b18f4798f3c2e3d6
 - transfer 			29dccb6701984d679d9fa8a3c4f7a63b

[03:45:32] Creating tender...

[03:45:32] Processing data file: tender_create.json

[03:45:32] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/9dd53a52d26c4124beab1d3250cc4884/tenders
[03:45:32] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans/9dd53a52d26c4124beab1d3250cc4884/tenders HTTP/1.1" 201 7097
[03:45:32] Response status code: 201

[03:45:32] Tender created:
 - id 				777be75e035c4dea929b5c84005e343d
 - token 			ba0f06d0f7da46d99d2feb68661511ef
 - transfer 			1e45064144044dc9be685f8ab01caa2d
 - status 			draft
 - tenderID 			UA-2021-05-31-000002-a
 - tenderID 			UA-2021-05-31-000002-a
 - procurementMethodType 	closeFrameworkAgreementUA

[03:45:32] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/777be75e035c4dea929b5c84005e343d
[03:45:32] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/tenders/777be75e035c4dea929b5c84005e343d HTTP/1.1" 200 6992
[03:45:32] Response status code: 200

[03:45:32] Create tender criteria...

[03:45:32] Processing data file: criteria_create.json

[03:45:32] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/777be75e035c4dea929b5c84005e343d/criteria?acc_token=ba0f06d0f7da46d99d2feb68661511ef
[03:45:33] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/777be75e035c4dea929b5c84005e343d/criteria?acc_token=ba0f06d0f7da46d99d2feb68661511ef HTTP/1.1" 201 53725
[03:45:33] Response status code: 201

[03:45:33] Tender criteria created:
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

[03:45:33] Patching tender...

[03:45:33] Processing data file: tender_patch.json

[03:45:33] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/777be75e035c4dea929b5c84005e343d?acc_token=ba0f06d0f7da46d99d2feb68661511ef
[03:45:33] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/tenders/777be75e035c4dea929b5c84005e343d?acc_token=ba0f06d0f7da46d99d2feb68661511ef HTTP/1.1" 200 60913
[03:45:33] Response status code: 200

[03:45:33] Tender status patched:
 - id 				777be75e035c4dea929b5c84005e343d
 - status 			active.tendering

[03:45:33] Creating bids...

[03:45:33] Processing data file: bid_document.txt

[03:45:33] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[03:45:33] Starting new HTTPS connection (1): upload-docs-sandbox-2.prozorro.gov.ua:443
[03:45:35] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 586
[03:45:35] Response status code: 200

[03:45:35] Processing data file: bid_create_0.json

[03:45:35] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/777be75e035c4dea929b5c84005e343d/bids
[03:45:36] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/777be75e035c4dea929b5c84005e343d/bids HTTP/1.1" 201 1956
[03:45:36] Response status code: 201

[03:45:36] Bid created:
 - id 				55297730f9364717966eca094f684b82
 - token 			6640b0c8905f431baf3cffc5fc7ec0c7
 - status 			draft

[03:45:36] Processing data file: bid_document.txt

[03:45:36] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[03:45:36] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 580
[03:45:36] Response status code: 200

[03:45:36] Processing data file: bid_create_1.json

[03:45:36] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/777be75e035c4dea929b5c84005e343d/bids
[03:45:36] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/777be75e035c4dea929b5c84005e343d/bids HTTP/1.1" 201 2056
[03:45:36] Response status code: 201

[03:45:36] Bid created:
 - id 				a339adb466c544bb939875c6bd7b2b03
 - token 			3b7e226ddb8b47b2a0de0ffc6af02b8d
 - status 			draft

[03:45:36] Processing data file: bid_document.txt

[03:45:36] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[03:45:36] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 572
[03:45:36] Response status code: 200

[03:45:36] Processing data file: bid_create_2.json

[03:45:36] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/777be75e035c4dea929b5c84005e343d/bids
[03:45:37] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/777be75e035c4dea929b5c84005e343d/bids HTTP/1.1" 201 2056
[03:45:37] Response status code: 201

[03:45:37] Bid created:
 - id 				c62cbddcd4894f17a73b3b3931024946
 - token 			c85f07ae45c748a29d58035ef7af4a19
 - status 			draft

[03:45:37] Processing data file: bid_document.txt

[03:45:37] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[03:45:37] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 576
[03:45:37] Response status code: 200

[03:45:37] Processing data file: bid_create_3.json

[03:45:37] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/777be75e035c4dea929b5c84005e343d/bids
[03:45:37] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/777be75e035c4dea929b5c84005e343d/bids HTTP/1.1" 201 2056
[03:45:37] Response status code: 201

[03:45:37] Bid created:
 - id 				839e89a8675046a186b00daa7d08d6ca
 - token 			ca21001790344482ae2f4a353112bfa1
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
