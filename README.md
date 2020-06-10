# gitmaster-chatbot

![Git master Chatbox demo](https://s7.gifyu.com/images/gitmaster-chatbot.gif) 

## How to install
* Install Python.
* Install Node.Js (12+).
* Install dependencies in `requirements.txt`.
* Install Node.Js dependencies in `/chatbox` (yarn).

## Start
* Train the model: `./bin/train.py`.
* Start the Rasa actions server: `./bin/start-server.py`.
* Start the Rasa application in shell mode: `./bin:start-chatbot.py`.
* Start the Rasa application in "web" mode: `rasa run --credentials credentials.yml --cors "*"`
* Start the React Web application: `cd chatbox && npm start`