from .._client import BaseClient


class OtpService:
    @classmethod
    def create(
        cls,
        to: str,
        message: str,
        sender_id: str = None,
        code_type: str = None,
        code_length: int = None,
        validity_minutes: int = None,
    ):
        payload = {
            "to": to,
            "message": message,
        }
        if sender_id is not None:
            payload["senderId"] = sender_id
        if code_type is not None:
            payload["codeType"] = code_type
        if code_length is not None:
            payload["codeLength"] = code_length
        if validity_minutes is not None:
            payload["validityMinutes"] = validity_minutes
        return BaseClient().post("/otp", payload)

    @classmethod
    def verify(cls, to: str, code: str):
        payload = {
            "to": to,
            "code": code,
        }
        return BaseClient().post("/otp/verify", payload)

    @classmethod
    def delete(cls, otp_id: str):
        payload = {
            "otpId": otp_id,
        }
        return BaseClient().delete("/otp", payload)
