#!/usr/bin/env python

__author__ = 'Shanquel Scott study hall John W., Gabby and Sondos'


import requests
import turtle
import urllib.request
import json
import time


def astro():
    workers = ""
    r = requests.get('http://api.open-notify.org/astros.json').json()
    print(f"There are a total of {r['number']} people in space")
    print(r)
    for people in r['people']:
        workers += people['name'] + ' is on ' + people['craft'] + '\n'
    print(workers)


def coords():
    r = requests.get('http://api.open-notify.org/iss-now.json').json()
    print(f"The current geographic {r['iss_position']['latitude']}")
    print(f"The current geographic {r['iss_position']['longitude']}")


def geographic_turtle():
    r = requests.get('http://api.open-notify.org/iss-now.json').json()
    lat = r['iss_position']['latitude']
    lon = r['iss_position']['longitude']
    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('map.gif')
    screen.register_shape('iss.gif')
    iss = turtle.Turtle()
    iss.shape('iss.gif')
    iss.setheading(90)
    iss.penup()
    iss.goto(float(lon), float(lat))


def indiana_time():
    lat_indy = 39.76838
    lon_indy = -86.15804
    location_indy = turtle.Turtle()
    location_indy.penup()
    location_indy.color('yellow')
    location_indy.goto(lon_indy, lat_indy)
    location_indy.dot(5)
    location_indy.hideturtle()
    url = 'http://api.open-notify.org/iss-pass.json?'
    params = f'lat={lat_indy}&lon={lon_indy}'
    response_indy = urllib.request.urlopen(url + params)
    result_indy = json.loads(response_indy.read())
    over_indy = result_indy['response'][1]['risetime']
    location_indy.write(time.ctime(over_indy), font=('Lato', 20, 'bold'))


def main():
    astro()
    coords()
    geographic_turtle()
    indiana_time()
    turtle.done()


if __name__ == '__main__':
    main()
