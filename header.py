import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import schedule
import time

# import Flask
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

# import dummy_data from data.py
from data import dummy_data

def retrieve_data():
    return dummy_data

def export_graph(figure, export_name, extension):
    # write figure to file
    figure.write_image(f'{export_name}.{extension}')