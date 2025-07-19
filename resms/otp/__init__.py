from .service import OtpService

create = OtpService().create
verify = OtpService().verify

__all__ = ["create", "verify"]
