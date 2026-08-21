# Private Family Catalogue

A one-page catalogue of a private collection coming out of storage, built for auction houses to review.

[Website](https://ianduncanmagee.com) · [LinkedIn](https://www.linkedin.com/in/ianduncanmagee) · [GitHub](https://github.com/AladdinYan) · [Substack](https://substack.com/@worldaccordingtoian)

![Private Family Catalogue](assets/readme/hero.png)

## What it does

- Presents 36 numbered items across nine categories, each with a photo carousel and description
- A Gallery tab shows all 128 photographs in a filterable masonry wall
- Click any photo for a full-size viewer with keyboard navigation and a jump back to the item
- Light and dark view with a one-click toggle
- Contacts tab with a direct email button for enquiries

## Built with

Hand-written HTML, CSS and vanilla JavaScript in a single self-contained file; photos embedded as data URIs; EB Garamond and Archivo via Google Fonts.

## How to run it

Open `index.html` in a browser. That is the whole site.

```bash
open index.html
```

To change an item, edit the `ITEMS` list in `build/build_site.py` and rebuild:

```bash
python3 build/build_site.py
```

## Status

Complete and live. Next: a separate valuation pass on the paintings.

## Project structure

```
magee-showroom/
├── index.html          # the entire site, photos included
├── build/
│   ├── build_site.py   # rebuilds index.html from the item list
│   └── photos/         # web-sized photos, one per catalogue image
└── assets/readme/      # README hero image
```

All photographs are family property. All rights reserved; no reuse without permission.
