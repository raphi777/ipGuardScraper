def get_search_url(mp, search_term):
    if mp.id == "TRENDYOL_DE":
        return "https://www.trendyol.com/de/sr?q={0}&qt={0}&st={0}&os=1".format(search_term)
