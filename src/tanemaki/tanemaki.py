""" Tanemaki """
from datetime import datetime
import argparse

ARGS_PARSER = argparse.ArgumentParser()
ARGS_PARSER.add_argument("--plan", help="料金プラン情報表示", action="store_true")

class Tanemaki:
    """
    タネマキの諸々情報を保持する

    Examples
    --------
    >>> from tanemaki import Tanemaki
    >>> t = Tanemaki()
    >>> t    # タネマキの情報を表示します
    2011年12月01日生まれなので、もう 7 年目もぐー
    >>>
    >>> Tanemaki.say_moguo('エアコンを取り替える')     # もぐおになれます
    'エアコンを取り替えるもぐー'
    >>>

    Attributes
    ----------
    birthdt : datetime
        生年月日
    guests : list
        来客者リスト
    """
    MOGUO_SUFFIX = 'もぐー'
    TANEMAKI_URL = 'https://tane-maki.net'
    TANEMAKI_URL_PRICING = TANEMAKI_URL + '/pricing/'

    def __init__(self):
        self.birthdt = datetime.strptime('2011-12-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        self.guests = []

    def __len__(self):
        return (datetime.now() - self.birthdt).days

    def __repr__(self):
        args = ARGS_PARSER.parse_args()
        if args.plan:
            res = '料金プランは {} を参照'.format(self.TANEMAKI_URL_PRICING)
        else:
            res = '{}生まれなので、もう {} 年目'
            res = res.format(self.birthdt.strftime('%Y年%m月%d日'), self.get_years())
        return self.say_moguo(res)

    def __add__(self, guest):
        self.guests.append(guest)
        return self.say_moguo('{} さん、いらっしゃい'.format(guest))

    def __radd__(self, guest):
        return self + guest

    def __lshift__(self, guest):
        return self + guest

    def __sub__(self, guest):
        if guest in self.guests:
            self.guests.pop(self.guests.index(guest))
            return self.say_moguo('{} さん、またおいで'.format(guest))
        return self.say_moguo('すでに {} さんは帰ってる'.format(guest))

    def __rsub__(self, guest):
        return self - guest

    def __rshift__(self, guest):
        return self - guest

    def __rlshift__(self, guest):
        return self >> guest

    def __rrshift__(self, guest):
        return self << guest


    def __getitem__(self, index):
        if len(self.guests) < index:
            raise IndexError()
        return self.guests[index]


    def get_years(self):
        """
        何年目なのか
        """
        nowdt = datetime.now()
        birthdt = self.birthdt
        years = nowdt.year - birthdt.year
        if nowdt < (self.birthdt.replace(year=birthdt.year + years)):
            years -= 1
        return years


    @staticmethod
    def say_moguo(strsay):
        """
        あなたのかわりに、もぐおが発言します

        Parameters
        ----------
        strsay : str
            あなたの発言

        Returns
        -------
        str
            もぐおの発言
        """
        return strsay + Tanemaki.MOGUO_SUFFIX
