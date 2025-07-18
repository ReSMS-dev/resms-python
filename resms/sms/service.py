from resms._client import BaseClient


class SMSService:
    @classmethod
    def send(cls, to: str, message: str, sender_id: str = None):
        client = BaseClient()
        payload = {
            "to": to,
            "message": message,
        }
        if sender_id is not None:
            payload["senderId"] = sender_id
        return client.post("/sms/send", payload)
