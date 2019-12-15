# Amazon Affiliate Earning reports automation
How to automate Amazon Associates earnings report download. 

This script basically automates the earning reports from your amazon affiliate site. Since there is no API or anything to make this automatic I built this selenium script that basically goes into the report page and request a new report and downloads it into whatever directory you selected.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.



### Installing Selenium

For this to run we need to make sure we have Selenium installed. To install it do the following


```
brew install selenium-server-standalone
```

### Running the script

Once you get Selenium then you can go to the terminal and run the follwong

```
python3 amazon-affiliate-automation.py

```

This will ask you 3 questions: 

* Directory where you want to save your file
* username
* password ( dont worry i didnt add anything here to steal your password)

I created these inputs so that I dont have to leave the fields blanks, but if you want to run this file everyday without having to put the inputs then you can edit the variables at the top and add your credentials there.

```python

download_dir = "your/directory/here"
user = "user@name.com"
password = "password"

```

This script will make sure that there is no pop up window when downlaing the file. So sit back and enjoy. I will be adding a cleaning file to create visualizations with the data.
