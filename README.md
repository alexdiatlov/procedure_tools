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
[10:44:46] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[10:44:46] Starting new HTTPS connection (1): lb-api-sandbox-2.prozorro.gov.ua:443
[10:44:46] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 1230991
[10:44:46] Response status code: 200

[10:44:46] Client time delta with server: 0 seconds

[10:44:46] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[10:44:47] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 1230991
[10:44:47] Response status code: 200

[10:44:47] Client time delta with server: 0 seconds

[10:44:47] Creating plan...

[10:44:47] Processing data file: plan_create.json

[10:44:47] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans
[10:44:47] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans HTTP/1.1" 201 4135
[10:44:47] Response status code: 201

[10:44:47] Plan created:
 - id 				ce3b01973eb1464c9883d8035648a1db
 - token 			8525790c6f414f30839f74d960af6952
 - transfer 			2304e1d551bb4f7ba7d3c97a1159e54c

[10:44:47] Creating tender...

[10:44:47] Processing data file: tender_create.json

[10:44:47] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/ce3b01973eb1464c9883d8035648a1db/tenders
[10:44:47] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans/ce3b01973eb1464c9883d8035648a1db/tenders HTTP/1.1" 201 7100
[10:44:47] Response status code: 201

[10:44:47] Tender created:
 - id 				1f3b075ae2c5480aad722020a1585b67
 - token 			2db3542fb7364e499aeae8db60425abb
 - transfer 			82ebd778922248af85622aeb8ecc17a3
 - status 			draft
 - tenderID 			UA-2021-09-07-000056-b
 - procurementMethodType 	closeFrameworkAgreementUA

[10:44:47] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/1f3b075ae2c5480aad722020a1585b67
[10:44:47] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/tenders/1f3b075ae2c5480aad722020a1585b67 HTTP/1.1" 200 6995
[10:44:47] Response status code: 200

[10:44:47] Create tender criteria...

[10:44:47] Processing data file: criteria_create.json

[10:44:47] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/1f3b075ae2c5480aad722020a1585b67/criteria?acc_token=2db3542fb7364e499aeae8db60425abb
[10:44:47] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/1f3b075ae2c5480aad722020a1585b67/criteria?acc_token=2db3542fb7364e499aeae8db60425abb HTTP/1.1" 201 53725
[10:44:47] Response status code: 201

[10:44:47] Tender criteria created:
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

[10:44:47] Patching tender...

[10:44:47] Processing data file: tender_patch.json

[10:44:47] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/1f3b075ae2c5480aad722020a1585b67?acc_token=2db3542fb7364e499aeae8db60425abb
[10:44:48] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/tenders/1f3b075ae2c5480aad722020a1585b67?acc_token=2db3542fb7364e499aeae8db60425abb HTTP/1.1" 200 60916
[10:44:48] Response status code: 200

[10:44:48] Tender status patched:
 - id 				1f3b075ae2c5480aad722020a1585b67
 - status 			active.tendering

[10:44:48] Creating bids...

[10:44:48] Processing data file: bid_document.txt

[10:44:48] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:44:48] Starting new HTTPS connection (1): upload-docs-sandbox-2.prozorro.gov.ua:443
[10:44:50] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 586
[10:44:50] Response status code: 200

[10:44:50] Processing data file: bid_create_0.json

[10:44:50] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/1f3b075ae2c5480aad722020a1585b67/bids
[10:44:50] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/1f3b075ae2c5480aad722020a1585b67/bids HTTP/1.1" 201 1933
[10:44:50] Response status code: 201

[10:44:50] Bid created:
 - id 				e7407b6bcce84f57897c3c9d0184635c
 - token 			fd9ca07a64d5491c94be03bb6e6b8440
 - status 			draft

[10:44:50] Processing data file: bid_document.txt

[10:44:50] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:44:50] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 582
[10:44:50] Response status code: 200

[10:44:50] Processing data file: bid_create_1.json

[10:44:50] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/1f3b075ae2c5480aad722020a1585b67/bids
[10:44:50] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/1f3b075ae2c5480aad722020a1585b67/bids HTTP/1.1" 201 2036
[10:44:50] Response status code: 201

[10:44:50] Bid created:
 - id 				30e477fbea7a4348aab0c2fe1611edaf
 - token 			7eefbd8f00ae4d52b4c074b4fe2a0745
 - status 			draft

[10:44:50] Processing data file: bid_document.txt

[10:44:50] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:44:52] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 572
[10:44:52] Response status code: 200

[10:44:52] Processing data file: bid_create_2.json

[10:44:52] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/1f3b075ae2c5480aad722020a1585b67/bids
[10:44:52] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/1f3b075ae2c5480aad722020a1585b67/bids HTTP/1.1" 201 2032
[10:44:52] Response status code: 201

[10:44:52] Bid created:
 - id 				2bccfd59a9154b6596118e9700b86849
 - token 			a2cab32c8c3f4c31a8cb40112794ffe0
 - status 			draft

[10:44:52] Processing data file: bid_document.txt

[10:44:52] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[10:44:52] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 574
[10:44:52] Response status code: 200

[10:44:52] Processing data file: bid_create_3.json

[10:44:52] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/1f3b075ae2c5480aad722020a1585b67/bids
[10:44:52] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/1f3b075ae2c5480aad722020a1585b67/bids HTTP/1.1" 201 2030
[10:44:52] Response status code: 201

[10:44:52] Bid created:
 - id 				8a212803de2b4f50b49470cbbcb51f75
 - token 			f1574dfea8fa45048a2fd96512a781b9
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
