import requests
import config

class AddEntry:
    def new_entry(self, content_id):
        url = "https://online-movie-database.p.rapidapi.com/title/get-details"

        querystring = {"tconst": content_id}
        headers = {
            "X-RapidAPI-Key": config.API_KEY,
            "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
        }
        response_data = requests.request("GET", url, headers=headers, params=querystring)
        response = response_data.json()

        content_type = response.get('titleType', None)
        if content_type == 'movie':
            content_data = {
                'id': response.get('id', None)[7:].rstrip('/'),
                'title': response.get('title', None),
                'titleType': response.get('titleType', None),
                'runningTimeInMinutes': response.get('runningTimeInMinutes', "N/A"),
                'year': response.get('year', "N/A"),
                'image': response.get('image', {}).get('url', "/static/images/placeholder.png")
            }
        elif content_type == 'tvSeries':
            content_data = {
                'id': response.get('id', None)[7:].rstrip('/'),
                'title': response.get('title', None),
                'titleType': response.get('titleType', None),
                'numberOfEpisodes': response.get('numberOfEpisodes', "N/A"),
                'year': response.get('year', "N/A"),
                'seriesStartYear': response.get('seriesStartYear', "N/A"),
                'seriesEndYear': response.get('seriesEndYear', "N/A"),
                'image': response.get('image', {}).get('url', "/static/images/placeholder.png")
            }
        else:
            pass

        return content_data
