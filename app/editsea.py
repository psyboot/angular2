import json


class editSea():
    """docstring for editSea"""
    def __init__(self):
        # super(editSea, self).__init__()
        # self.arg = arg
        self.data = open("data/data.json")

    def loadJson(self):
        self.insea = json.load(self.data, encoding="utf-8")
        print(self.insea)
