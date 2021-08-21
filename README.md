# shsh2-saver

![CI Status](https://github.com/00p513-dev/shsh2-saver/actions/workflows/build.yml/badge.svg?branch=main)

Make a data.json in the same directory like the following:
```
{
	"1" : [
		{
			"apnonce": "3a88b7c3802f2f0510abc432104a15ebd8bd7154",
			"boardConfig": "N53AP",
			"ecid": "48504799564",
			"deviceIdentifier": "iPhone6,2"
		}
	],
	"2" : [
		{
			"apnonce": "27325c8258be46e69d9ee57fa9a8fbc28b873df434e5e702a8b27999551138ae",
			"boardConfig": "D20AP",
			"ecid": "55577356113551420",
			"deviceIdentifier": "iPhone10,1"
		}
	]
}
```

Then run the script with `python3 main.py`

200 = SHSH saved successfully
Anything else: check your json

To use the workflow create a secret named jsonURL with a link to your json
