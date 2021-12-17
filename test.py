import requests

base_path = "http://android-task-tracker-backend.herokuapp.com"
session = requests.Session()

requests_total = 0


def respInfo(resp):
    global requests_total
    requests_total += 1
    print("#", requests_total, ": ", sep="")
    print(resp.status_code, resp.headers)
    print(resp.content.decode())
    print("---")


def post(path, data):
    respInfo(session.post(base_path + path, data=data))


def put(path, data):
    respInfo(session.put(base_path + path, data=data))


def get(path):
    respInfo(session.get(base_path + path))


def delete(path):
    respInfo(session.delete(base_path + path))


if __name__ == '__main__':
    # Auth user
    get("/")

    post("/eig", {
        "matrix": [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    })



