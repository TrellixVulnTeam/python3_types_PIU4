from typing import Any

class chatbot:
    l: Any = ...
    chatbot: Any = ...
    def __init__(self) -> None: ...
    chatbotIdentifier: Any = ...
    def legacyConverts(self) -> None: ...
    async def sortMessage(self, message: Any) -> None: ...
    async def serviceIdentifier(self, fromService: Any, fromServer: Any, fromChannel: Any, toService: Any, toServer: Any, toChannel: Any, message: Any): ...
    async def sendWebhook(self, message: Any, objDeliveryDetails: Any, FormattingOptions: Any, formattingSettings: Any, formatType: Any, messageUnchanged: Any) -> None: ...
    async def sendMessage(self, message: Any, objDeliveryDetails: Any, FormattingOptions: Any, formattingSettings: Any, formatType: Any, messageUnchanged: Any) -> None: ...