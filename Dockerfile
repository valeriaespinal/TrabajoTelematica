FROM ubuntu
RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install flask
RUN pip3 install -f requirements.txt
COPY proyectofinal / 
EXPOSE 80

