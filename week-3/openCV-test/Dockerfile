FROM python:3

ADD countblack.py /

ADD /img /img/

RUN pip install pystrich
RUN pip install openCV-python

CMD [ "python", "countblack.py", "img" ]
