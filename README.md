## Cloning repo

git clone git@github.com:aerohit/yogesh.git

## To download the data:

rsync -avz physionet.org::physiobank-core/database/gaitndd .

## To process data:

    mkdir output
    python process_data.py
