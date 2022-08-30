# Data analysis
- Document here the project: crowdfeel
- Description: Project Description
- Data Source:
- Type of analysis:

Please document the project the better you can.

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for crowdfeel in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/crowdfeel`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "crowdfeel"
git remote add origin git@github.com:{group}/crowdfeel.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
crowdfeel-run
```

# Install

Go to `https://github.com/{group}/crowdfeel` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/crowdfeel.git
cd crowdfeel
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
crowdfeel-run
```

```GCP
check current setup: gcloud info
initiate new gcloud project: gcloud init
check bucket: gsutil ls
download csv (go to raw_data folder and run the following):
gsutil -m cp \
  "gs://crowdfeel_bucket/X_test_1600k.csv" \
  "gs://crowdfeel_bucket/X_test_160k.csv" \
  "gs://crowdfeel_bucket/X_test_16k.csv" \
  "gs://crowdfeel_bucket/X_test_400k.csv" \
  "gs://crowdfeel_bucket/X_test_48k.csv" \
  "gs://crowdfeel_bucket/X_test_800k.csv" \
  "gs://crowdfeel_bucket/X_train_1600k.csv" \
  "gs://crowdfeel_bucket/X_train_160k.csv" \
  "gs://crowdfeel_bucket/X_train_16k.csv" \
  "gs://crowdfeel_bucket/X_train_400k.csv" \
  "gs://crowdfeel_bucket/X_train_48k.csv" \
  "gs://crowdfeel_bucket/X_train_800k.csv" \
  "gs://crowdfeel_bucket/training_data.csv" \
  "gs://crowdfeel_bucket/y_test_1600k.csv" \
  "gs://crowdfeel_bucket/y_test_160k.csv" \
  "gs://crowdfeel_bucket/y_test_16k.csv" \
  "gs://crowdfeel_bucket/y_test_400k.csv" \
  "gs://crowdfeel_bucket/y_test_48k.csv" \
  "gs://crowdfeel_bucket/y_test_800k.csv" \
  "gs://crowdfeel_bucket/y_train_1600k.csv" \
  "gs://crowdfeel_bucket/y_train_160k.csv" \
  "gs://crowdfeel_bucket/y_train_16k.csv" \
  "gs://crowdfeel_bucket/y_train_400k.csv" \
  "gs://crowdfeel_bucket/y_train_48k.csv" \
  "gs://crowdfeel_bucket/y_train_800k.csv" \
  .
```
