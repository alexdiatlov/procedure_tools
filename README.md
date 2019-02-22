# procedure_tools

## Usage
```
usage: procedure [-h] [-a 460800] [-p /api/0/] [-d aboveThresholdUA]
                 [-s tender_create.json]
                 host token

positional arguments:
  host                  api host
  token                 api token

optional arguments:
  -h, --help            show this help message and exit
  -a 460800, --acceleration 460800
                        acceleration multiplier
  -p /api/0/, --path /api/0/
                        api path
  -d aboveThresholdUA, --data aboveThresholdUA
                        data files path custom or one of ['aboveThresholdUA',
                        'closeFrameworkAgreementUA']
  -s tender_create.json, --stop tender_create.json
                        data file name to stop after
```

## Usage example

Create with default data
```
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/2.4/ --data=closeFrameworkAgreementUA
```

Create with default data and stop after specific data file
```
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/2.4/ --data=closeFrameworkAgreementUA
```

Create with custom data files (relative path)
```
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/2.4/ --data=customdata/closeFrameworkAgreementUA
```

Create with custom data files (absolute path)
```
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/2.4/ --data=/Users/JonhDoe/customdata/closeFrameworkAgreementUA
```

Create with custom data files (absolute path, Windows)
```
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/2.4/ --data=C:\Users\JonhDoe\customdata\closeFrameworkAgreementUA
```

## Output example
```
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/2.4/ --data=closeFrameworkAgreementUA --stop=bid_create_4.json
```
```
Creating tender...

Processing data file: tender_create.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/2.4/tenders

Tender created:
 - id 				11dd15e5561b494c86d5a7a77b291c04
 - token 			7996a71a845b443a9f7043cca222b71f
 - status 			active.tendering
 - tenderID 			UA-2019-02-22-000195-b
 - procurementMethodType 	closeFrameworkAgreementUA

Creating bids...

Processing data file: bid_create_0.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/2.4/tenders/11dd15e5561b494c86d5a7a77b291c04/bids

Bid created:
 - id 				19d350d07fd244eb9cfa8ad424ffe837
 - token 			fbeb77aff97f4714a9378d9d71a2e715
 - status 			pending

Processing data file: bid_create_1.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/2.4/tenders/11dd15e5561b494c86d5a7a77b291c04/bids

Bid created:
 - id 				dddd3f80ddc54958a260d0feda1c2b6b
 - token 			7743ceecd7f349628ecb05a91598bc54
 - status 			pending

Processing data file: bid_create_2.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/2.4/tenders/11dd15e5561b494c86d5a7a77b291c04/bids

Bid created:
 - id 				4f473c0707714b50acc9580708804b68
 - token 			b7a5ef754586418b9fa52686c01f768e
 - status 			pending

Processing data file: bid_create_3.json

[POST] https://lb-api-sandbox.prozorro.gov.ua/api/2.4/tenders/11dd15e5561b494c86d5a7a77b291c04/bids

Bid created:
 - id 				64948c26465b461caa8d9476027872b9
 - token 			ffea0e64f6224287a8490add0d548810
 - status 			pending

```
