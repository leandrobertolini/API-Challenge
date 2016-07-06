
from django import conf


def get_provinces_from_xy(x, y):
    provinces = []

    for provinces_name in conf.settings.PROVINCES.keys():
        x_bottom_right = x <= conf.settings.PROVINCES[provinces_name]['bottomRight']['x']
        x_upper_left = x >= conf.settings.PROVINCES[provinces_name]['upperLeft']['x']

        y_bottom_right = y >= conf.settings.PROVINCES[provinces_name]['bottomRight']['y']
        y_upper_left = y <= conf.settings.PROVINCES[provinces_name]['upperLeft']['y']

        if x_upper_left and x_bottom_right and y_bottom_right and y_upper_left:
            provinces.append(provinces_name)

    return provinces


def get_provinces_from_all_cordinates(ax, ay, bx, by):
    provinces = []

    for provinces_name in conf.settings.PROVINCES.keys():
        x_bottom_right = int(bx) <= conf.settings.PROVINCES[provinces_name]['bottomRight']['x']
        x_upper_left = int(ax) >= conf.settings.PROVINCES[provinces_name]['upperLeft']['x']

        y_bottom_right = int(by) >= conf.settings.PROVINCES[provinces_name]['bottomRight']['y']
        y_upper_left = int(ay) <= conf.settings.PROVINCES[provinces_name]['upperLeft']['y']

        if x_upper_left and x_bottom_right and y_bottom_right and y_upper_left:
            provinces.append(provinces_name)

    return provinces
