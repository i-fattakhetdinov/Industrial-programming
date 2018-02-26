FROM python:2.7-onbuild
RUN apt-get update
RUN sh -c '/bin/echo -e "Y" | apt-get install netcat'
RUN python -m pip install pymongo
RUN pip2 install -r requirements.txt
ADD start.sh /start.sh
CMD ["/start.sh"]

