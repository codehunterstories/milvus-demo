# Build a Question Answering Engine

[link] <https://github.com/towhee-io/examples/blob/main/nlp/question_answering/1_build_question_answering_engine.ipynb>

## Preparations

[notice] Python version >= 3.7.x & Only online

### Install Milvus

[link] <https://milvus.io/docs/install_standalone-docker.md>

### Clone model

``` bash
git submodule status
# Init submodule on first time
git submodule init question_answer/model/dpr-ctx_encoder-single-nq-base
git submodule update question_answer/model/dpr-ctx_encoder-single-nq-base
```

## Deploy On Local

### Install Dependencies

``` bash
python -m pip install -r requirements.txt
```

### Set Up the Environment

``` bash
export MILVUS_IP={your milvus ip. default '127.0.0.1'}
export MILVUS_PORT={your milvus port. default '19530'}
export MILVUS_DATASET_PATH={your dataset path. default './dataset/question_answer.csv'}
```

### Load vector into Milvus

``` bash
python create_milvus_collection.py
python load_embedding.py
```

### Run on Gradio

``` bash
python release.py
```

## Deploy On Docker

### Load vector into Milvus (On Docker.)

``` bash
docker build -t python:3.9.17-milvus -f ./docker/load.Dockerfile .
docker run --rm --name milvus-towhee \
-e MILVUS_IP={your milvus ip. default '127.0.0.1'} \
-e MILVUS_PORT={your milvus port. default '19530'} \
-e MILVUS_DATASET_PATH={your dataset path. default './dataset/question_answer.csv'} \
-v ./model:/usr/local/towhee/model \
-it python:3.9.17-milvus
```

### Run on Gradio (On Docker.)

``` bash
docker build -t python:3.9.17-gradio -f ./docker/release.Dockerfile .
docker run --name gradio \
-e MILVUS_IP={your milvus ip. default '127.0.0.1'} \
-e MILVUS_PORT={your milvus port. default '19530'} \
-e MILVUS_DATASET_PATH={your dataset path. default './dataset/question_answer.csv'} \
-v ./model:/usr/local/towhee/model \
-p 7860:7860 \
-itd python:3.9.17-gradio
```

## Access

Running on local URL:  <http://127.0.0.1:7860>

Running on public URL: <https://7efbf90b-a281-48f9.gradio.live>
