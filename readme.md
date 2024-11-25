# Eric's Moderation API
> Everything here was tested on Python 3.9.6, however it should work with older and newer versions.

Model trained on Open AI's Moderation datasets (https://github.com/openai/moderation-api-release)

## Why does this exist?
1. Runs faster hosted locally than OpenAI's endpoint
2. Does not send data to OpenAI
3. Moderation dataset and models are not changing unlike OpenAI's, so constant tuning is not needed.
4. Using OpenAI's Moderation endpoint without using their services technically breaks their usage policies.
5. More reliable!! If OpenAI goes down, this does not as it is separate from openai!!

## What's Included?
- Pretrained Model
- Dataset used (Dataset from OpenAI)
- Pretrained Vectorizer
- `train.py` to modify how the model is trained
- An API to easily integrate into your applications
- `test.py` to check if the moderation model is working and view sample results
- `demobot.py` A demonstration of the API through a Discord Bot

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
The floats range from 0-1, being how confident the Model is that the text matches the label. In your application, you should find 2 ranges, one for automatic action and one to silently log for a human moderator to review. 

Recommended values you should use for your applications:
```
# For Automatic Action
"harassment":2, # Disabled
"hate":0.67,
"hate/threatening":0.67,
"self-harm":0.75,
"sexual":0.68,
"sexual/minors":0.68,
"violence":2, # Disabled
"violence/graphic":2 # Disabled

# To silently log to moderation channel
"harassment":0.45,
"hate":0.30,
"hate/threatening":0.37,
"self-harm":0.37,
"sexual":0.37,
"sexual/minors":0.35,
"violence":0.37,
"violence/graphic":0.37
```

Sample CURL Request
```sh
curl -X POST -H "Content-Type: application/json" -d '{"text": "sample text goes here"}' http://127.0.0.1:9235/run
```
