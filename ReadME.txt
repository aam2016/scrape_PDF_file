Details

The job consists in taking a pdf (sample of a few pages provided) and exporting its content into a tabular format (excel or csv). 

Page structure:
Each page contains information about a company and should be represented as a new row in the export file.
On the page itself, there is a list of key/value pairs. The keys should be represented as columns and the values as the cell value.

Document structure:
Sometimes, there are section title pages - they should be ignored.
The number of pages in each section will vary so the script should not expect the number of pages in each section to be the same between sections.

The deliverable is a script written in Python or Ruby that processes a PDF of a similar structure to the sample provided and outputs an excel/csv file.
Alongside the script, a 'how-to install and run the script' guide shall be provided, especially if the script has dependancies like packages or gems.