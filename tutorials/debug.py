import urllib
import os
import pandas as pd
import contextily as ctx
from geopandas import GeoDataFrame, read_file
from shapely.geometry import Point, LineString, Polygon
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import psycopg2

import sys
sys.path.append("..")
import movingpandas as mp

import warnings
warnings.simplefilter("ignore")


def countAvgSpeed(trajectory):
    sum = 0
    for speed in trajectory.df.speed:
        sum += speed

