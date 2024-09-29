# CryptoTools

## Setup

### Prerequisites

- Python 3.12+

- MySQL Client Libraries for Python.

    On Debian/Ubuntu-based distros, run the following:

        ```sh
        sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
        ```

    For other distros as well as operating systems, see the full guide at <https://pypi.org/project/mysqlclient/>.

### Create Database and Setup Environment Variables

You have to create a `.env` file at the project root
containing the values of the required environment
variables. See the `example.env` file to know what
those variables are.

Some variables require setting up a database.

### Install Python Packages

You may want to create and activate a virtual environment
(venv) first. Then, at the project root, run

    ```sh
    pip install -r requirements.txt
    ```

## Launch the App

Activate the venv if necessary. Then, at the project
root, execute

    ```sh
    flask run
    ```

Alternatively, to enable hot-reloading (flask to automatically
reload the app when some code changes):

    ```sh
    flask run --debug
    ```

## Database Migration

Whenever some models change, create a new migration
and apply it for the changes to actually take
effect/be reflected in the database.

To do that, activate the venv if necessary, then
execute

    ```sh
    flask db migrate -m "Migration content, e.g. rename column C of table T"
    flask db upgrade
    ```

## License

Copyright (C) 2024-now Vu Tung Lam and Nguyen Van Thien.

Licensed under the 3-clause BSD license. See
[LICENSE.txt](./LICENSE.txt) for details.
