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
Creating plan...

Processing data file: plan_create.json

[POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans

Plan created:
 - id 				03b12f79950f473cb595dd29045daf8e
 - token 			04f3aa6bf9034511a3c451e097c33d8a
 - transfer 			79bc92174b9f4677a6d13c2ee4cd329d

Creating tender...

Processing data file: tender_create.json

[POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/03b12f79950f473cb595dd29045daf8e/tenders

Tender created:
 - id 				6897cad4993d429fa01cabcd753e4c52
 - token 			f20f5e93798d4e4290805baa2e080881
 - transfer 			0eee417d283d4164aefa5b038e93b002
 - status 			draft
 - tenderID 			UA-2020-10-16-000077-a
 - procurementMethodType 	closeFrameworkAgreementUA

[GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/6897cad4993d429fa01cabcd753e4c52

Create tender criteria...

Processing data file: criteria_create.json

[POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/6897cad4993d429fa01cabcd753e4c52/criteria?acc_token=f20f5e93798d4e4290805baa2e080881

Tender criteria created:
 - classification.id 				CRITERION.EXCLUSION.CONVICTIONS.PARTICIPATION_IN_CRIMINAL_ORGANISATION
 - classification.id 				CRITERION.EXCLUSION.CONVICTIONS.FRAUD
 - classification.id 				CRITERION.EXCLUSION.CONVICTIONS.CORRUPTION
 - classification.id 				CRITERION.EXCLUSION.CONVICTIONS.CHILD_LABOUR-HUMAN_TRAFFICKING
 - classification.id 				CRITERION.EXCLUSION.CONTRIBUTIONS.PAYMENT_OF_TAXES
 - classification.id 				CRITERION.EXCLUSION.BUSINESS.BANKRUPTCY
 - classification.id 				CRITERION.EXCLUSION.MISCONDUCT.MARKET_DISTORTION
 - classification.id 				CRITERION.EXCLUSION.CONFLICT_OF_INTEREST.MISINTERPRETATION
 - classification.id 				CRITERION.EXCLUSION.NATIONAL.OTHER
Patching tender...

Processing data file: tender_patch.json

[PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/6897cad4993d429fa01cabcd753e4c52?acc_token=f20f5e93798d4e4290805baa2e080881

Tender status patched:
 - id 				6897cad4993d429fa01cabcd753e4c52
 - status 			active.tendering

Creating bids...

Processing data file: bid_document.txt

[POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload

Processing data file: bid_create_0.json

[POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/6897cad4993d429fa01cabcd753e4c52/bids

Bid created:
 - id 				1b04c717d2fa4c2d91e3952776bb8108
 - token 			2ee8ba342df64eefacd0d0d460343489
 - status 			draft

Processing data file: bid_document.txt

[POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload

Processing data file: bid_create_1.json

[POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/6897cad4993d429fa01cabcd753e4c52/bids

Bid created:
 - id 				467c57c4fde244a2aa1a858d9408469c
 - token 			5673ccd6dbf8499ca48396f68af66e00
 - status 			draft

Processing data file: bid_document.txt

[POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload

Processing data file: bid_create_2.json

[POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/6897cad4993d429fa01cabcd753e4c52/bids

Bid created:
 - id 				863b122332c542459efc5e55600d0498
 - token 			b79a17970a964aeea0ac9780ce75aad8
 - status 			draft

Processing data file: bid_document.txt

[POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload

Processing data file: bid_create_3.json

[POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/6897cad4993d429fa01cabcd753e4c52/bids

Bid created:
 - id 				5dec2bce595d4bc185de9e6d71c4fa99
 - token 			cc22348e0180497eab082e51853d2e7e
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
