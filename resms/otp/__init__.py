from .service import OtpService

create = OtpService().create
verify = OtpService().verify
delete = OtpService().delete

__all__ = ["create", "verify", "delete"]
