FROM debian:bullseye

RUN apt-get -y update && apt-get -y upgrade && \
    apt-get install -y python3.9 python3-pip \
    zsh git curl

RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

RUN mkdir -p /app/src

WORKDIR /app/src

COPY requirements.txt .

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "tail", "-f", "/dev/null" ]
# ENTRYPOINT [ "sh", "build-tools/start.sh" ]
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
