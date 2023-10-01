# Pylint Websockets

A pylint plugin for [websockets](https://github.com/python-websockets/websockets) to [fix import errors](https://github.com/python-websockets/websockets/issues/940). **Should no longer be necessary.**

## Installation

Via Pip

```
pip install pylint-websockets
```

Via Poetry

```
poetry add --dev pylint-websockets
```

## Usage

Add the following arguments when running Pylint:

```
--load-plugins=pylint_websockets
```

Alternatively, add the following to your `pyproject.toml`:

```toml
[tool.pylint.MASTER]
load-plugins = 'pylint_websockets'
```
