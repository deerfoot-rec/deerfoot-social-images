# deerfoot-social-images

Public image host for Deerfoot's weekly social posts. Buffer needs public image URLs, so every post image is rendered here and linked as
`https://raw.githubusercontent.com/deerfoot-rec/deerfoot-social-images/main/<YYYY-MM-DD>/post.png` (date = the day the post goes out).

- `assets/` - Deerfoot logo (logo.svg wordmark, icon.svg mark)
- `templates/` - starting-point HTML layouts (1080x1350, Magnolia #fbf5ff background, Rhino #263d5a text, Morning Glory #a4dfd9 accent, Montserrat 500/600/800). Copy one, change the content, keep the look.
- `src/render.py` - `python3 src/render.py templates/x.html out.png` renders a layout to PNG with Playwright.
