$ conda create -n rasa3 python=3.8
$ conda activate rasa3
$ pip install pip==20.2
[needs Microsoft Build Tool installed]

$ pip install rasa==2.8.1
$ pip install rasa-sdk==2.8.1
$ rasa init [to create a new project]

$ pip install SQLAlchemy==1.3.22
$ pip install SQLAlchemy==1.3.22
$ conda install ujson (y when prompt)
$ conda install tensorflow (y when prompt)
$ pip install rasa-x==0.39.3 --extra-index-url https://pypi.rasa.com/simple

$ rasa --version
[rasa 2.8.1 with Python virtual environment 3.8 has been installed]

---------------------------------------------------------------------------------------------
[For Running on WhatsApp relevent commands]
$ rasa run -m models --enable-api --cors "*"
$ ngrok http 5005


$ rasa run --log-file out.log --cors * --enable-api

--------------------------------------------------------------------------------------------
For voice chatbot Libraries

For Automatic Speech Recognition (ASR) | Speech To Text (STT)
$ pip install SpeechRecognition PyAudio

For Text to Speech (TTS)
$ pip install gtts
[For Windows]
$ pip install mpyg321
[For Ubuntu]
$ sudo apt-get install mpg321


For Running Endpoint:
$ rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml 

--------------------------------------------------------------------------------------------------------------------------
                                                My Notes Related to Project
Overall Info:
- Total Number of Stories: 40
- Total Number of Success Stories: 17
- Total Number of Killed Stories: 23

Covered portion:
- Total Stories: 8
- Sucess Stories: 2
- Killed Stories: 6