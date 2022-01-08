---
title: iphone-text-extract-then-format
---

Note: All of the heavy lifting is done by [iphone-message-export](https://github.com/sethrj/iphone-message-export) from [Seth R. Johnson](https://github.com/sethrj) <-- check out that repository

# Iphone Text Message Export and Format

Extracts messages from an iphone backup folder using [libimobiledevice](), converts it to a json format using [iphone-message-export](https://github.com/sethrj/iphone-message-export), and finally converts it to a readable html format using the `format.py` script. 

_worked on an iphone 6s using ubuntu 21_

**Motivation**: I was having a lot of trouble finding a way to back up all my messages in a readable format from an iphone (particularly on linux); all the solutions were required buying software. I was able to get it working with the following instructions / scripts (mostly relying on [iphone-message-export](https://github.com/sethrj/iphone-message-export) from [Seth R. Johnson](https://github.com/sethrj), which does all the heavy lifting). Posting it all here in case it helps anyone.


# Usage

## Step 1: Download libmobile

On Debian / Ubuntu terminal:

```bash
sudo apt-get install libimobiledevice-utils
```

## Step 2: Backup a plugged in iphone

```bash
idevicebackup2 backup backup_folder_location/ # <-- backup in location of your choosing
````
^ place all the contents from `backup_folder_location/` into the local `backup/` folder in this repository

## Step 3: Extract all the messages

Use the `export.py`, which is a slightly modified script from [Seth Johnson's iphone-message-export repo](https://github.com/sethrj/iphone-message-export), to convert all the messages to json format

open the export.py file, and change the backup & export folder variables at beginning of script if you need to

Then:
```bash
python3 export.py
```
^ or whatever you use to call python

## Step 4: Convert to HTML

Finally, convert it all to html with the `format.py` file.

Open the `format.py` file and change the user variable at the top of the script to the phone number of the iphone you backed up

```bash
python3 format.py
```

And that's it. All in a readable format; images too. This is what it'll look like:

![example](_/example.png)



# Roadmap
- [ ] have it use contacts to get actual names instead of numbers
- [ ] improve formatting in html
- [ ] convert to an electron app to put all those paid apps out of business