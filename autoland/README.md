# Mozilla Autoland

A web service and user interface for automatically landing changes to Mozilla Mercurial repositories.


## Building Autoland

##### Prerequisites

 * `docker` (on OS X you will want `docker-machine`, too)
 * `docker-compose`
 * `pyinvoke` (v0.13+, can be installed on OS X with a [Homebrew formula](http://brewformulas.org/pyinvoke))


##### Running the development server

To build and start the development services' containers: 

```bash
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

```bash
$ curl $(docker-machine ip default):8888
...
```


To make a request directly to the Autoland web service API, you will want to
use the URL `http://[MY_DOCKER_HOST_IP]:8888/api/`.  For example:

```bash
$ curl localhost:8888/api/v1/repos/conduit/series/bz://1234/a
```

##### Running the test suite and tasks

To see all available tasks, pass `-l` or `--list` to pyinvoke:

```bash
$ invoke -l
```

To run the entire test suite (front-end and back-end tests):

```bash
$ invoke test
```

To run a specific test or test module in the Python back-end, use one of the
[various methods](http://doc.pytest.org/en/latest/usage.html#specifying-tests-selecting-tests)
pytest has for test selection and pass it to pytest with the `-t` or
`--testargs` flag:

```bash
$ invoke autoland.test.webapi -t '-k name_of_my_test_or_module'
```

For help with a specific task, use `-h` or `--help`

```bash
$ invoke -h autoland.test.ui
```

##### Submitting Code

Make sure your code passes lint and tests first:

```bash
$ invoke lint
$ invoke test
```

The dev environment comes with [YAPF](https://github.com/google/yapf) pre-
installed for super-fast fixing of code style and pep8 violations.

To reformat your code automatically, run:

```bash
$ invoke format
```

We use [Google-style Python comments](https://google.github.io/styleguide/pyguide.html#Comments) in our docstrings.