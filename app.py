import os
import pathlib
from typing import List, Tuple, Union, Dict, Iterable, Optional, Any
from flask import Flask, request, jsonify, Response

from functions import com_filter, com_map, com_unique, com_limit, com_sort, com_regex


app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST'])
def perform_query() -> Union[Tuple[str,int],Tuple[Response,int]]:
    """
    The function implements a view that processes the request by the POST method at the address "/perform_query",
    accepts five parameters in the request body: where four parameters define the requests and their parameters,
    and the fifth is the file name. The query result is returned as a list of found elements in JSON format.
    """
    req_json: Optional[Dict[str,Any]] = request.json

    if req_json is None:
        return '', 400

    file_name: Union[str, None] = req_json.get("file_name")
    com_list: List[Tuple] = [(req_json.get("cmd1"), req_json.get("value1")),
                             (req_json.get("cmd2"), req_json.get("value2"))]

    if not file_name:
        return '', 400

    path = pathlib.Path(f"{DATA_DIR}/{file_name}")

    if not path.is_file():
        return '', 400

    with open(path, 'r', encoding='utf-8') as file:
        data: Iterable[str] = file
        for cmd, value in com_list:
            if cmd == "filter":
                data = com_filter(data, str(value))
            elif cmd == "map":
                if not (value.isdigit() or type(value) == int):
                    return '', 400
                data = com_map(data, int(value))
            elif cmd == "limit":
                if not (value.isdigit() or type(value) == int):
                    return '', 400
                data = com_limit(data, int(value))
            elif cmd == "unique":
                data = com_unique(data)
            elif cmd == "sort":
                if type(value) != str and value not in ['desc', 'asc']:
                    return '', 400
                data = com_sort(data, value)
            elif cmd == "regex":
                if type(value) != str:
                    return '', 400
                data = com_regex(data, value)
            else:
                return '', 400

    return jsonify(data), 200


if __name__ == '__main__':
    app.run(debug=True)
