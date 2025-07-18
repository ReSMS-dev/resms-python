from .service import SMSService

send = SMSService().send

__all__ = ["send"]
