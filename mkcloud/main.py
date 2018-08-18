#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np
import random

def mkcloud(filename, dic, theme_start, theme_end):

    def linear_gradient(n=10):
        ''' returns a gradient list of (n) colors between
        two hex colors. start_hex and finish_hex
        should be the full six-digit color string,
        inlcuding the number sign ("#FFFFFF") '''
        # https://gist.github.com/RoboDonut/83ec5909621a6037f275799032e97563
        start = tuple(int(theme_start.lstrip('#')[i:i+2], 16) for i in (0, 2 ,4))
        end = tuple(int(theme_end.lstrip('#')[i:i+2], 16) for i in (0, 2 ,4))
        RGB_list = [start]
        for t in range(1, n):
            curr_vector = tuple([
                int(start[j] + (float(t)/(n-1))*(end[j]-start[j]))
                for j in range(3)
            ])
            RGB_list.append(curr_vector)
        return ['#%02x%02x%02x'%i for i in RGB_list]

    colors = linear_gradient()

    def color_from_theme(word, font_size, position, orientation, random_state=None, **kwargs):
        return random.choice(colors)

    font_path = './NotoSansCJKkr-Regular.otf'
    x, y = np.ogrid[:800, :800]
    mask = (x - 400) ** 2 + (y - 400) ** 2 > 360 ** 2
    mask = 255 * mask.astype(int)
    wc = WordCloud(
        color_func=color_from_theme, 
        font_path=font_path, 
        background_color="rgba(255, 255, 255, 0)", 
        mode="RGBA", mask=mask, width=800, height=800
    )
    wc.generate_from_frequencies(dic)
    wc.to_file(filename)
