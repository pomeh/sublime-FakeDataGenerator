from __future__ import unicode_literals
from ..phone_number import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        '69########',
        '69## ######',
        '69## ### ###',

        '210#######',
        '210 #######',
        '210 ### ####',

        '2##0######',
        '2##0 ######',
        '2##0 ### ###',

        '2###0#####',
        '2###0 ## ###',

        '(+30) 69## ######',
        '+30 69## ######',
        '+3069########',
        '(+30) 2### ######',
        '+30 2### ######',
        '+302#########',
    )
