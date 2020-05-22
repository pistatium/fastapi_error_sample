from typing import Optional, Tuple, List, Type


class ApiError(Exception):
    """ エラーの基底となるクラス """
    status_code: int = 400
    detail: str = 'API error'  # エラー概要
    reason: str = ''  # エラー理由(あれば)

    def __init__(self, reason: Optional[str] = None):
        if reason:
            self.reason = reason

    def __str__(self):
        return f'{self.detail}\n{self.reason}'

    @classmethod
    def as_open_api_definition(cls) -> Tuple[str, dict]:
        """
        OpenAPI の形式でエラーの詳細を記述する
        :return:
        """
        return str(cls.status_code), {
            'description': cls.detail,
            'content': {
                'application/json': {
                    'example': {
                        'detail': cls.detail
                    }
                }
            }
        }


class DontSetDummyParameter(ApiError):
    status_code = 403
    detail = 'ここに値をセットしないでください'


class InvalidFizzBuzzInput(ApiError):
    status_code = 400
    detail = 'input の値が不正です'


class WrongFizzBuzzAnswer(ApiError):
    status_code = 400
    detail = '不正解です'


def error_response(error_types: List[Type[ApiError]]) -> dict:
    d = {}
    for et in error_types:
        status_code, response = et.as_open_api_definition()
        if not d.get(status_code):
            d[status_code] = {
                'description': f'"{et.detail}"',
                'content': {
                    'application/json': {
                        'example': {
                            'detail': et
                        }
                    }
                }}
        else:
            # 同じステータスコードなら description に追記
            d[status_code]['description'] += f'\n"{et.detail}"'
    return d
