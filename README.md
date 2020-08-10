Hi! Welcome to Pio Report Pull, a class that allows you to download files that are saved within P.io's system. 

- Why do I need this? 

If you are a P.io user, you know that the api provided for users does not allow you to access reports that you created within the system. 
This class solution will allow you to access those reports programtically. To completely take advantage of this solution, 
I would set this class to run through a chron so that you can get your reports on a schedule! 

- Awesome! What do I need to know to use it right away? * I am assuming you have a basic understanding of Python. 

This is using chrome selenium. If chrome is not on the computer you will be running this on, install it on the computer before using this scripts. 
Also, install the libraries that are in the import lines in the 'pio.py' file. 

To use the class and pull a report right away you would do the following: 

   - ReportOne = PioReportPull(yourusername, password, name of report as seen in pio*) 

  - *Make sure that this is the only report that has that name. 

So, in practice, it would look like: 

  - ReportOne = PioReportPull('xxxx', 'xxxx','Daily_Analytics') 
  
To access the report use: 

  - PioReportPull.get_report_path() 
  - Note: This is assuming that nothing else is being downloaded at the same time.
        The call brings back the complete path from the last downloaded file. 
 
Voila!

Now you can pull it into a DB easily using Pandas, manipulate it in a DataFrame, or do whatever else! 

Please let me know if you have any questions or recommendations for imporvements. 

Thanks, 

Josh


# Pio-Report-Pull
Class that pulls a report from Placements (P.io) using Selenium
