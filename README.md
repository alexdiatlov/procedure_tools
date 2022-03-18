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
[00:07:07] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[00:07:07] Starting new HTTPS connection (1): lb-api-sandbox-2.prozorro.gov.ua:443
[00:07:08] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 832886
[00:07:08] Response status code: 200

[00:07:08] Client time delta with server: 0 seconds

[00:07:08] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[00:07:08] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/1.1" 200 832886
[00:07:09] Response status code: 200

[00:07:09] Client time delta with server: -1 seconds

[00:07:09] Creating plan...

[00:07:09] Processing data file: plan_create.json

[00:07:09] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans
[00:07:09] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans HTTP/1.1" 201 4186
[00:07:09] Response status code: 201

[00:07:09] Plan created:
 - id 				95d2eda359064f5e99513104b6a285a1
 - token 			f3f63e4c4a4a4a0db6fe0e8dfbec5880
 - transfer 			d666ecb5cda2479c88b6c77a5adbea82
 - status 			draft

[00:07:09] Patching plan...

[00:07:09] Processing data file: plan_patch.json

[00:07:09] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/95d2eda359064f5e99513104b6a285a1?acc_token=f3f63e4c4a4a4a0db6fe0e8dfbec5880
[00:07:09] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/plans/95d2eda359064f5e99513104b6a285a1?acc_token=f3f63e4c4a4a4a0db6fe0e8dfbec5880 HTTP/1.1" 200 4085
[00:07:09] Response status code: 200

[00:07:09] Plan patched:
 - id 				95d2eda359064f5e99513104b6a285a1
 - status 			scheduled

[00:07:09] Creating tender...

[00:07:09] Processing data file: tender_create.json

[00:07:09] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/95d2eda359064f5e99513104b6a285a1/tenders
[00:07:10] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans/95d2eda359064f5e99513104b6a285a1/tenders HTTP/1.1" 201 6429
[00:07:10] Response status code: 201

[00:07:10] Tender created:
 - id 				d4344c8cf0604530964e11a9410f46bc
 - token 			13b7d39b2eda426a92758efbc0a3e154
 - transfer 			bc88c706d5b941adb26ac4cb09ccc492
 - status 			draft
 - tenderID 			UA-2022-03-19-000002-a
 - procurementMethodType 	closeFrameworkAgreementUA

[00:07:10] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/d4344c8cf0604530964e11a9410f46bc
[00:07:10] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/tenders/d4344c8cf0604530964e11a9410f46bc HTTP/1.1" 200 6324
[00:07:10] Response status code: 200

[00:07:10] Create tender criteria...

[00:07:10] Processing data file: criteria_create.json

[00:07:10] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/d4344c8cf0604530964e11a9410f46bc/criteria?acc_token=13b7d39b2eda426a92758efbc0a3e154
[00:07:10] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/d4344c8cf0604530964e11a9410f46bc/criteria?acc_token=13b7d39b2eda426a92758efbc0a3e154 HTTP/1.1" 201 53725
[00:07:10] Response status code: 201

[00:07:10] Tender criteria created:
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

[00:07:10] Patching tender...

[00:07:10] Processing data file: tender_patch.json

[00:07:10] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/d4344c8cf0604530964e11a9410f46bc?acc_token=13b7d39b2eda426a92758efbc0a3e154
[00:07:11] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/tenders/d4344c8cf0604530964e11a9410f46bc?acc_token=13b7d39b2eda426a92758efbc0a3e154 HTTP/1.1" 200 60245
[00:07:11] Response status code: 200

[00:07:11] Tender patched:
 - id 				d4344c8cf0604530964e11a9410f46bc
 - status 			active.tendering

[00:07:11] Creating bids...

[00:07:11] Processing data file: bid_document.txt

[00:07:11] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[00:07:11] Starting new HTTPS connection (1): upload-docs-sandbox-2.prozorro.gov.ua:443
[00:07:11] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 580
[00:07:11] Response status code: 200

[00:07:11] Processing data file: bid_create_0.json

[00:07:11] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/d4344c8cf0604530964e11a9410f46bc/bids
[00:07:11] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/d4344c8cf0604530964e11a9410f46bc/bids HTTP/1.1" 201 1953
[00:07:11] Response status code: 201

[00:07:11] Bid created:
 - id 				78515755ad49448987d29faab5ec8d22
 - token 			7f2da7509af843c59c7f12ab65c99616
 - status 			draft

[00:07:11] Processing data file: bid_document.txt

[00:07:11] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[00:07:12] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 574
[00:07:12] Response status code: 200

[00:07:12] Processing data file: bid_create_1.json

[00:07:12] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/d4344c8cf0604530964e11a9410f46bc/bids
[00:07:12] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/d4344c8cf0604530964e11a9410f46bc/bids HTTP/1.1" 201 2052
[00:07:12] Response status code: 201

[00:07:12] Bid created:
 - id 				fdaa49709b884239ab11c00aaea4e889
 - token 			a2483e3b047c4376bc95b4770e3c8af0
 - status 			draft

[00:07:12] Processing data file: bid_document.txt

[00:07:12] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[00:07:12] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 580
[00:07:12] Response status code: 200

[00:07:12] Processing data file: bid_create_2.json

[00:07:12] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/d4344c8cf0604530964e11a9410f46bc/bids
[00:07:12] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/d4344c8cf0604530964e11a9410f46bc/bids HTTP/1.1" 201 2046
[00:07:12] Response status code: 201

[00:07:12] Bid created:
 - id 				ee39ef0d8a5c43bfaf7c56467eed4332
 - token 			64d469d9338f48bcbf185d4247dc16cf
 - status 			draft

[00:07:12] Processing data file: bid_document.txt

[00:07:12] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[00:07:12] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/1.1" 200 574
[00:07:12] Response status code: 200

[00:07:12] Processing data file: bid_create_3.json

[00:07:12] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/d4344c8cf0604530964e11a9410f46bc/bids
[00:07:12] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/d4344c8cf0604530964e11a9410f46bc/bids HTTP/1.1" 201 2052
[00:07:12] Response status code: 201

[00:07:12] Bid created:
 - id 				0f54f6451e854cb4a30996d730f88fba
 - token 			8d0c954cebcc40d8aa9b2ccdf8a26020
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
