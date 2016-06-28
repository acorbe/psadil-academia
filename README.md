# academia-ipsum
A template for building an academic website with using [Pelican](http://blog.getpelican.com/) Static Site Generator, powered by [Python](https://www.python.org/). Based on the [academia theme](https:/github.com/wjhopper/academia). See it in action at http://people.umass.edu/whopper

#### Dependencies
An installation of Python. If you don't have python installed already installed, you can install the most recent Python release [from here](https://www.python.org/downloads/release/python-352/). Alternatively, you can install base python along with many commonly used packages by installing the [Anaconda](https://www.continuum.io/downloads) Python distribution.

Once you have installed Python, open a python shell and the install the Pelican and Markdown packages

```python
pip3 install Pelican Markdown
# or simply pip, if you have Python 2.x
```

To take advantage of the Makefile for automated deployment options, make sure you have `make` intalled and accessible on your path.

## Installation
The simplest way to get started is to download and extract [the zip file](#) for this repo. If you care about getting updates for the [academia] theme, then you should either clone or fork this repository (see these links for how-to's in case your are not familiar with these operations).

## Customization
Once you have a copy of this repo on your computer, start customizing the content! It helps to read through the Pelican documentation before getting started, to have an idea about what all this is about, and to consult the documentation throughout your setup process.

To customize the site and add your own content, you should be familiar with [Markdown](http://daringfireball.net/projects/markdown/). If you are not, see the [syntax guide](http://daringfireball.net/projects/markdown/syntax) to get up to speed.

#### Pelicanconf
In the `pelicanconf.py` file, be sure to update the following settings to real values:

```python
AUTHOR = 'First M. Last'
SITENAME = 'First M. Last'
SITESUBTITLE = 'Things and Stuff, Stuff and Things'
SITEURL = 'localhost:8000'
THEME = './academia'
AVATAR = 'blank_avatar.png'
## If you don't have a github page or don't want to share your email, etc.,
## you can delete the entire entry for that item to remove it from the sidebar
LINKS = (('cv', 'path/to/your/CV.pdf'),
         ('email', 'mailto:username@domain_name'),
         ('github', 'https://github.com/your_real_username'))
```

#### Files
The files `misc/Fake_CV.pdf` and `img/blank_avatar.png` are place holders you should replace with your own C#avatarV and picture.

#### Pages
There are 5 files in the `content/pages` directory: `publications.md`, `presentations.md`, `code.md`, `courses.md`, and `home.md`. The publications, presentations, code, and courses files are meant to be lists of publications, presentations, etc., with links to accompanying content. You should customize these boilerplate lists with your own content.

When linking to static content (e.g., pdfs, powerpoints, etc.,) from these pages, be sure to prefix the path to these files with `{filename}`, to ensure the links are correctly generated by Pelican.

The `home.md` file is special: its content is injected into the home page. It is recommended to keep the `status` option in the header for this file set to `hidden`, to avoid generating an extra entry for it in the navigation bar.

#### Blog
The files in the `content/posts` directory are used to create the blog posts. Two fake blog posts are included in the files `blog1.md` and `blog2.md` for demonstration purposes.

## Producing Content
To see your site and test out changes, start up the development web server by running `make devserver` in the directory where your Pelican site is set up, and navigate your web browser to http://localhost:8000

For information on publishing your site, read the [publishing docs](http://docs.getpelican.com/en/3.6.3/publish.html)

To sync local content

```
make rsync_upload
```

If you need to checkout the pages that were uploaded, use

```
ssh user@webadmin.oit.umass.edu
```
