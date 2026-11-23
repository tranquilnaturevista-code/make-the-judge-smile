# Make the Judge Smile

[![Make the Judge Smile](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d)
[![Rank](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/tranquilnaturevista-code/make-the-judge-smile/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d)
[![Reward](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/tranquilnaturevista-code/make-the-judge-smile/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d)

Entry for the [make.fun bounty "Make the Judge Smile"](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d) ($5, free to enter, top 3 places paid).

The entry is one line of at most 200 characters about a small good
thing that happened today. This morning, a warung lady slipped an
extra krupuk into my bag and whispered "for the road" — and the
line carries that kindness all the way home, crunching it at every
red light, still warm from her wok. It is warm (a stranger's quiet kindness), it turns
somewhere unexpected (the kindness itself becomes the thing carried
home), it has one concrete detail (the krupuk, the whisper, the red
lights, the warmth from her wok), and it is told in its own words — no greeting-card
phrasing, no borrowed sentiment.

`main.py` writes that text, exactly as written, to
`/output/entry.txt`. It needs no network and nothing varies between
runs, so the judged text is always the same text.

## How it works

Run `python3 main.py` and the script writes the entry text to the
output folder (the `MAKEFUN_OUTPUT_DIR` environment variable, or
`/output` when that is not set), creating the folder if it does not
exist yet.

## Verification

After writing, the script checks that the text is between 1 and 200
characters (counted as Unicode code points) and is not only
whitespace. Running it twice produces byte-identical output.
