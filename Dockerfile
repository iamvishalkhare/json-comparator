FROM ubuntu 
MAINTAINER vishalkhare39@gmail.com

RUN apt-get update
RUN git clone https://github.com/iamvishalkhare/json-comparator.git
RUN cd jsoncomparator
RUN pip3 install -r requirements.txt
CMD ["echo","Vishal's docker Image created"] 