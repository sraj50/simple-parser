# simple-parser
A basic parser to investigate natural-language posts from a Q&amp;A site


The dataset to be parsed comes from https://hardwarerecs.stackexchange.com a Q&A site for hardware recommendations. The data itself is in XML format.

Each line represents a record of a post begining with <row> and ending with />

Each post has four attributes
  Id: unique identifier of each post
  PostTypeId: 1=question, 2=answer, 3-8:others
  CreationDate: creation date & time of post (yyyy-mm-ddThh:mm:ss)
  Body: content of post


<b>Process Data</b><br>
The first step is to process the XML data by doing some clean up so that only the body of post is available.

Special characters ("&#xA", "&#xD") are replaced by single empty space.

XML character references are changed to their original representation. For example, "&amp" to &, "&quot" to ", "&pos" to ', "&gt" to >, "&lt" to <

All HTML tags are also removed.
