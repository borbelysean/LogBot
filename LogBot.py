import sys
import HelpPages.MainHelp as MainHelp
import argparse
from datetime import datetime, date, time
import ArgumentUtils.GenericUtils as GenericUtils
import ArgumentUtils.StartDate as StartDate
#Goose was here




Categories = ["Net", "Auth", "Dev"]

def CommaToList(CSL):
    myList = CSL.split(",")
    for cat in myList:
        if not cat in Categories:
            print("Error: Category " + cat + "is not supported. Supported options are: " + ', '.join(Categories))
            exit(0)
    return myList
    
parser = argparse.ArgumentParser(description="Simplifies the log diagnosis process.")
parser.add_argument("-s", metavar="--start_date", type=str, nargs=1, help="Date in YYYY-MM-DD format to start searching from. All results found to have been logged before this date will be included. If end_date is included only log entries that fall between the start_date and end_date dates will be included.")
parser.add_argument("-e", metavar="--end_date", type=str, nargs=1, help="Date in YYYY-MM-DD format to end searching from. All results found to have been logged after this date will be included. If start_date is included only log entries that fall between the start_date and end_date dates will be included.")
parser.add_argument("-d", metavar="--numDays", type=int, nargs=1, help="Number of days to go back. All resultant log entries that were created on or after numDays before today will be included. Value is ignored if start_date and/or end_date are given.")
parser.add_argument("-H", metavar="--numHours", type=int, nargs=1, help="Number of hours to go back. All resultant log entries that were created numHours ago or sooner will be included. Value is ignored if start_date and/or end_date are given.")
parser.add_argument("-c", metavar="--categories", type=str, nargs=1, help="Category/ Categories to filter results by.")
parser.add_argument("pattern", type=str, nargs=1, help="Regular expression to filter results by.")
args = parser.parse_args()


#Make sure that if either/both the -s and/or -e flags are given, the -d and -H flags are not present. Also
# if the -H flag is present, the -d flag must not be present and vice versa. - TO-DO

if(args.c):
    categories = CommaToList(args.c[0])
    #Consolidate by category - TO-DO
else:
    #Consolidate all log files
    logList = GenericUtils.consolidateLogs()


if(args.s):
    #Check if date is valid
    GenericUtils.checkDate(args.s[0])
    
    start = args.s[0]
    logList = StartDate.filterByStartDate(logList, args.s[0])
if(args.e):
    end = args.e[0]
    #Call EndDate.filterByEndDate()  - TO-DO
if(args.d):
    days = args.d[0]
    #Call NumDays.filterByDays() - TO-DO
if(args.H):
    hours = args.H[0]
    #Call NumHours.filterByHours() - TO-DO
if(args.pattern):
    patternRaw = args.pattern[0]
    #Call Pattern.filterByPattern() - TO-DO



#Finalize Results
with open('res.txt', 'w') as results:
    for l in logList:
        results.write(l[0].strftime("%b %d %Y %H:%M:%S") + " " + l[2] + " " + l[1] + '\n')


    
    
    

