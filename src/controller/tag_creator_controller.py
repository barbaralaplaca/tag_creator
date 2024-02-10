from src.drivers.barcode_handler import BarcodeHandler


class TagCreatorController:
    """ Responsibility for implementing business rules """

    def create(self, product_code: str) -> dict:
        path_from_tag = self.__create_tag(product_code)
        formatted_response = self.__format_response(path_from_tag)
        return formatted_response

    def __create_tag(self, product_code: str) -> str:
        barcode_handler = BarcodeHandler()
        path_from_tag = barcode_handler.create_barcode(product_code)
        return path_from_tag

    def __format_response(self, path_from_tag: str) -> dict:
        return {
            "data": {
                "type": "Tag Image",
                "count": 1,
                "path": f'{path_from_tag}.png'
            }
        }
