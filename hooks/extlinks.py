import re
from mkdocs.plugins import get_plugin_logger

logger = get_plugin_logger(__name__)

def on_page_content(html, page, config, files):
    """
    Modify generated HTML to add target="_blank" and rel="noopener noreferrer" to all external links.
    """
    # Regex to find external links (not starting with / or #) that don’t already have target=
    external_link_pattern = re.compile(r'<a (?!.*?target=)(href="https?://[^"]+")')

    def add_target_blank(match):
        return f'<a target="_blank" rel="noopener noreferrer" {match.group(1)}'

    modified_html = external_link_pattern.sub(add_target_blank, html)
    return modified_html
