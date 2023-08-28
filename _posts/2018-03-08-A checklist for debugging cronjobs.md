---
layout: single
title: A checklist for debugging cronjobs
comments: true
classes: wide
---

This is a non-exhaustive list of gotchas that I've found myself run into 
time and again when I have to put a scraper or a model on a
cron job. By following these steps you should be able to debug
your cronjob and get it to work as expected.

So, let’s say you have set a Python script as a cron-job,

1. First, make sure the shebang is the first line to your script:

      `#!/usr/bin/env`

2. Check if the script has execution rights, if not, run:

      `chmod +x <script-name>.py`
3. Now, check if script runs with just the script name:

      `./<script-name>.py`

4. Use this command to go into the bash prompt and try step 3:
      `env -i /bin/bash --noprofile --norc`
    
    This should give you an fair idea of why your script is not running.
    Cron executes commands in a different shell and within an empty environment, 
    so without absolute paths it wouldn’t even have access to the user’s version of Python. 
    Hence, its always a better idea to use absolute paths to refer to the script in the cron job 
    and for every file that the Python script uses. 

5. Oftenly, in bash environment the `python` keyword is aimed at the local version of Python.
At this point, it can be a good idea to add the output of $PATH as the first line of the `crontab`. 
Make sure to leave no gap between the “=” sign, like so:
  `SHELL=/bin/sh
  PATH=/home/user/anaconda3/bin`


If the problem still persists, take a long break and head out to stackoverflow.

All the best.

