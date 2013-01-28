# apache_parser.py

This is a fork/mutation of a apache log parser script. I've found it a good enough parser to add GeoIP resolution and JSON serialization.
The original can be found at the end of this document. All credits to the original author and FreegeoIP author.

At this time it supports generating reports for:

* **client_ip** - client ip count (added)
* **uri** - pageviews for each uri
* **time** - datetime with highest request/second
* **status_code** - hits for each http status code
* **referral** - uris of referring sites
* **agent** - hits for each user agent
* **subscriptions** - the number of feed subscribers per uri.
    This is done by parsing user agents for their subscriber count.

In addition to the above, I've added GeoIP resolution and a JSON report

* **full** - all lines parsed as json (added)

## Usage

Here are some example uses:

    python apache_parser.py access.log subscriptions
    python apache_parser.py access.log uri --quantity 5
    python apache_parser.py access.log agent --cutoff 100
    
There is help available at the command-line as well.

    python apache_parser.py --help


## User agents successfully parsed for feed subscribers

These are the feeds that have been tested against
the feed subscription system:

    Feedfetcher-Google; (+http://www.google.com/feedfetcher.html; 3 subscribers; feed-id=7675226481817637975)
    Netvibes (http://www.netvibes.com/; 5 subscribers; feedId: 5404723)
    Bloglines/3.1 (http://www.bloglines.com; 1 subscriber)
    NewsGatorOnline/2.0 (http://www.newsgator.com; 1 subscribers)
    Zhuaxia.com 1 Subscribers
    AideRSS/1.0 (aiderss.com); 2 subscribers
    xianguo-rssbot/0.1 (http://www.xianguo.com/; 1 subscribers)
    Fastladder FeedFetcher/0.01 (http://fastladder.com/; 1 subscriber)
    HanRSS/1.1 (http://www.hanrss.com; 1 subscriber)
    livedoor FeedFetcher/0.01 (http://reader.livedoor.com/; 1 subscriber)


## Credits

This script draws inspiration and code from:

* original repo: https://github.com/lethain/apache-log-parser
* freegeoip: https://github.com/fiorix/freegeoip
* http://effbot.org/zone/wide-finder.htm
* http://www.python.org/dev/peps/pep-0265/
