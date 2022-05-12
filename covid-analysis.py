from flask import Flask
from flask_restful import Resource, Api
import csv
import os

app = Flask(__name__)
api = Api(app)

FLASK_PORT = CODE_HOME = os.environ.get('FLASK_PORT', '5100')

print("Api running on port : {} ".format(FLASK_PORT))


def csvtojson(csvfilepath):
    jsonArray = []
    with open(csvfilepath, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)
        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)
    return jsonArray


def fetchdata(func):
    def inner(anls_class):
        jsonArray = csvtojson('covid-analysis.csv')

        # getting the returned value
        returned_value = func(anls_class, jsonArray)

        # returning the value to the original frame
        return returned_value
    return inner


class LatestCovidData(Resource):
    def get(self):
        jsonArray = csvtojson('latest-covid-data.csv')
        return jsonArray, 200


class MostAffectedCountry(Resource):

    @fetchdata
    def get(self, jsonArray):
        return '{} is most affected by covid with death rate {}.'.format(
            jsonArray[0]['most_affected'],
            jsonArray[1]['most_affected']), 200


class LeastAffectedCountry(Resource):

    @fetchdata
    def get(self, jsonArray):
        return '{} is least affected by covid with death rate {}.'.format(
            jsonArray[0]['least_affected'],
            jsonArray[1]['least_affected']), 200


class HighestCovidCases(Resource):

    @fetchdata
    def get(self, jsonArray):
        return '{} is having highest confirmed covid cases {}.'.format(
            jsonArray[0]['highest_cases'],
            jsonArray[1]['highest_cases']), 200


class LowestCovidCases(Resource):

    @fetchdata
    def get(self, jsonArray):
        return '{} is having lowest confirmed covid cases {}.'.format(
            jsonArray[0]['lowest_cases'],
            jsonArray[1]['lowest_cases']), 200


class TotalCases(Resource):

    @fetchdata
    def get(self, jsonArray):
        return 'Total confirmed covid cases {} across world.'.format(
            jsonArray[0]['lowest_cases']), 200


class HighestCovidEfficiency(Resource):

    @fetchdata
    def get(self, jsonArray):
        return '{} has highest recoverd cases per confirmed cases with rate {}.'.format(
            jsonArray[0]['highest_efficiency'],
            jsonArray[1]['highest_efficiency']), 200


class LowestCovidEfficiency(Resource):

    @fetchdata
    def get(self, jsonArray):
        return '{} has highest recoverd cases per confirmed cases with rate {}.'.format(
            jsonArray[0]['lowest_efficiency'],
            jsonArray[1]['lowest_efficiency']), 200


class HighestActiveCases(Resource):

    @fetchdata
    def get(self, jsonArray):
        return '{} is most suffering from covid with {} active cases.'.format(
            jsonArray[0]['highest_suffering'],
            jsonArray[1]['highest_suffering']), 200


class LowestActiveCases(Resource):

    @fetchdata
    def get(self, jsonArray):
        return '{} is least suffering from covid with {} active cases.'.format(
            jsonArray[0]['lowest_suffering'],
            jsonArray[1]['lowest_suffering']), 200


api.add_resource(LatestCovidData, '/latest-covid-data')
api.add_resource(MostAffectedCountry, '/most-affected-country')
api.add_resource(LeastAffectedCountry, '/least-affected-country')
api.add_resource(HighestCovidCases, '/highest-cases')
api.add_resource(LowestCovidCases, '/lowest-cases')
api.add_resource(TotalCases, '/total-cases')
api.add_resource(HighestCovidEfficiency, '/highest-covid-efficiency')
api.add_resource(LowestCovidEfficiency, '/lowest-covid-efficiency')
api.add_resource(HighestActiveCases, '/highest-active-cases')
api.add_resource(LowestActiveCases, '/lowest-active-cases')

if __name__ == '__main__':
    app.run(port=FLASK_PORT)
