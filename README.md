# Text_anonymizer

A webapp and API that anonymize named entities in text

The API can anonymize in 2 ways:

1. Change all named entitied to X's

    This can be used in the API by sending a POST request to

    https://localhost:PORT/get_anonymized/

![X Anonymization](./images/x_anonymize_screen.png)

2. Return text and positions of all named entities

    This can be used in the API by sending a POST request to

    https://localhost:PORT/get_pos/

![Entities Position](./images/get_pos_screen.png)





#### First, we create a network so both containers and communicate

```
sudo docker network create --driver bridge <your-network-name>
```



## API

To setup API Image

```bash
sudo docker build -t text_anonymizer:api -f ./app/Dockerfile.api .
```

To create API Container

```bash
sudo docker run -d --name api -p 8000:8000 text_anonymizer:api --network <your-network-name>
```

## WebApp

To start up docker web app image

```bash
sudo docker build -t text_anonymizer:app -f ./app/Dockerfile.webapp .
```

To start up the web app container

```bash
sudo docker run -d --name app -p 80:8501 text_anonymizer:app --network <your-network-name>
```

