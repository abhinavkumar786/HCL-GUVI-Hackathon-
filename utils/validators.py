class InputValidator:
    @staticmethod
    def validate_file(file_path: str) -> bool:
        return file_path.endswith(".pdf")
