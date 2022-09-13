
[![Logo3.png](https://i.postimg.cc/4d6RBfZn/Logo3.png)](https://postimg.cc/34xqwHkH)


# CrowdFeel

Real-time sentiments and emotions analysis through Twitter

CrowdFeel is web App which allows users to trak in real-time the emotions and sentiments of a certain target tweets. Users can search tweets by username (post by or mentioned), location of the tweets or by hashtag.


💻 Check it out : https://crowd-feel.herokuapp.com/


Front-end repository: https://github.com/Alvarodelamaza/crowdfeel-frontend


## Tech Stack
**ML and AI:** Tensorflow, Vertex AI, Google Bert model

**Backend:** FastAPI, Docker, Google Cloud Run, Heroku

**Frontend:** Streamlit


## Screenshots

[![Screen-Shot-2022-09-13-at-12-12-12.png](https://i.postimg.cc/TPJmrbSs/Screen-Shot-2022-09-13-at-12-12-12.png)](https://postimg.cc/7Cbf45q1)

[![Screen-Shot-2022-09-13-at-12-11-32.png](https://i.postimg.cc/VkB5T8Rr/Screen-Shot-2022-09-13-at-12-11-32.png)](https://postimg.cc/87c1JxxN)

[![Screen-Shot-2022-09-13-at-12-11-43.png](https://i.postimg.cc/Lsx593Gm/Screen-Shot-2022-09-13-at-12-11-43.png)](https://postimg.cc/7CTwX0xR)


## Authors

- [Angelo Darriet](https://github.com/AngieDar)
- [Alvaro de la Maza](https://github.com/Alvarodelamaza)
- [Tjebbe Lodeizen](https://github.com/tjebbel)

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
```
