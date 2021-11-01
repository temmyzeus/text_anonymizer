# Text Anonymizer

A webapp and API that anonymizes naming entities in text.

The API can anonymize in 2 ways:

1. Change all named entitied to X's

   This can be used in the API by sending a POST request to

   http://ec2-3-235-197-114.compute-1.amazonaws.com:8000/x_anonymize

![X Anonymization](./images/x_anonymize_screen.png)

2. Return text and positions of all naming entities

   This can be used in the API by sending a POST request to

   http://ec2-3-235-197-114.compute-1.amazonaws.com:8000/entity_positions

![Entities Position](./images/get_pos_screen.png)



### Send Post Request to API using Python
```python
import requests
send_json = {
    'name': 'Input Text',
    'text': 'Your Text Here'
}
x_anonymize_api = 'http://ec2-3-235-197-114.compute-1.amazonaws.com:8000/x_anonymize'
get_entity_positions_api = 'http://ec2-3-235-197-114.compute-1.amazonaws.com:8000/entity_positions'
response = requests.post(x_anonymize_api, json=send_json)
print(reponse.text)
```

## Setup & Run on Local Machine with Docker Compose

1. Make sure docker and docker-compose are both installed, Check how to from official documentation

   https://docs.docker.com/engine/install/

   https://docs.docker.com/compose/install/

2. CD to directory

3. Run docker-compose.yml file or  docker-compose.prod.yml file. The difference is the former reflects changes made since docker volume mapping is used in it while the latter doesn't reflect changes unless docker images is rebuilt.



## Setup & Run on Local Machine with Docker

#### First, we create a network so both containers and communicate

```bash
sudo docker network create --driver bridge <your-network-name>
```

### API

To setup API Image

```bash
sudo docker build -t text_anonymizer:api -f ./app/Dockerfile.api .
```

To create and run API Container

```bash
sudo docker run -d --name api -p 8000:8000 text_anonymizer:api --network <your-network-name>
```

### WebApp

To start up docker web app image

```bash
sudo docker build -t text_anonymizer:app -f ./app/Dockerfile.webapp .
```

To create and run web app container

```bash
sudo docker run -d --name app -p 80:8501 text_anonymizer:app --network <your-network-name>
```