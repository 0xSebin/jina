FROM docker:24.0.2-git

RUN apk update && apk upgrade && apk --no-cache add curl bash make

CMD ["bash"]