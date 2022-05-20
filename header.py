# dash imports 
import dash
from dash import dcc
from dash import html

# plotly imports
import plotly.express as px

# panda imports
import pandas as pd

# system imports
import schedule
import time

# import Flask
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

# import dummy_data from data.py
from data import dummy_data


# create a retrieve_data function
def retrieve_data():
    # return dummy data from data.py
    return dummy_data

# create an export_graph function that takes a figure, a name and a format
def export_graph(figure, export_name, extension):
    # write figure to file
    figure.write_image(f'{export_name}.{extension}')
    
