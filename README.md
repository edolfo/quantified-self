# Starting Up

### Requirements
* Docker
* Ports `[6001, 6002, 6003, 27019]` must be open

### Quickstart
From this directory, run:

`bash up.sh`

This should (eventually) get you into the shell; after you see something like this:

```bash
Creating hckrlabs-quant-self_mongo_1 ... done
Creating hckrlabs-quant-self_app_1   ... done
```

...you may need to hit `Enter` to get a cursor.

Once inside the shell, run the following commands:

```bash
npm run setup
npm start
```

* The `npm run setup` command will install all needed python and javascript dependencies.
* The `npm start` command will launch a `nodemon` process to automatically restart the `Flask` server
on server-side file changes.  It will also launch a front-end toolchain (`react-scripts`) that
will similarly automatically compile and refresh your webpage on client-side file changes.
