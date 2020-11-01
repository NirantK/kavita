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
ADD requirements.txt .
ADD Alfaaz.py .

EXPOSE 8501
RUN pip install -r requirements.txt
RUN pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
ADD sentiment_detection.py .