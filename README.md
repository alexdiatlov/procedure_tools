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
                        ['competitiveDialogueUA', 'reporting',
                        'esco.multilot', 'belowThreshold', 'aboveThresholdUA',
                        'aboveThresholdEU.plan', 'closeFrameworkAgreementUA',
                        'belowThreshold.multilot', 'aboveThresholdEU.tender',
                        'negotiation.quick', 'esco',
                        'closeFrameworkAgreementUA.central',
                        'aboveThresholdUA.defense', 'belowThreshold.features',
                        'competitiveDialogueEU', 'aboveThresholdEU.multilot',
                        'belowThreshold.central', 'negotiation',
                        'esco.features', 'aboveThresholdEU']
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
[14:22:20] Converted retries value: 10 -> Retry(total=10, connect=None, read=None, redirect=None, status=None)
[14:22:20] Converted retries value: 10 -> Retry(total=10, connect=None, read=None, redirect=None, status=None)
[14:22:20] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[14:22:20] Starting new HTTPS connection (1): lb-api-sandbox-2.prozorro.gov.ua:443
[14:22:20] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 1224273
[14:22:21] Response status code: 200

[14:22:21] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[14:22:21] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 1224273
[14:22:21] Response status code: 200

[14:22:21] Creating plan...

[14:22:21] Processing data file: plan_create.json

[14:22:21] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans
[14:22:22] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans HTTP/1.1" 201 4067
[14:22:22] Response status code: 201

[14:22:22] Plan created:
 - id 				9288bf10ab814221b0e3d6d1a424b465
 - token 			fde21ad67e284a0c9c6dc326f0453ee2
 - transfer 			089d8e13d4db459cb317728a1ee646f6

[14:22:22] Creating tender...

[14:22:22] Processing data file: tender_create.json

[14:22:22] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/9288bf10ab814221b0e3d6d1a424b465/tenders
[14:22:22] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans/9288bf10ab814221b0e3d6d1a424b465/tenders HTTP/1.1" 201 6771
[14:22:22] Response status code: 201

[14:22:22] Tender created:
 - id 				cc8d367af8f44d3cbd9897580e12d260
 - token 			53bc1780107943398dee504ffb36c43f
 - transfer 			4f21a53ec15b48e5b08d79d24fe59666
 - status 			draft
 - tenderID 			UA-2020-10-19-000169-b
 - tenderID 			UA-2020-10-19-000169-b
 - procurementMethodType 	closeFrameworkAgreementUA

[14:22:22] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/cc8d367af8f44d3cbd9897580e12d260
[14:22:22] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/tenders/cc8d367af8f44d3cbd9897580e12d260 HTTP/1.1" 200 6666
[14:22:22] Response status code: 200

[14:22:22] Create tender criteria...

[14:22:22] Processing data file: criteria_create.json

[14:22:22] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/cc8d367af8f44d3cbd9897580e12d260/criteria?acc_token=53bc1780107943398dee504ffb36c43f
[14:22:22] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/cc8d367af8f44d3cbd9897580e12d260/criteria?acc_token=53bc1780107943398dee504ffb36c43f HTTP/1.1" 201 50898
[14:22:22] Response status code: 201

[14:22:22] Tender criteria created:
 - classification.id 				CRITERION.EXCLUSION.CONVICTIONS.PARTICIPATION_IN_CRIMINAL_ORGANISATION
 - classification.id 				CRITERION.EXCLUSION.CONVICTIONS.FRAUD
 - classification.id 				CRITERION.EXCLUSION.CONVICTIONS.CORRUPTION
 - classification.id 				CRITERION.EXCLUSION.CONVICTIONS.CHILD_LABOUR-HUMAN_TRAFFICKING
 - classification.id 				CRITERION.EXCLUSION.CONTRIBUTIONS.PAYMENT_OF_TAXES
 - classification.id 				CRITERION.EXCLUSION.BUSINESS.BANKRUPTCY
 - classification.id 				CRITERION.EXCLUSION.MISCONDUCT.MARKET_DISTORTION
 - classification.id 				CRITERION.EXCLUSION.CONFLICT_OF_INTEREST.MISINTERPRETATION
 - classification.id 				CRITERION.EXCLUSION.NATIONAL.OTHER

[14:22:22] Patching tender...

[14:22:22] Processing data file: tender_patch.json

[14:22:22] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/cc8d367af8f44d3cbd9897580e12d260?acc_token=53bc1780107943398dee504ffb36c43f
[14:22:23] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/tenders/cc8d367af8f44d3cbd9897580e12d260?acc_token=53bc1780107943398dee504ffb36c43f HTTP/1.1" 200 57760
[14:22:23] Response status code: 200

[14:22:23] Tender status patched:
 - id 				cc8d367af8f44d3cbd9897580e12d260
 - status 			active.tendering

[14:22:23] Creating bids...

[14:22:23] Processing data file: bid_document.txt

[14:22:23] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[14:22:23] Starting new HTTPS connection (1): upload-docs-sandbox-2.prozorro.gov.ua:443
[14:22:23] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 592
[14:22:23] Response status code: 200

[14:22:23] Processing data file: bid_create_0.json

[14:22:23] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/cc8d367af8f44d3cbd9897580e12d260/bids
[14:22:23] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/cc8d367af8f44d3cbd9897580e12d260/bids HTTP/1.1" 201 1962
[14:22:23] Response status code: 201

[14:22:23] Bid created:
 - id 				38c0e317bd914a8fba52bcba1b707506
 - token 			d68101d7754b409f8467866dff1f5cab
 - status 			draft

[14:22:23] Processing data file: bid_document.txt

[14:22:23] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[14:22:23] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 572
[14:22:23] Response status code: 200

[14:22:23] Processing data file: bid_create_1.json

[14:22:23] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/cc8d367af8f44d3cbd9897580e12d260/bids
[14:22:23] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/cc8d367af8f44d3cbd9897580e12d260/bids HTTP/1.1" 201 2062
[14:22:23] Response status code: 201

[14:22:23] Bid created:
 - id 				7f6162a640cb4270b2cae721af6428c9
 - token 			8199007d2fe84d6d8aee6df5af18eb9e
 - status 			draft

[14:22:23] Processing data file: bid_document.txt

[14:22:23] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[14:22:24] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 586
[14:22:24] Response status code: 200

[14:22:24] Processing data file: bid_create_2.json

[14:22:24] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/cc8d367af8f44d3cbd9897580e12d260/bids
[14:22:24] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/cc8d367af8f44d3cbd9897580e12d260/bids HTTP/1.1" 201 2062
[14:22:24] Response status code: 201

[14:22:24] Bid created:
 - id 				35c88092ec404cb6a8b94cbf0a3fc8c7
 - token 			1eed661ae69046b69b8ed692494f48bb
 - status 			draft

[14:22:24] Processing data file: bid_document.txt

[14:22:24] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[14:22:24] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 590
[14:22:24] Response status code: 200

[14:22:24] Processing data file: bid_create_3.json

[14:22:24] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/cc8d367af8f44d3cbd9897580e12d260/bids
[14:22:24] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/cc8d367af8f44d3cbd9897580e12d260/bids HTTP/1.1" 201 2062
[14:22:24] Response status code: 201

[14:22:24] Bid created:
 - id 				1306c7e7abd84a3fb3deb132b6325e38
 - token 			615e66a4ab0f495080127c57429c1245
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
