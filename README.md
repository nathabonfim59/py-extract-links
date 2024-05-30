# What is it?

When I'm doing a pentest, there is a tedious process of extracting all the links from a given webpage to see if there is anything interesting.
Sometimes, they are inside JSONs, JS, and lots of stuff. This is just a script to automate this otherwise kind of tedious process.

If you find it useful, give us a star, and if you find a bug or have a suggestion, feel free to open a PR.

**TLDR:** just some hacked together regexes to extract links from a webpage.

## Usage

```
usage: extract_links.py [-h] [--domains DOMAINS [DOMAINS ...]] [--summary] [--subdomains] source

Extract all links from an HTML file

positional arguments:
  source                URL or file path of the HTML content to extract domains from

options:
  -h, --help            show this help message and exit
  --domains DOMAINS [DOMAINS ...]
                        A list of domains with wildcards like *.google.com
  --summary             Return a summary separated by root domain
  --subdomains          Have a list of subdomains in the summary
```


Example:

### From URL
```
./extract_links.py http://google.com
Domains extracted:
----------------------------------------------------------------------------------------------------
https://mail.google.com/mail/?tab=wm
https://drive.google.com/?tab=wo
http://www.google.com/setprefdomain?prefdom=BR&amp;prev=http://www.google.com.br/&amp;sig=K_0YZ7AcnuSOXsvin5UXnjkzw3HJA%3D
http://www.google.com.br/history/optout?hl=pt-BR
https://www.google.com/url?q=https://gemini.google.com/advanced%3Futm_source%3DHPP-ms%26utm_medium%3DOwned%26utm_campaign%3Di18n-adv-may&amp;source=hpp&amp;id=19042168&amp;ct=3&amp;usg=AOvVa
w259on_boc9RupjNMiGrnfV&amp;sa=X&amp;ved=0ahUKEwjbxd7RhbWGAxUdLrkGHbFOCvMQ8IcBCAY
https://play.google.com/?hl=pt-BR&tab=w8
http://schema.org/WebPage
https://www.youtube.com/?tab=w1
https://www.google.com/imghp?hl=pt-BR&tab=wi
https://www.google.com/images/hpp/gemini-advanced-sparkle-rgb-1-42px.png
https://accounts.google.com/ServiceLogin?hl=pt-BR&passive=true&continue=http://www.google.com/&ec=GAZAAQ
https://news.google.com/?tab=wn
http://maps.google.com.br/maps?hl=pt-BR&tab=wl
https://www.google.com.br/intl/pt-BR/about/products?tab=wh
```

### Summary root domains
```
./extract_links.py http://google.com --summary
Summary separated by root domain:
----------------------------------------------------------------------------------------------------
   9 occurrences: google.com
   3 occurrences: google.com.br
   1 occurrences: schema.org
   1 occurrences: youtube.com
```


### Summary subdomains
```
./extract_links.py http://google.com --summary --subdomains
Summary separated by root domain:
----------------------------------------------------------------------------------------------------
   4 occurrences: www.google.com
   2 occurrences: www.google.com.br
   1 occurrences: news.google.com
   1 occurrences: mail.google.com
   1 occurrences: drive.google.com
   1 occurrences: accounts.google.com
   1 occurrences: schema.org
   1 occurrences: play.google.com
   1 occurrences: maps.google.com.br
   1 occurrences: www.youtube.com
```

### Filter in by domain

> youtube and google urls (you can use `--summary` as well)

```
./extract_links.py http://google.com --domains *google.com.br *youtube.com
Domains extracted:
----------------------------------------------------------------------------------------------------
http://maps.google.com.br/maps?hl=pt-BR&tab=wl
http://www.google.com.br/history/optout?hl=pt-BR
https://www.youtube.com/?tab=w1
https://www.google.com.br/intl/pt-BR/about/products?tab=wh
```

# License
MIT - Basically, you can do whatever you want with it and I'm now responsable for anything you do with it ;)
See the details in the LICENSE file
