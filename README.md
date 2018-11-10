# Uncle Mong API Server

## Description
Uncle Mong is a chatbot based on the concept of brand mascots. It is created as a proof-of-concept implementation, created and hosted off Google Dialogflow. This git repo contains code to host the API server to handle requests that were more specific to Hai Sia, e.g. fish info, etc.

## Prerequisites
- Server running Python 3.7.1 (tested with this)
- Flask microframework

## Installation Steps

Install dependencies
```sh
sudo apt update && sudo apt -y upgrade
sudo apt install git
```

Clone repo
```sh
git clone https://gitea.zhengyuan.me/hai-sia/uncle-mong-api.git
```

Install virtualenv
```sh
sudo pip3 install virtualenv
```

Create virtualenv
```sh
cd uncle-mong-api
virtualenv venv
```

Activate the environment
```sh
. venv/bin/activate
```

Install Flask
```sh
pip install flask
```

Run API Server
```sh
flask run
```