import json
import pprint

def read_file(file_path):
    """
    return file content read from given file
    :param file_path:
    :return:
    """
    buffer = ""
    buffer += open(file_path, "rU").read()
    return buffer


def read_formatted_tweets():
    dir_path = "datacollection/json_tweets"
    json_tweets_files = {
        "Nunavut-Iqaluit": "jaon_name_Nunavut-Iqaluit.txt",
        "Yukon-Whitehorse": "json_name_Yukon-Whitehorse.txt",
        "Northwest Territories-Yellowknife": "json_name_Northwest_Territories-Yellowknife.txt",
        "Saskatchewan-Regina": "json_name_Saskatchewan-Regina.txt",
        "Quebec-Quebec City": "json_name_Quebec-Quebec_City.txt",
        "Prince Edward Island-Charlottetown": "json_name_Prince_Edward_Island-Charlottetown.txt",
        "Nova Scotia-Halifax": "json_Nova-Scotia-Halifax.txt",
        "Newfoundland and Labrador-St. John's": "json_Newfoundland_and_Labrador-St. John's.txt",
        "New Brunswick-Fredericton": "json_New_Brunswick-Fredericton.txt",
        "Manitoba-Winnipeg": "json_Manitoba-Winnipeg.txt",
        "British Columbia-Victoria": "json_Manitoba-Winnipeg.txt",
        "Alberta-Edmonton": "json_Alberta-Edmonton.txt"
    }

    province_tweets_collection = dict()

    for (province_city, file_name) in json_tweets_files.items():
        result = []
        (province, city) = province_city.split("-")
        buffer = read_file(dir_path + "./" + file_name)
        json_data = json.loads(buffer)
        for (user_name, user_data) in json_data[0].iteritems():
            result.extend(user_data)
        province_tweets_collection[province] = result

    return province_tweets_collection

# pprint.pprint(read_formatted_tweets())