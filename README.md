# Delibar to Buku

Simple Python script I've hacked to import all [Delibar](http://www.delibarapp.com/) bookmarks to [Buku](https://github.com/jarun/Buku).

Since Delibar was discontinued a few years ago and I couldn't find a good way of exporting its data, I've decided to build something to help me achieve that. Buku seems to be a nice option, so I'm giving it a try now.

## Quick Start

If you're already using Buku, maybe it would be a good idea to backup its database with:

```
cp ~/.local/share/buku/bookmarks.db ~/.local/share/buku/bookmarks.db.backup
```

Then, clone this repo and run:

```
pip install -r requirements.txt
python main.py
```

