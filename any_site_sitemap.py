import sys
import logging
from pysitemap import crawler

if __name__ == '__main__':
    if '--iocp' in sys.argv:
        from asyncio import events, windows_events
        sys.argv.remove('--iocp')
        logging.info('using iocp')
        el = windows_events.ProactorEventLoop()
        events.set_event_loop(el)

    # root_url = sys.argv[1]
    name = input("sitename")
    root_url = name 
    crawler(root_url, out_file=f'{name}_sitemap.xml', exclude_urls=[".pdf", ".jpg", ".zip"])
