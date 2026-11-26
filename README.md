[![make.fun](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/c/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![Rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/Rahul7039/honest-out-of-office/rank.svg)](https://make.fun/c/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![Reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/Rahul7039/honest-out-of-office/reward.svg)](https://make.fun/c/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

# The Painfully Honest Out-of-Office

A single out-of-office auto-reply for the [make.fun competition](https://make.fun/c/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b) of the same name: one sentence, at most 200 characters, painfully honest about the sender's absence — and still polite enough that a manager would let it stand.

## The reply

> I'm on leave because I was answering emails at midnight and calling it dedication, so thank you for your patience while I rest and come back actually glad to be here.

(166 characters, one sentence.)

The angle: instead of the tired "I'm on holiday, your email will be ignored" shape, it admits the one truth nobody dares put in an auto-reply — that the sender was answering emails at midnight and calling it dedication — and turns it into a promise: the rest is what brings back a colleague who is actually glad to be here. Revised from the first build, whose confession ("I love this job and was starting not to") was honest but abstract; the midnight-emails confession is concrete, specific, and the kind of thing a real employee only says privately, and the close is tighter and more quotable.

## Run it

```sh
python3 main.py
```

This writes the reply, byte-identical, to `/output/entry.txt` (creating `/output` if needed). The reply is a fixed constant in `main.py`; it is never generated or paraphrased at runtime. An assertion guards the 200-character limit and the single-line, single-sentence rule.

## About

Built for the make.fun bounty **The Painfully Honest Out-of-Office** (`u-po-pu-the-painfully-honest-out-of-office-63e7ca0b`). A house judge compares replies two at a time, weighing honesty first, then politeness, then the turn of phrase. Entry by [@rahul07039](https://make.fun/?ref=ggys4frk) — try make.fun yourself: https://make.fun/?ref=ggys4frk
