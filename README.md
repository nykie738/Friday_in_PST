# Friday_in_PST
*Today is Friday in California. Shoot!*

Yep, it is the well-known "Today is Friday in California" meme.

Honestly, you can just follow the X bot that tweets the meme video every Friday in Pacific Standard Time (PST). However, I thought of this as a good opportunity to learn how to write an html file and open it through codes.

## Installation
The program uses "pytz". If it is not installed in your (or your friend's) computer, the program will not operate properly. Please confirm that the required libraries are installed (if the computer does not have python, you will need to start from downloading python).
```
pip install pytz
```

So, what if you live in California? Well, in that case, line 10 in caliFriday.py is redundant. You may remove it but keep in mind that line 11 needs to be changed to "if today.weekday() == 4" when line 10 is removed. Otherwise, make sure that caliFriday.py and TIFIC.html are in the same directory. If they are, then you're good to go!

## How to run the program on terminal (not complex):
```
python caliFriday.py
```

## Appendix
For those unfamiliar with the "Today is Friday in California" meme, here's the vid:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/9WaYCdQ8FOQ/0.jpg)](https://www.youtube.com/watch?v=9WaYCdQ8FOQ)

You can also find the lore behind this meme here:

https://knowyourmeme.com/memes/today-is-friday-in-california

