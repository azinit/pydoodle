# TODO: @extends/@implements IOStream
# TODO: Catch exceptions

import json


class JsonStream:
    @staticmethod
    def read(path, encoding="utf-8"):
        with open(path, mode="r", encoding=encoding) as file:
            data = json.load(file)
            return data

    @staticmethod
    def write(path, data: dict, encoding="utf-8"):
        with open(path, mode="w", encoding=encoding) as file:
            json.dump(data, file)


if __name__ == '__main__':

    fp = "../../user_info.json"
    _data = JsonStream.read(fp)
    print(_data)
    _data["best_score"] = 13
    JsonStream.write(fp, _data)
