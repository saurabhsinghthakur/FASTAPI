"""
Response Component based on FAST API
@author: Saurabh Singh <sa786bh@gmail.com>
@since: 1
"""
from fastapi.responses import ORJSONResponse

class Response():
    # @var string HTTP response formats
    def __init__(self, **kwargs):
        self.__response = kwargs.get('response', {})
        self.__status_code = kwargs.get('status_code', 200)
        self.__errors = kwargs.get('errors', {})
    
    def success(self):
        final_response = {
            "status": "success",
            "results": self.__response,
            "errors": {},
            "code": self.__status_code
        }
        return final_response

    def error(self):
        final_response = {
            "status": "failed",
            "results": {},
            "errors": self.__errors,
            "code": self.__status_code
        }
        return final_response