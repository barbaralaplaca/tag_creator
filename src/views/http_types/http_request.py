

class HttpRequest:
    def __init__(
            self,
            header: dict = None,
            body: dict = None,
            query_params: dict = None
    ) -> None:
        self.header = header
        self.body = body
        self.query_params = query_params
