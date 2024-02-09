# Eric's Moderation API
Model created with Open AI's Moderation datasets

## Install
```sh
git clone ericpandev/Moderation && cd Moderation
python -m pip install -r requirements.txt
```

## Running the Server
```sh
python server.py
```

# API
`POST` http://127.0.0.1:9235/run<br>
Sample Request:
```json
{
    "text": "sample text goes here"
}
```

Sample Response:
```json
{
    "harassment":0.0,
    "hate":0.0,
    "hate/threatening":0.0,
    "self-harm":0.02,
    "sexual":0.0,
    "sexual/minors":0.0,
    "violence":0.01,
    "violence/graphic":0.01
}
```