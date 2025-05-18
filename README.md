# ReSMS SDK for Python
Python SDK for ReSMS, a simple and powerful SMS API.

## Installation

```bash
pip install resms
```

## Setup
You need to get an API key on [ReSMS Dashboard](https://resms.dev/dashboard).
Then import the package and create a new instance of the `ReSMS` class with your API key.

```python
from resms import ReSMS
```

## Usage
Send you can send your SMS:
```python
sms = ReSMS("re-1234")
sms.send(to="+33123456789", message="Code 123456")
```

## Documentation
The full documentation is available at [resms.dev/docs](https://resms.dev/docs).

## License
This project is licensed under the MIT License.

## Note
This is a simple SDK for ReSMS. More features and improvements will be added in the future. If you have any suggestions or issues, please open an issue on GitHub.