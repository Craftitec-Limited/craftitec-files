class CustomException(Exception):
    def __init__(
            self,
            detail: str,
            tag: str,
            status_code: int = None,
            ) -> None:
        
        self.status_code = status_code
        self.detail = detail
        self.tag = tag

    def __str__(self) -> str:
        return f"{self.status_code}: {self.detail}"

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(status_code={self.status_code!r}, detail={self.detail!r})"
