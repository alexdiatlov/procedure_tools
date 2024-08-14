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
                 [-m quick(mode:no-auction)] [-s tender_create.json]
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
                         - reorder.py
                         - reporting
                         - simple.defense

  -m quick(mode:no-auction), --submission quick(mode:no-auction)
                        value for submissionMethodDetails, one of:
                         - quick
                         - quick(mode:no-auction)
                         - quick(mode:fast-auction)
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
[12:22:32] Using seed 661011

[12:22:32] Initializing tenders client

[12:22:32] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[12:22:32] Starting new HTTPS connection (1): lb-api-sandbox-2.prozorro.gov.ua:443
[12:22:32] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/11" 200 887419
[12:22:33] Response status code: 200

[12:22:33] Client time delta with server: -1937 milliseconds

[12:22:33] Initializing ds client

[12:22:33] Creating plan...

[12:22:33] Processing data file: plan_create.json

[12:22:33] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans
[12:22:34] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans HTTP/11" 201 4202
[12:22:34] Response status code: 201

[12:22:34] Plan created:
 - id 				b39bacb963b0446fb3fac49977fde22a
 - token 			9e119a752c184f4cbf5be74ad2518fca
 - transfer 			5e26ffb531cc4225973a748bd22f9230
 - status 			draft

[12:22:34] Patching plan...

[12:22:34] Processing data file: plan_patch.json

[12:22:34] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/b39bacb963b0446fb3fac49977fde22a?acc_token=9e119a752c184f4cbf5be74ad2518fca
[12:22:34] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/plans/b39bacb963b0446fb3fac49977fde22a?acc_token=9e119a752c184f4cbf5be74ad2518fca HTTP/11" 200 4101
[12:22:34] Response status code: 200

[12:22:34] Plan patched:
 - id 				b39bacb963b0446fb3fac49977fde22a
 - status 			scheduled

[12:22:34] Creating tender...

[12:22:34] Processing data file: tender_create.json

[12:22:34] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/b39bacb963b0446fb3fac49977fde22a/tenders
[12:22:34] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans/b39bacb963b0446fb3fac49977fde22a/tenders HTTP/11" 201 7169
[12:22:34] Response status code: 201

[12:22:34] Tender created:
 - id 				11325b8b6d8e4a45ae179fef7fd63aa9
 - token 			f606cab74ded47d6aab5ef2cc11cf975
 - transfer 			39e38047e71c43d8bccbf01654dbfda7
 - status 			draft
 - tenderID 			UA-2024-08-14-000011-a
 - procurementMethodType 	closeFrameworkAgreementUA

[12:22:34] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/11325b8b6d8e4a45ae179fef7fd63aa9
[12:22:34] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/tenders/11325b8b6d8e4a45ae179fef7fd63aa9 HTTP/11" 200 7064
[12:22:34] Response status code: 200

[12:22:34] Processing data file: tender_document_attach.json

[12:22:34] Processing data file: tender_document_file.txt

[12:22:34] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:22:34] Starting new HTTPS connection (1): upload-docs-sandbox-2.prozorro.gov.ua:443
[12:22:35] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/11" 200 584
[12:22:35] Response status code: 200

[12:22:35] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/11325b8b6d8e4a45ae179fef7fd63aa9/documents?acc_token=f606cab74ded47d6aab5ef2cc11cf975
[12:22:35] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/11325b8b6d8e4a45ae179fef7fd63aa9/documents?acc_token=f606cab74ded47d6aab5ef2cc11cf975 HTTP/11" 201 555
[12:22:35] Response status code: 201

[12:22:35] Document attached:
 - id 				471786dd8061493b8fb286d647c913f3
 - url 				https://public-docs-sandbox-2.prozorro.gov.ua/get/1cd151b64da54751a0de5a3ceef2adc6?Signature=AKAMrq629XC5V5z2ULAprUzIrC6%2FIjuy%2BJ0f5jrgRPlX5lIv8oHClQYKo%2Fs7jSHe6DYrgQ5Wz9xQFOwbTc%2B%2FBQ%3D%3D&KeyID=1331dc52

