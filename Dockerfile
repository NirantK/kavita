FROM python:3.7-slim

RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'
RUN apt-get update && apt-get install
RUN apt-get -y install wget
ADD requirements.txt .
ADD Alfaaz.py .
ADD sentiment_detection.py .
RUN mkdir Hinglish-Bert-Class
# Downloading model from https://huggingface.co/meghanabhange/Hinglish-Bert-Class
RUN wget https://s3.amazonaws.com/models.huggingface.co/bert/meghanabhange/Hinglish-Bert-Class/config.json -O ./Hinglish-Bert-Class/config.json
RUN wget https://cdn.huggingface.co/meghanabhange/Hinglish-Bert-Class/pytorch_model.bin -O ./Hinglish-Bert-Class/pytorch_model.bin
RUN wget https://cdn.huggingface.co/meghanabhange/Hinglish-Bert-Class/special_tokens_map.json -O ./Hinglish-Bert-Class/special_tokens_map.json
RUN wget https://cdn.huggingface.co/meghanabhange/Hinglish-Bert-Class/tokenizer_config.json -O ./Hinglish-Bert-Class/tokenizer_config.json
RUN wget https://cdn.huggingface.co/meghanabhange/Hinglish-Bert-Class/vocab.txt -O ./Hinglish-Bert-Class/vocab.txt


RUN pip install -r requirements.txt
RUN pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
EXPOSE 8501