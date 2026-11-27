# news-repo-20261127
[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/yyyywaiwai/news-repo-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/yyyywaiwai/news-repo-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

Entry for make.fun's [news-image-20261127](https://make.fun/bounty/news-image-20261127) bounty: one image summing up the world's news of Friday, 27 November 2026.

The front page leads with the Iranian drone strike in Kuwait that killed two Italian workers (Tehran denies responsibility), plus the Thanksgiving storms snarling US travel, Russia hitting two foreign grain ships off Odesa, Hamas weighing its reply after Israel killed 10 in Gaza, UK net migration at its lowest since 1997, Depardieu facing trial, a tanker capsizing off Ibiza, and the Gukesh–Sindarov marathon draw at the World Chess Championship.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (1024x1024, 95,039 bytes)
python3 main.py --verify-only   # check the image without writing output
```

`main.py` copies the shipped `entry.png` to the output directory (or `/output` by default) and verifies it is a PNG within the 1 MiB / 1024x1024 limits, re-checking the copy's hash after writing.
