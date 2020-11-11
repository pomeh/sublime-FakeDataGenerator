

# Fake Data Generator

## Description

This package will repeat the selected text N times, and also may generate Fake Data if you wish using the awesome external library [Faker][]

`CTRL+SHIFT+P` to access to the command pallete and select `Fake: it!` .

Behind the escenes, this package calls [Faker][] methods in short hand (without the need to write the class name `faker.`)

## Usage

-   Enclose the data to fake with `{{` and `}}` with the proper name of the function to call. See examples.

-   Select the text (The package is capable to handle multiple selections)

-   Done!

### Installation

Download or clone the contents of this repository to a folder named exactly as the package name into the Packages/ folder of ST.

## Example

-   Write, or copy and paste the following in a new ST tab/view:

-   { "{{index()}}": "{{name()}}", }

-   Then select the inner portion marked as code:

-   { `"{{index()}}": "{{name()}}",` }

-   CTRL+SHIFT+P

-   Type: Fake: It!

-   Repeat: 3

-   Press Enter

-   This is the current output:

-   { `"1": "Trina Friesen","2": "Mack Koch","3": "Burney O'Kon",`

}

## Package Methods and Modifiers

-   `index()` \# will keep an internal autoincrement counter [this is not provided by faker]

    -   You may wish to keep aditionals autoincrement counters. You can keep separated counters by providing an argument as index such `index(1)` or `index('goals')`

-   Supports three basic modifiers: `repeat`, `encode` and `escape`.

    -   For example

        -   "{{index()|repeat(3)}}"

    -   Will run the faker function three times and produce

        -   "1,2,3"

    -   For example

        -   "{{index()|repeat(3, '-')}}"

    -   Will produce

        -   "1-2-3"

    -   For example

        -   "{{url()|encode()}}"

    -   Will produce

        -   "http%3A%2F%2Fcarroll.biz%2F"

    -   For example

        -   "{{name()|escape()}}"

    -   Will produce

        -   Dalibor Ma\\u0161ek \# for Dalibor Mašek

## Handy List of Faker Methods (see [complete list in Faker documentation][])

## BASIC METHODS

name() \# Dalibor Mašek

first\_name() \# Vendula

last\_name() \# Dušková

safe\_email() \# <ikucera@example.net>

date\_time\_this\_year() \# 2013-07-12 12:07:09

url() \# <http://www.duskova.cz/>

uri\_path(deep=None) \# app/categories/category

ipv4() \# 97.154.116.193

random\_int(min=0, max=9999) \# 5018

boolean(chance\_of\_getting\_true=50) \# True

words(nb=3) \# ducimus ex rerum

sentence(nb\_words=6, variable\_nb\_words=True) \# Et eos et adipisci sed suscipit maiores.

md5(raw\_output=False) \# 22b9f5010ee6434c5672af4f223f9c4e

random\_element(array=('a', 'b', 'b')) \# b

## TEXT

random\_letter() \# i

sentence(nb\_words=6, variable\_nb\_words=True) \# Et eos et adipisci sed suscipit maiores.

sentences(nb=3) \# Quis tempora nisi necessitatibus libero ipsum fugit eos ......

text(max\_nb\_chars=200) \# Iusto deserunt rerum nostrum quia doloremque. Rem ...

word() \# ut

words(nb=3) \# ducimus ex rerum

paragraphs(nb=3) \# Molestiae quae et placeat illum perferendis........

paragraph(nb\_sentences=3, variable\_nb\_sentences=True) \# Voluptate tenetur qui ......

## DATE TIME

year() \# 2009

month() \# 06

day\_of\_month() \# 23

month\_name() \# February

day\_of\_week() \# Wednesday

timezone() \# Asia/Yerevan

date(pattern="%Y-%m-%d") \# 1995-12-23

time(pattern="%H:%M:%S") \# 10:37:21

date\_time() \# 1989-11-02 09:28:43

date\_time\_this\_decade() \# 2014-01-16 12:06:02

date\_time\_this\_year() \# 2013-07-12 12:07:09

date\_time\_this\_month() \# 2014-03-07 20:03:09

iso8601() \# 1993-12-04T02:47:48

am\_pm() \# AM

unix\_time() \# 1351615176

## PERSON

name() \# Dalibor Mašek

first\_name() \# Vendula

last\_name() \# Dušková

user\_name() \# zuzana.polakova

safe\_email() \# <ikucera@example.net>

email() \# <marketa06@seznam.cz>

phone\_number() \# 733 971 899

job() \# Physiological scientist

company() \# Pospíšil o.s.

company\_suffix() \# a.s.

credit\_card\_number(card\_type=None, validate=False, max\_check=10) \# 4486550681899265

## LOCATION

address() \# Za Křížem 71 191 02 Letovice

street\_name() \# Poslední

street\_address() \# Na Lázeňce 4/9

postcode() \# 417 77

locale() \# en\_WS

country() \# Samoa

country\_code() \# BN

language\_code() \# pt

city\_name() \# Bohušovice nad Ohří

city() \# Spálené Poříčí

state() \# Jihočeský kraj

latitude() \# -68.8597715

longitude() \# 56.371770

## INTERNET

url() \# <http://www.duskova.cz/>

uri() \# <http://zeman.cz/>

domain\_name() \# horakova.cz

tld() \# com

uri\_path(deep=None) \# app/categories/category

uri\_page() \# main

ipv4() \# 97.154.116.193

ipv6() \# 37cc:ff29:d8ee:bda4:24cb:76fc:7c7e:a130

user\_agent() \# Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.0; Trident/5.0)

## COLOR

rgb\_css\_color() \# rgb(241,137,244)

hex\_color() \# \#f2e171

## NUMBERS

random\_int(min=0, max=9999) \# 5018

random\_digit() \# 8

random\_number(digits=None) \# 610456427

numerify(text="\#\#\#") \# 607

## MISCELANEA

password(length=10, special\_chars=True, digits=True, upper\_case=True, lower\_case=True) \# BAgRm)CTXJ

md5(raw\_output=False) \# 22b9f5010ee6434c5672af4f223f9c4e

sha1(raw\_output=False) \# c58d17a41060bbf38b5ce501c721d7114205c095

sha256(raw\_output=False) \# a2ce2b5a7288467d158880c113a04aa95b6e441173c6e4d4ac08a616bd4195ff

null\_boolean() \# None

[1] <http://www.sublimetext.com/>

[2] <https://sublime.wbond.net/installation>

[3] <https://github.com/joke2k/faker>

[4] <https://github.com/joke2k/faker>

  [Sublime Text 3+]: http://www.sublimetext.com/
  [Package Control 2]: https://sublime.wbond.net/installation
  [Faker]: https://github.com/joke2k/faker
  [complete list in Faker documentation]: http://fake-factory.readthedocs.org/en/latest/providers.html
