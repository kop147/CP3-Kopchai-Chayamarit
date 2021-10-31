# can find at www.w3schools.com/python
# transform json format data to python use jason.loads
# transform dictionary data from python to jason use jason.dumps
import json
def readJson():
    x = '{ "name":"john", "age":30, "city":"New York"}'

    y = json.loads(x)

    print(y["name"])


readJson()
