#!/bin/sh

FILE='README.md'

cat > $FILE <<- EOM
# procedure_tools

## Install

Clone and install with pip
\`\`\`
cd procedure_tools

pip install -e .
\`\`\`

## Usage
\`\`\`
EOM

procedure -h >> $FILE

cat >> $FILE <<- EOM
\`\`\`

## Usage example

Create with default data
\`\`\`
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/0/ --data=closeFrameworkAgreementUA
\`\`\`

Create with default data and stop after specific data file
\`\`\`
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/0/ --data=closeFrameworkAgreementUA
\`\`\`

Create with custom data files (relative path)
\`\`\`
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/0/ --data=customdata/closeFrameworkAgreementUA
\`\`\`

Create with custom data files (absolute path)
\`\`\`
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/0/ --data=/Users/JonhDoe/customdata/closeFrameworkAgreementUA
\`\`\`

Create with custom data files (absolute path, Windows)
\`\`\`
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/0/ --data=C:\Users\JonhDoe\customdata\closeFrameworkAgreementUA
\`\`\`

## Output example
\`\`\`
procedure https://lb-api-sandbox.prozorro.gov.ua 59fcc88692e341a2a4a0c184db282e83 --acceleration=1000000 --path=/api/0/ --data=closeFrameworkAgreementUA --stop=bid_create_4.json
\`\`\`
\`\`\`
EOM

procedure https://lb-api-sandbox.prozorro.gov.ua ${1} --acceleration=1000000 --path=/api/0/ --data=closeFrameworkAgreementUA --stop=bid_create_3.json >> $FILE

cat >> $FILE <<- EOM
\`\`\`

## Update readme

Pass API token as parameter to README.sh
\`\`\`
./README.sh 59fcc88692e341a2a4a0c184db282e83
\`\`\`

## Run tests

\`\`\`
HOST=https://lb-api-sandbox.prozorro.gov.ua TOKEN=59fcc88692e341a2a4a0c184db282e83 py.test procedure_tools/test.py -s -v
\`\`\`
EOM
