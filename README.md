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
import resms
resms.api_key = "your_api_key"
```

## Usage
You can send a SMS using:
```python
resms.sms.send(to="+33123456789", message="Code 123456", senderId="ReSMS")
```

You can send an OTP using:
```
resms.otp.send(to="+33123456789", message="Your OTP is {CODE}", senderId="ReSMS")
```

## Documentation
The full documentation is available at [docs.resms.dev](https://docs.resms.dev/python).

Here is an implementation example of ReSMS Python package: https://github.com/ReSMS-dev/resms-python-example

## License
This project is licensed under the MIT License.

## Note
This is a simple SDK for ReSMS. More features and improvements will be added in the future. If you have any suggestions or issues, please tell us on our discord server: [Discord](https://discord.gg/EasHpu2qTj).
