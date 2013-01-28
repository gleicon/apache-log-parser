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

## Before using it

    Run python updatedb to fetch and compile the GeoIP db.

## Usage

Here are some example uses:

    python apache_parser.py access.log subscriptions
    python apache_parser.py access.log uri --quantity 5
    python apache_parser.py access.log agent --cutoff 100
    
    to test the full json report:

    python apache_parser.py access.log agent full | pbcopy
    then paste it on (http://jsonlint.com)

There is help available at the command-line as well.

    python apache_parser.py --help

## Full report

    Apart from an array of hashes, each hash meaning a log line with geoip resolution, there's an item for each count report (client_ip, uri, time, status_code< referral, agent and subscriptions), lines_matched and total_lines.
    
## TODO
    Work on the regexp to avoid non-matches

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

* updatedb.py and search.py are (c) Alex Fiori

This script draws inspiration and code from:

* original repo: https://github.com/lethain/apache-log-parser
* freegeoip: https://github.com/fiorix/freegeoip
* http://effbot.org/zone/wide-finder.htm
* http://www.python.org/dev/peps/pep-0265/
