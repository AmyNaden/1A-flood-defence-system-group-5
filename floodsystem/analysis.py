import numpy as np
import matplotlib.dates as datex
import datetime

def polyfit(dates, levels, p):
    # Looping through dates to assign dates to x and water level to y
    dates = datex.date2num(dates)
    # Finds coefficients of best fit polynomial
    p_coeff = np.polyfit(dates, levels, p)
    # Converting coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)
    # Finding date offset in days
    date_now = datetime.today
    d0 = datex.date2num(date_now) - dates[0]
    return (poly, d0)
