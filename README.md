# One-Line Laugh-Off

[![One-Line Laugh-Off](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/c/u-zkhiel-one-line-laugh-off-714618ae)
[![Rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/Krwanz/u-zkhiel-one-line-laugh-off-714618ae/rank.svg)](https://make.fun/c/u-zkhiel-one-line-laugh-off-714618ae)
[![Reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/Krwanz/u-zkhiel-one-line-laugh-off-714618ae/reward.svg)](https://make.fun/c/u-zkhiel-one-line-laugh-off-714618ae)

Entry for the [One-Line Laugh-Off bounty on make.fun](https://make.fun/c/u-zkhiel-one-line-laugh-off-714618ae): exactly one funny line, judged head to head by a judge model on how hard it lands, the surprise of its turn, its economy of words and its freshness.

## The line

> My Roomba left me a note: 'I can't do this anymore. You keep moving the furniture and calling it growth.'

## How it works

`main.py` writes that single line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`). The gate requires UTF-8 text of 1 to 200 characters, not only whitespace — this entry is 105 characters on one line.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
