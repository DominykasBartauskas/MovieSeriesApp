import requests
import config


class Search:
    def search_all(self, user_query):
        url = "https://online-movie-database.p.rapidapi.com/title/find"

        querystring = {"q": user_query}
        headers = {
            "X-RapidAPI-Key": config.API_KEY,
            "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
        }
        response_data = requests.request("GET", url, headers=headers, params=querystring)
        response = response_data.json()

        movie_data = []
        series_data = []

        for result in response['results']:
            content_type = result.get('titleType', None)
            if content_type == 'movie':
                movie_data.append({
                    'id': result.get('id', None)[7:].rstrip('/'),
                    'title': result.get('title', None),
                    'titleType': result.get('titleType', None),
                    'runningTimeInMinutes': result.get('runningTimeInMinutes', "N/A"),
                    'year': result.get('year', "N/A"),
                    'image': result.get('image', {}).get('url', "/static/images/placeholder.png")
                })
            elif content_type == 'tvSeries':
                series_data.append({
                    'id': result.get('id', None)[7:].rstrip('/'),
                    'title': result.get('title', None),
                    'titleType': result.get('titleType', None),
                    'numberOfEpisodes': result.get('numberOfEpisodes', "N/A"),
                    'year': result.get('year', "N/A"),
                    'seriesStartYear': result.get('seriesStartYear', "N/A"),
                    'seriesEndYear': result.get('seriesEndYear', "N/A"),
                    'image': result.get('image', {}).get('url', "/static/images/placeholder.png")

                })
            else:
                pass

        return movie_data, series_data
