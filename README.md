# AskCoding

[![build-status-image]][travis]
[![coverage-status]][coveralls]

## What

AskCoding is primarily a computer science learning resources aggregator. We collect and list learning resources like Books, eBooks, Tutorials, Online Courses, Offline Courses, Blog Posts, Video Talks that can help people learn and understand various topics in Computer Science.

## Why

Finding good resources for a technology/topic is very hard. When you are trying to learn a new technology, either you seek help from close friends/colleagues or search for days on web. Also people have different methodologies that they like while learning. Some like to follow a Book with some exercises, some wants to do an online course while some already know some related technology and wants to a quick primer and dive in. We want to cater this need of learners with AskCoding.

This project is extension of [Codesters](http://codesters.org)([source here](https://github.com/codesters/codesters)). When we first started Codesters, we were students and just started learning Python and JavaScript. The project was very basic in feature set and what it can offer to users. Even then, we are seeing medium traffic since last 3 years from various sources. Now we have more experience with professional web and software development under our belt; we are dedicating our time to this project to build a community where people can suggest good resources to newcomers/students in technologies.

## How

There are already many good listings/aggregators for some technologies. Firstly we would like to get data from there and then have a simple way for people to add new resources or review.

Some of the sources we are looking at for now to get data from:

- Technology/Topic 's own official websites. Many communities have a section for beginners.
- [Awesome lists](https://github.com/sindresorhus/awesome): These are the best, structured lists for various programming languages, technologies.
- Technology/Topic specific sub-reddits.
- Newsletters.

__But this is just Copying stuff from somewhere else__

In all honesty, yes. We are not creating content. And for filling initial content, we are using existing sources of that content. We will give attributions to original source from where we took that data.

__We are also aiming to release regular data dumps for resources on our Platform.__

## Project Technicals

AskCoding is a Django/Python based website. We aim to use these technologies:

- Django as primary web-development framework
- PostgreSQL for data storage
- Redis for caching
- Nginx for serving static files and acting as reverse-proxy for Django.
- ElasticSearch for searching/indexing.

## Guidelines

- We follow [12 factor app](http://12factor.net/) principles for our development and deployment.  
- Flake8 for Python specific linting.
- EditorConfig/isort for formatting Python files.
- Py.test for testing.

## Contributing

If you are excited by the idea and want to help, there are many ways in which you can do that:

- Features/Improvements for Platform: This can be done by anyone. Use our forum/issues page.
- Handling/Writing backend with Python: If you are a Python programmer, this is good way for you to contribute.
- Improving/Suggesting test cases: If you are QA/Tester.
- Improving Platform UX, Website Language/Copy: What should be shown to end-users on various pages. UX developers, Editors can help with this.
- UI/Frontend Design: People with design skills can contribute to frontend html/css/js.

## Installing the AskCoding Development environment

The AskCoding development environment is the recommended option for folks interested in contributing. This is documented in [README.dev.md](README.dev.md).

## License

AskCoding is licensed under MIT. See *LICENSE.md* file.


[build-status-image]: https://secure.travis-ci.org/akarambir/askcoding.svg?branch=master
[travis]: http://travis-ci.org/akarambir/askcoding?branch=master
[coverage-status]: https://coveralls.io/repos/github/akarambir/askcoding/badge.svg?branch=master
[coveralls]: https://coveralls.io/github/akarambir/askcoding?branch=master
