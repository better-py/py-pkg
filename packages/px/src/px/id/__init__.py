import time

from loguru import logger
from tsidpy import TSID


def generate_id_str():
    """Generate a string representation of a new ID
    生成一个新的 ID 的字符串表示

    _example_: [
        0KAPXXQJKG83B, 0KAPXXQJKG83C,
        0KAPXXQJKG83D, 0KAPXXQJKG83E,
        0KAPXXQJKG83F, 0KAPXXQJKG83G,
        0KAPXXQJKG83H, 0KAPXXQJKG83J,
        0KAPXXQJKG83K, 0KAPXXQJKG83M,
    ]
    Returns:
        _type_: str
        _description_: 生成一个新的 ID 的字符串表示
    """

    return TSID.create()


def generate_id_digit():
    """Generate a numeric representation of a new ID
    生成一个新的 ID 的数字表示

    _example_: [
        696615413582069203, 696615413582069204,
        696615413582069205, 696615413582069206,
        696615413582069207, 696615413582069208,
        696615413582069209, 696615413582069210,
        696615413582069211, 696615413582069212,
    ]

    Returns:
        _type_: int
        _description_: 生成一个新的 ID 的数字表示
    """
    return TSID.create().number
