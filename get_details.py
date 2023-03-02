import requests
import json
import config


class Details:
    def get_details(self, content_id):

        url = "https://online-movie-database.p.rapidapi.com/title/get-overview-details"
        querystring = {"tconst": content_id, "currentCountry": "US"}

        headers = {
            "X-RapidAPI-Key": config.API_KEY,
            "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
        }

        response_data = requests.request("GET", url, headers=headers, params=querystring)
        response = json.loads(response_data.text)

        content_data = []

        content_type = response.get('title', []).get('titleType', None)
        if content_type == 'movie':
            content_data.append({
                'id': response.get('id', None)[7:].rstrip('/'),
                'title': response.get('title', []).get('title', None),
                'titleType': response.get('title', []).get('titleType', None),
                'runningTimeInMinutes': response.get('title', []).get('titleType', "N/A"),
                'year': response.get('title', []).get('year', "N/A"),
                'image': response.get('title', []).get('image', {}).get('url', "/static/images/placeholder.png"),
                'rating': response.get('ratings', []).get('rating', "N/A"),
                'rank': response.get('ratings', []).get('topRank', "N/A"),
                'genres': response.get('genres', "N/A"),
                'release_date': response.get('releaseDate', "N/A"),
                'plot_short': response.get('plotOutline', []).get('text', "N/A"),
                'plot': response.get('plotSummary', []).get('text', "N/A")
            })
        elif content_type == 'tvSeries':
            content_data.append({
                'id': response.get('id', None)[7:].rstrip('/'),
                'title': response.get('title', []).get('title', None),
                'titleType': response.get('title', []).get('titleType', None),
                'numberOfEpisodes': response.get('title', []).get('numberOfEpisodes', "N/A"),
                'year': response.get('title', []).get('year', "N/A"),
                'seriesStartYear': response.get('title', []).get('seriesStartYear', "N/A"),
                'seriesEndYear': response.get('title', []).get('seriesEndYear', "Ongoing"),
                'image': response.get('title', []).get('image', {}).get('url', "/static/images/placeholder.png"),
                'rating': response.get('ratings', []).get('rating', "N/A"),
                'genres': response.get('genres', "N/A"),
                'release_date': response.get('releaseDate', "N/A"),
                'plot_short': response.get('plotOutline', []).get('text', "N/A"),
                'plot': response.get('plotSummary', []).get('text', "N/A")
            })
        else:
            pass

        return content_data
