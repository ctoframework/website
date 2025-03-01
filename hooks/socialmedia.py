from textwrap import dedent
import urllib.parse
import re

include = re.compile(r"blog/[1-9].*")

def on_page_markdown(markdown, **kwargs):
    page = kwargs['page']
    config = kwargs['config']
    if False and not include.match(page.url):
        return markdown

    page_url = config.site_url+page.url
    page_title = urllib.parse.quote(page.title+'\n')

    return markdown + dedent(f"""
                             
    ---
                             
    [Share on :fontawesome-brands-x-twitter:](https://x.com/intent/tweet?text={page_title}&url={page_url}){{ .md-button }}
    [Share on :fontawesome-brands-linkedin:](https://www.linkedin.com/sharing/share-offsite/?url={page_url}){{ .md-button }}
    [Share on :fontawesome-brands-facebook:](https://www.facebook.com/sharer/sharer.php?u={page_url}){{ .md-button }}
    """)
