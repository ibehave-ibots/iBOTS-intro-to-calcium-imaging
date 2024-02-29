def download_file_from_sciebo(public_url, folder, filename):
    import urllib.request
    from pathlib import Path
    path = Path(folder).joinpath(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = urllib.request.urlopen(public_url + "/download").read()
    path.write_bytes(data)