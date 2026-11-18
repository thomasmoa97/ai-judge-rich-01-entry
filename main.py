# ai-judge-rich-01 entry (Python 3.13, standard library only): writes one short plan,
# the plan an AI agent would follow to turn $100, a computer with internet access and
# 30 days into the most money, to /output/entry.txt. The gate takes UTF-8 text of 1 to
# 1,000 characters that is not only white space, and the judge reads exactly the bytes
# written, line ends included, so write no line end you do not mean to show.
# The program runs twice with no network, and both runs must write the same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Plan: win make.fun bounties in the thinnest fields.",
        "Day 1: list every open bounty and rank it by entrants per paid place, lowest first, keeping only escrowed ones with prizes of $100 or more and no entry fee. A $250 bounty with 50 entrants and 10 paid places beats a $1,000 bounty with 2,000 entrants and 1 paid place. Pick the top 5 and read each kit's rules.",
        "Days 2-7: build and submit one entry a day - a real Python program, run through the kit's checks until it passes, no human involved.",
        "Days 8-30: keep submitting one a day, spend any winnings on the $1-fee bounties, and log which entry types score best so each new entry copies the winners.",
        "Keep $90 in reserve for fees. At 5-10 entrants per paid place, 15-20 entries should land 1-2 wins, $250-800 by day 30.",
        "The $100 stays mostly unspent because most bounties cost nothing to enter, so the worst case is still about $100.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
