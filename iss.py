#!/usr/bin/env python

__author__ = 'Shanquel Scott study hall John W.'

import requests
import turtle


def astros():
    workers = ""
    r = requests.get('http://api.open-notify.org/astros.json').json()
    print(f"There are a total of {r['number']} people in space")
    for astros in r['people']:
        workers += astros['name'] + ' is on ' + astros['craft'] + '\n'
    print(workers)
    # return workers


def coords():
    r = requests.get('http://api.open-notify.org/iss-now.json').json()
    print(f"The current geographic {r['iss_position']['latitude']}")
    print(f"The current geographic {r['iss_position']['longitude']}")


def main():
    astros()
    coords()
    turtle.done()


if __name__ == '__main__':
    main()