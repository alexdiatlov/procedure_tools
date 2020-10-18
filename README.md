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
[23:05:37] Creating plan...

[23:05:37] Processing data file: plan_create.json

[23:05:38] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans

[23:05:38] Plan created:
 - id 				b471fb7239ca4e6cb7bc8b91605540c7
 - token 			0739c98953a3436e906f5e414934ffe5
 - transfer 			c1f40e10d38747e78b84a90c50b62bb1

[23:05:38] Creating tender...

[23:05:38] Processing data file: tender_create.json

[23:05:38] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/b471fb7239ca4e6cb7bc8b91605540c7/tenders

[23:05:38] Tender created:
 - id 				ccda8b7a55a84e11a28559db9591eecb
 - token 			304afaca2f154731892c89b9d6f0b6ef
 - transfer 			9520be3b741c46c594edc225335bc3bd
 - status 			draft
 - tenderID 			UA-2020-10-18-000250-a
 - tenderID 			UA-2020-10-18-000250-a
 - procurementMethodType 	closeFrameworkAgreementUA

[23:05:38] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/ccda8b7a55a84e11a28559db9591eecb

[23:05:38] Create tender criteria...

[23:05:38] Processing data file: criteria_create.json

[23:05:38] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/ccda8b7a55a84e11a28559db9591eecb/criteria?acc_token=304afaca2f154731892c89b9d6f0b6ef

[23:05:38] Tender criteria created:
 - classification.id 				CRITERION.EXCLUSION.CONVICTIONS.PARTICIPATION_IN_CRIMINAL_ORGANISATION
 - classification.id 				CRITERION.EXCLUSION.CONVICTIONS.FRAUD
 - classification.id 				CRITERION.EXCLUSION.CONVICTIONS.CORRUPTION
 - classification.id 				CRITERION.EXCLUSION.CONVICTIONS.CHILD_LABOUR-HUMAN_TRAFFICKING
 - classification.id 				CRITERION.EXCLUSION.CONTRIBUTIONS.PAYMENT_OF_TAXES
 - classification.id 				CRITERION.EXCLUSION.BUSINESS.BANKRUPTCY
 - classification.id 				CRITERION.EXCLUSION.MISCONDUCT.MARKET_DISTORTION
 - classification.id 				CRITERION.EXCLUSION.CONFLICT_OF_INTEREST.MISINTERPRETATION
 - classification.id 				CRITERION.EXCLUSION.NATIONAL.OTHER

[23:05:38] Patching tender...

[23:05:38] Processing data file: tender_patch.json

[23:05:38] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/ccda8b7a55a84e11a28559db9591eecb?acc_token=304afaca2f154731892c89b9d6f0b6ef

[23:05:38] Tender status patched:
 - id 				ccda8b7a55a84e11a28559db9591eecb
 - status 			active.tendering

[23:05:38] Creating bids...

[23:05:38] Processing data file: bid_document.txt

[23:05:39] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload

[23:05:39] Processing data file: bid_create_0.json

[23:05:39] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/ccda8b7a55a84e11a28559db9591eecb/bids

[23:05:39] Bid created:
 - id 				f121b9e0e93f4e48954a28b052bdb1c9
 - token 			d35999d7b2284b7aa7572afbb110af18
 - status 			draft

[23:05:39] Processing data file: bid_document.txt

[23:05:39] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload

[23:05:39] Processing data file: bid_create_1.json

[23:05:40] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/ccda8b7a55a84e11a28559db9591eecb/bids

[23:05:40] Bid created:
 - id 				f5a707c273564261891bb187183aaa06
 - token 			12096346ae0e4d669f4408ba0ae7df2c
 - status 			draft

[23:05:40] Processing data file: bid_document.txt

[23:05:40] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload

[23:05:40] Processing data file: bid_create_2.json

[23:05:40] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/ccda8b7a55a84e11a28559db9591eecb/bids

[23:05:40] Bid created:
 - id 				124ced0902674128a5b9b6c142bc503d
 - token 			dbd9992379f443cf962164d0314d5fec
 - status 			draft

[23:05:40] Processing data file: bid_document.txt

[23:05:40] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload

[23:05:40] Processing data file: bid_create_3.json

[23:05:40] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/ccda8b7a55a84e11a28559db9591eecb/bids

[23:05:40] Bid created:
 - id 				64a68a08dd0c4c87a34ddb1291ffd6be
 - token 			8b39a443341a4ba593c547eee40c10fe
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