[12:22:35] Create tender criteria...

[12:22:35] Processing data file: criteria_create.json

[12:22:35] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/11325b8b6d8e4a45ae179fef7fd63aa9/criteria?acc_token=f606cab74ded47d6aab5ef2cc11cf975
[12:22:35] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/11325b8b6d8e4a45ae179fef7fd63aa9/criteria?acc_token=f606cab74ded47d6aab5ef2cc11cf975 HTTP/11" 201 53697
[12:22:35] Response status code: 201

[12:22:35] Tender criteria created:
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

[12:22:35] Processing data file: tender_notice_attach.json

[12:22:35] Processing data file: tender_notice_file.p7s

[12:22:35] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:22:36] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/11" 200 590
[12:22:36] Response status code: 200

[12:22:36] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/11325b8b6d8e4a45ae179fef7fd63aa9/documents?acc_token=f606cab74ded47d6aab5ef2cc11cf975
[12:22:36] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/11325b8b6d8e4a45ae179fef7fd63aa9/documents?acc_token=f606cab74ded47d6aab5ef2cc11cf975 HTTP/11" 201 575
[12:22:36] Response status code: 201

[12:22:36] Document attached:
 - id 				010530c74b054c339d79ef8ac6c9662e
 - url 				https://public-docs-sandbox-2.prozorro.gov.ua/get/772632aab56047d2832924e891723ac3?Signature=SAmD69JXYid2eNbB7smQBZPBaeqjksJgvBkCf4kzt8qePfT%2FWV6BFx8A7k2Hmw4%2FlotCsZko1%2BcUNsXziotWCA%3D%3D&KeyID=1331dc52
 - documentType 		notice

[12:22:36] Patching tender...

[12:22:36] Processing data file: tender_patch.json

[12:22:36] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/11325b8b6d8e4a45ae179fef7fd63aa9?acc_token=f606cab74ded47d6aab5ef2cc11cf975
[12:22:36] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/tenders/11325b8b6d8e4a45ae179fef7fd63aa9?acc_token=f606cab74ded47d6aab5ef2cc11cf975 HTTP/11" 200 61943
[12:22:36] Response status code: 200

[12:22:36] Tender patched:
 - id 				11325b8b6d8e4a45ae179fef7fd63aa9
 - status 			active.tendering

[12:22:36] Skipping complaints creating: bot and reviewer tokens are required

[12:22:36] Creating bids...

[12:22:36] Processing data file: bid_document_file.txt

[12:22:36] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:22:36] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/11" 200 579
[12:22:36] Response status code: 200

[12:22:36] Processing data file: bid_confidential_document_file.txt

[12:22:36] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:22:36] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/11" 200 594
[12:22:36] Response status code: 200

[12:22:36] Processing data file: bid_eligibility_document_file.txt

[12:22:36] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:22:37] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/11" 200 589
[12:22:37] Response status code: 200

[12:22:37] Processing data file: bid_financial_document_file.txt

[12:22:37] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:22:37] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/11" 200 591
[12:22:37] Response status code: 200

[12:22:37] Processing data file: bid_qualification_document_file.txt

[12:22:37] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[12:22:37] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/11" 200 595
[12:22:37] Response status code: 200

[12:22:37] Processing data file: bid_create_0.json

[12:22:37] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/11325b8b6d8e4a45ae179fef7fd63aa9/bids
[12:22:37] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/11325b8b6d8e4a45ae179fef7fd63aa9/bids HTTP/11" 403 217
[12:22:37] Response status code: 403

[12:22:37] Response text:

[12:22:37] {"status": "error", "errors": [{"location": "body", "name": "data", "description": "Bid can be added only during the tendering period: from (2024-08-14T12:22:32.731843+03:00) to (2024-08-14T12:22:35.323960+03:00)."}]}

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
