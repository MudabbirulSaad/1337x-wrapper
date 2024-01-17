from api import wrapper
from fastapi import FastAPI, Query
import json


torrents = wrapper(proxy='1337x.to', cache='py1337xCache', cacheTime=500)


app = FastAPI()

@app.post("/search")
async def search(query: str, page: str = 1, category: str = None, sortBy: str = None, order: str = "desc", torrent_only: bool = False):
    result = torrents.search(query=query, page=page, category=category, sortBy=sortBy, order=order, torrent_only=torrent_only)
    return result

@app.post("/trending")
async def trending(category: str = Query(..., description="Category is required"), week: bool = False, torrent_only: bool = False):
    result = torrents.trending(category, week=week, torrent_only=torrent_only)
    return result

@app.post("/top")
async def top(category: str = Query(..., description="Category is required"), torrent_only: bool = False):
    result = torrents.top(category, torrent_only=torrent_only)
    return result

@app.post("/popular")
async def popular(category: str = Query(..., description="Category is required"), week: bool = False, torrent_only: bool = False):
    result = torrents.popular(category, week=week, torrent_only=torrent_only)
    return result

@app.post("/browse")
async def browse(category: str = Query(..., description="Category is required"), page: int = 1, torrent_only: bool = False):
    result = torrents.browse(category, page=page, torrent_only=torrent_only)
    return result

@app.post("/info")
async def info(torrentId: int = 0, link: str = None):
    if torrentId != 0:
        result = torrents.info(torrentId=torrentId)
        return result
    elif link:
        result = torrents.info(link=link)
        return result
    else:
        return  {"message": "Any of Link and torrentId are required."}
