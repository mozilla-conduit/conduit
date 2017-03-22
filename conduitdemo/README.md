# Conduit Demo

Follow these instructions to demo using the 'hg conduitstage'
command.

- Open 2 terminals
- In one terminal run `docker-compose up` inside the `conduitdemo` folder.
  You should run `docker-compose build --no-cache` first if this is your
  first time pulling from the repo in a while.
- In the other terminal run `docker-compose run demo /bin/sh`. This will
  open a shell in the demo container which has the client extension installed.
- In the demo container, run `hg clone http://hgserver:8080/testrepo`.
- `cd` inside that repo and make as many commits as you like.
- Run `hg conduitstage -r . http://hgserver:8080/testrepo`. This will run
  the stage commands within the docker-compose environment, hitting all
  the way to the commit index and anything else the commit index does like
  posting to bugzilla once that is functioning.
- Verify the result in the running log of docker-compose in the first terminal.

