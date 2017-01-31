# Mozilla Autoland

A web service and user interface for automatically landing changes to Mozilla Mercurial repositories.


## Building Autoland

##### Prerequisites

 * `docker` (on OS X you will want `docker-machine`, too)
 * `docker-compose`


##### Running the development server

To build and start the development services' containers: 

```
$ docker-compose up 
```

On Linux, to test that Autoland web interface is being served:

```
$ curl localhost:8888
<html>
<head>
  <title>Loading...</title>
...
```

On OS X with `docker-machine` you will want to run:

```
$ curl $(docker-machine ip default):8888
...
```


To make a request directly to the Autoland web service API, you will want to
use the URL `http://[MY_DOCKER_HOST_IP]:8888/api/`.  For example:

```
$ curl localhost:8888/api/v1/repos/conduit/series/bz://1234/a
```
