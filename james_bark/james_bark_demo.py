# -*- coding: utf-8 -*-
import pandas as pd

from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio


def buzi():
    # download and load all models
    preload_models()

    # generate audio from text
    text_prompt = """
         Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
         But I also have other interests such as playing tic tac toe.
    """
    audio_array = generate_audio(text_prompt)

    # play text in notebook
    Audio(audio_array, rate=SAMPLE_RATE)


def main():
    buzi()


if __name__ == '__main__':
    # pandas 配置
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 10000)
    pd.set_option('display.max_colwidth', 1000)
    pd.set_option('display.max_rows', None)

    # 业务逻辑
    main()
