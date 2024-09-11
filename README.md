# procedure_tools

## Install

1. Clone

    ```
    git clone https://github.com/ProzorroUKR/procedure_tools.git
    ```

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

## Update

1. Pull

    ```
    git pull
    ```

    In case of conflicts:

    * Undo changes in project folder or reset with command

        ```
        git reset --hard
        ```

    * Pull again

        ```
        git pull
        ```

    * If this did not help, clean project folder

        ```
        git clean -fd
        ```

    * Pull again

        ```
        git pull
        ```

2. Install

    ```
    pip install -e .
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
[11:30:32] Using seed 29142

[11:30:32] Initializing tenders client

[11:30:32] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/spore
[11:30:32] Starting new HTTPS connection (1): lb-api-sandbox-2.prozorro.gov.ua:443
[11:30:32] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/spore HTTP/11" 200 882086
[11:30:32] Response status code: 200

[11:30:32] Client time delta with server: -960 milliseconds

[11:30:32] Initializing ds client

[11:30:32] Creating plan...

[11:30:32] Processing data file: plan_create.json

[11:30:32] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans
[11:30:33] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans HTTP/11" 201 4202
[11:30:33] Response status code: 201

[11:30:33] Plan created:
 - id 				ba02034695c04b31911c8ab217431025
 - token 			65b5492def0649cc90eec46984e9cfe2
 - transfer 			c2b92d51c9214fe0a9f17a5ac3ab97f7
 - status 			draft

[11:30:33] Patching plan...

[11:30:33] Processing data file: plan_patch.json

[11:30:33] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/ba02034695c04b31911c8ab217431025?acc_token=65b5492def0649cc90eec46984e9cfe2
[11:30:33] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/plans/ba02034695c04b31911c8ab217431025?acc_token=65b5492def0649cc90eec46984e9cfe2 HTTP/11" 200 4101
[11:30:33] Response status code: 200

[11:30:33] Plan patched:
 - id 				ba02034695c04b31911c8ab217431025
 - status 			scheduled

[11:30:33] Creating tender...

[11:30:33] Processing data file: tender_create.json

[11:30:33] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/plans/ba02034695c04b31911c8ab217431025/tenders
[11:30:33] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/plans/ba02034695c04b31911c8ab217431025/tenders HTTP/11" 201 7427
[11:30:33] Response status code: 201

[11:30:33] Tender created:
 - id 				c0860f1d60d84a68aa99c16281835122
 - token 			8f1aeb99e2594962b89c959496685508
 - transfer 			813a17cc81cc4f4a88e4b9b1de6816d7
 - status 			draft
 - tenderID 			UA-2024-09-11-000228-a
 - procurementMethodType 	closeFrameworkAgreementUA

[11:30:33] [GET] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/c0860f1d60d84a68aa99c16281835122
[11:30:33] https://lb-api-sandbox-2.prozorro.gov.ua:443 "GET /api/0/tenders/c0860f1d60d84a68aa99c16281835122 HTTP/11" 200 7322
[11:30:33] Response status code: 200

[11:30:33] Processing data file: tender_document_attach.json

[11:30:33] Processing data file: tender_document_file.txt

[11:30:33] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[11:30:33] Starting new HTTPS connection (1): upload-docs-sandbox-2.prozorro.gov.ua:443
[11:30:33] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/11" 200 592
[11:30:33] Response status code: 200

[11:30:33] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/c0860f1d60d84a68aa99c16281835122/documents?acc_token=8f1aeb99e2594962b89c959496685508
[11:30:34] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/c0860f1d60d84a68aa99c16281835122/documents?acc_token=8f1aeb99e2594962b89c959496685508 HTTP/11" 201 549
[11:30:34] Response status code: 201

[11:30:34] Document attached:
 - id 				77741d5642ce4adf817b1b208c725c46
 - url 				https://public-docs-sandbox-2.prozorro.gov.ua/get/8829f12e179a4ed98df3124c29a4635a?Signature=cV22xdWtfJRGXYa8d2EYyd9fqYGYm9n%2BE0ebPK6TrXHi%2Bfkrdl549DKlHfZADg8QncT5wAXnKh2H4PKhMSPTCw%3D%3D&KeyID=1331dc52

[11:30:34] Create tender criteria...

[11:30:34] Processing data file: criteria_create.json

[11:30:34] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/c0860f1d60d84a68aa99c16281835122/criteria?acc_token=8f1aeb99e2594962b89c959496685508
[11:30:34] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/c0860f1d60d84a68aa99c16281835122/criteria?acc_token=8f1aeb99e2594962b89c959496685508 HTTP/11" 201 53697
[11:30:34] Response status code: 201

[11:30:34] Tender criteria created:
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

[11:30:34] Processing data file: tender_notice_attach.json

[11:30:34] Processing data file: tender_notice_file.p7s

[11:30:34] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[11:30:34] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/11" 200 576
[11:30:34] Response status code: 200

[11:30:34] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/c0860f1d60d84a68aa99c16281835122/documents?acc_token=8f1aeb99e2594962b89c959496685508
[11:30:34] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/c0860f1d60d84a68aa99c16281835122/documents?acc_token=8f1aeb99e2594962b89c959496685508 HTTP/11" 201 571
[11:30:34] Response status code: 201

[11:30:34] Document attached:
 - id 				ee7fb70d9e364e3b913a30690e1614f6
 - url 				https://public-docs-sandbox-2.prozorro.gov.ua/get/46b4d4a6b4cd4b5f86bced67ef6e770c?Signature=tbDxevxhhlxrWTUplcSyAlaP3p20mD6i7F5touEGIIlf2PT4o3q3GSXwlfJFZdaBTXyFQgfpjcfTET%2FKlxTaDA%3D%3D&KeyID=1331dc52
 - documentType 		notice

[11:30:34] Patching tender...

[11:30:34] Processing data file: tender_patch.json

[11:30:34] [PATCH] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/c0860f1d60d84a68aa99c16281835122?acc_token=8f1aeb99e2594962b89c959496685508
[11:30:34] https://lb-api-sandbox-2.prozorro.gov.ua:443 "PATCH /api/0/tenders/c0860f1d60d84a68aa99c16281835122?acc_token=8f1aeb99e2594962b89c959496685508 HTTP/11" 200 62201
[11:30:34] Response status code: 200

[11:30:34] Tender patched:
 - id 				c0860f1d60d84a68aa99c16281835122
 - status 			active.tendering

[11:30:34] Skipping complaints creating: bot and reviewer tokens are required

[11:30:34] Creating bids...

[11:30:34] Processing data file: bid_create_0.json

[11:30:34] Processing data file: bid_document_file.txt

[11:30:34] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[11:30:34] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/11" 200 575
[11:30:34] Response status code: 200

[11:30:34] Processing data file: bid_confidential_document_file.txt

[11:30:34] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[11:30:34] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/11" 200 614
[11:30:34] Response status code: 200

[11:30:34] Processing data file: bid_eligibility_document_file.txt

[11:30:34] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[11:30:35] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/11" 200 587
[11:30:35] Response status code: 200

[11:30:35] Processing data file: bid_financial_document_file.txt

[11:30:35] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[11:30:35] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/11" 200 601
[11:30:35] Response status code: 200

[11:30:35] Processing data file: bid_qualification_document_file.txt

[11:30:35] [POST] https://upload-docs-sandbox-2.prozorro.gov.ua/upload
[11:30:35] https://upload-docs-sandbox-2.prozorro.gov.ua:443 "POST /upload HTTP/11" 200 613
[11:30:35] Response status code: 200

[11:30:35] [POST] https://lb-api-sandbox-2.prozorro.gov.ua/api/0/tenders/c0860f1d60d84a68aa99c16281835122/bids
[11:30:35] https://lb-api-sandbox-2.prozorro.gov.ua:443 "POST /api/0/tenders/c0860f1d60d84a68aa99c16281835122/bids HTTP/11" 403 217
[11:30:35] Response status code: 403

[11:30:35] Response text:

[11:30:35] {"status": "error", "errors": [{"location": "body", "name": "data", "description": "Bid can be added only during the tendering period: from (2024-09-11T11:30:32.279576+03:00) to (2024-09-11T11:30:34.871619+03:00)."}]}

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
