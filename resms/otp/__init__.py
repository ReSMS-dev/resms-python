from .service import OtpService

send = OtpService().send
verify = OtpService().verify

__all__ = ["send", "verify"]
