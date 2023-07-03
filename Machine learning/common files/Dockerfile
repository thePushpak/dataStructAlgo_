FROM nvcr.io/nvidia/cuda:11.6.0-devel-ubuntu20.04

RUN apt -y update
RUN apt-get -y update
ENV DEBIAN_FRONTEND=noninteractive
RUN export PYTHONPATH=$PYTHONPATH:/usr/bin
RUN apt-get install -y python3 python3-dev python3-pip
RUN apt-get install -y wget


RUN apt-get install -y software-properties-common
RUN apt-get -y update
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
RUN mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
RUN add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
RUN apt-get -y update
RUN apt-get install -y libcudnn8=8.3.2.*-1+cuda11.5
RUN apt-get install libcudnn8-dev=8.3.2.*-1+cuda11.5

RUN pip install torch==1.10.2+cu113 torchvision==0.11.3+cu113 torchaudio==0.10.2+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
RUN apt-get install -y libcairo2-dev

WORKDIR /srv

COPY requirements.txt/ .
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY src/ ./

RUN export FLASK_APP="app:create_app"

# Run the flask server for the endpoints
CMD ["gunicorn", "-w", "1", "--reload", "-b", ":5037", "app:create_app(testing=False)"]

# flask run -h 0.0.0.0 -p 5035 --debugger --with-threads