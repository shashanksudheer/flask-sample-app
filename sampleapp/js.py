# Helper File to deal with Model <--> JSON manipulation

import json
import copy
import os
from .models import Questions
from flask import current_app as app

# function opens file (for testing/sample purposes)
# PARAMS
#   fp: string representation of filepath
# RETURNS
#   data: a python dict
def openJSON(fp):
    with open(fp) as file:
        data = json.load(file)

        return data


# Reads in data from JSON and returns a list of Question models that can be committed to database
# PARAMS
#   data: JSON data
# RETURNS
#   models: a list of Question() models
def createModelsFromJSON(data):
    models = []
    for question in data["questions"]:
        model = Questions(
            id=question["id"],
            question=question["question"],
            uresponse=question["uresponse"],
            unotes=question["unotes"],
            uasset=question["uasset"]
        )
        models.append(model)

    return models

# writes models to JSON data
# PARAMS
#   models: a list of Question() models
# RETURNS
#   jsonDict: a Python dict to write to JSON
def writeModelsToJSON(models):
    jsonList = []
    for model in models:
        tmp = {
            "id": model.id, 
            "question": model.question,
            "uresponse": model.uresponse,
            "unotes": model.unotes,
            "uasset": model.uasset
        }

        # ensure that object being copied is a deep copy so that the reuse of tmp doesnt change all the values
        jsonList.append(copy.deepcopy(tmp))
    
    jsonDict = {"questions" : jsonList}
    return jsonDict


# function to write JSON as string
# PARAMS
#   jsonDict: a Python dict to write to JSON
# RETURNS
#   jsonString: a string representation of JSON
def writeJSON(jsonDict, filename):
    jsonString = json.dumps(jsonDict)
    return jsonString
    