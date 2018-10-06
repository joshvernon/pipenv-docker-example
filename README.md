# pipenv-docker-example
Yet another example of a dockerized Python app using pipenv

### Running
```
sudo docker build -t pipenv-example .
sudo docker run -it --rm --name pipenv-example-rt pipenv-example
```

### See also
- [https://hub.docker.com/_/python/](https://hub.docker.com/_/python/)
- [https://stackoverflow.com/a/49705601](https://stackoverflow.com/a/49705601)
- [dfederschmidt's example app](https://github.com/dfederschmidt/docker-pipenv-sample) and its corresponding [blog post](https://federschmidt.xyz/python/docker/docker-pipenv/)
