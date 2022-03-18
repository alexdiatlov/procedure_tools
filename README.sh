#!/bin/sh

echo "Readme generation started."

FILE='README.md'

FAKE_API_TOKEN='broker_api_token'
FAKE_DS_USERNAME='broker_ds_username'
FAKE_DS_PASSWORD='broker_ds_password'

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

echo "Executing command help."

procedure -h >> $FILE

echo "Command help successfully generated."

cat >> $FILE <<- EOM
\`\`\`

## Usage example

Create with default data
\`\`\`
procedure ${API_HOST} ${FAKE_API_TOKEN} ${DS_HOST} ${FAKE_DS_USERNAME} ${FAKE_DS_PASSWORD} --acceleration=1000000 --path=/api/0/ --data=closeFrameworkAgreementUA
\`\`\`

Create with default data and stop after specific data file
\`\`\`
procedure ${API_HOST} ${FAKE_API_TOKEN} ${DS_HOST} ${FAKE_DS_USERNAME} ${FAKE_DS_PASSWORD} --acceleration=1000000 --path=/api/0/ --data=closeFrameworkAgreementUA --stop=bid_create_3.json
\`\`\`

Create with custom data files (relative path)
\`\`\`
procedure ${API_HOST} ${FAKE_API_TOKEN} ${DS_HOST} ${FAKE_DS_USERNAME} ${FAKE_DS_PASSWORD} --acceleration=1000000 --path=/api/0/ --data=customdata/closeFrameworkAgreementUA
\`\`\`

Create with custom data files (absolute path)
\`\`\`
procedure ${API_HOST} ${FAKE_API_TOKEN} ${DS_HOST} ${FAKE_DS_USERNAME} ${FAKE_DS_PASSWORD} --acceleration=1000000 --path=/api/0/ --data=/Users/JonhDoe/customdata/closeFrameworkAgreementUA
\`\`\`

Create with custom data files (absolute path, Windows)
\`\`\`
procedure ${API_HOST} ${FAKE_API_TOKEN} ${DS_HOST} ${FAKE_DS_USERNAME} ${FAKE_DS_PASSWORD} --acceleration=1000000 --path=/api/0/ --data=C:\Users\JonhDoe\customdata\closeFrameworkAgreementUA
\`\`\`

## Output example
\`\`\`
procedure ${API_HOST} ${FAKE_API_TOKEN} ${DS_HOST} ${FAKE_DS_USERNAME} ${FAKE_DS_PASSWORD} --acceleration=1000000 --path=/api/0/ --data=closeFrameworkAgreementUA --stop=bid_create_4.json
\`\`\`
\`\`\`
EOM

echo "Executing command example."

procedure ${API_HOST} ${API_TOKEN} ${DS_HOST} ${DS_USERNAME} ${DS_PASSWORD} --acceleration=1000000 --path=/api/0/ --data=closeFrameworkAgreementUA --stop=bid_create_3.json >> $FILE

echo "Command example successfully generated."

cat >> $FILE <<- EOM
\`\`\`

## Update readme

\`\`\`
export API_HOST=${API_HOST}
export API_TOKEN=${FAKE_API_TOKEN}
export DS_HOST=${DS_HOST}
export DS_USERNAME=${FAKE_DS_USERNAME}
export DS_PASSWORD=${FAKE_DS_PASSWORD}

./README.sh
\`\`\`
or
\`\`\`
API_HOST=${API_HOST} API_TOKEN=${FAKE_API_TOKEN} DS_HOST=${DS_HOST} DS_USERNAME=${FAKE_DS_USERNAME} DS_PASSWORD=${FAKE_DS_PASSWORD} ./README.sh
\`\`\`

## Run tests

\`\`\`
export API_HOST=${API_HOST}
export API_TOKEN=${FAKE_API_TOKEN}
export DS_HOST=${DS_HOST}
export DS_USERNAME=${FAKE_DS_USERNAME}
export DS_PASSWORD=${FAKE_DS_PASSWORD}

python setup.py test
\`\`\`
or
\`\`\`
API_HOST=${API_HOST} API_TOKEN=${FAKE_API_TOKEN} DS_HOST=${DS_HOST} DS_USERNAME=${FAKE_DS_USERNAME} DS_PASSWORD=${FAKE_DS_PASSWORD} python setup.py test
\`\`\`
EOM

echo "Readme successfully generated."
