import requests
import requests_cache
from api import parser


class wrapper():
    def __init__(self, proxy=None, cookie=None, cache=None, cacheTime=86400, backend='sqlite'):
        self.baseUrl = f'https://www.{proxy}' if proxy else 'https://www.1377x.to'
        self.headers = {
            "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Sec-Gpc": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }

        if cookie:
            self.headers['cookie'] = f'cf_clearance={cookie}'

        self.requests = requests_cache.CachedSession(cache, expire_after=cacheTime, backend=backend) if cache else requests

    def search(self, query, page=1, category=None, sortBy=None, order='desc', torrent_only=False):
        query = '+'.join(query.split())
        category = category.upper() if category and category.lower() in ['xxx', 'tv'] else category.capitalize() if category else None
        url = f"{self.baseUrl}/{'sort-' if sortBy else ''}{'category-' if category else ''}search/{query}/{category+'/' if category else ''}{sortBy.lower()+'/' if sortBy else ''}{order.lower()+'/' if sortBy else ''}{page}/"

        response = self.requests.get(url, headers=self.headers)
        return parser.torrentParser(response, baseUrl=self.baseUrl, page=page, torrent_only=torrent_only)

    def trending(self, category=None, week=False, torrent_only=False):
        url = f"{self.baseUrl}/trending{'-week' if week and not category else ''}{'/w/'+category.lower()+'/' if week and category else '/d/'+category.lower()+'/' if not week and category else ''}"

        response = self.requests.get(url, headers=self.headers)
        return parser.torrentParser(response, baseUrl=self.baseUrl, torrent_only=torrent_only)

    def top(self, category=None, torrent_only=False):
        category = 'applications' if category and category.lower() == 'apps' else 'television' if category and category.lower() == 'tv' else category.lower() if category else None
        url = f"{self.baseUrl}/top-100{'-'+category if category else ''}"

        response = self.requests.get(url, headers=self.headers)
        return parser.torrentParser(response, baseUrl=self.baseUrl, torrent_only=torrent_only)

    def popular(self, category, week=False, torrent_only=False):
        url = f"{self.baseUrl}/popular-{category.lower()}{'-week' if week else ''}"

        response = self.requests.get(url, headers=self.headers)
        return parser.torrentParser(response, baseUrl=self.baseUrl, torrent_only=torrent_only)

    def browse(self, category, page=1, torrent_only=False):
        category = category.upper() if category.lower() in ['xxx', 'tv'] else category.capitalize()
        url = f'{self.baseUrl}/cat/{category}/{page}/'

        response = self.requests.get(url, headers=self.headers)
        return parser.torrentParser(response, baseUrl=self.baseUrl, page=page, torrent_only=torrent_only)

    def info(self, link=None, torrentId=None):
        if not link and not torrentId:
            raise TypeError('Missing 1 required positional argument: link or torrentId')
        elif link and torrentId:
            raise TypeError('Got an unexpected argument: Pass either link or torrentId')

        link = f'{self.baseUrl}/torrent/{torrentId}/h9/' if torrentId else link
        response = self.requests.get(link, headers=self.headers)

        return parser.infoParser(response, baseUrl=self.baseUrl)