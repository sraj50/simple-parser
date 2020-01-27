# simple-parser
A basic parser to investigate natural-language posts from a Q&amp;A site


The dataset to be parsed comes from https://hardwarerecs.stackexchange.com a Q&A site for hardware recommendations. The data itself is in XML format.

Each line represents a record of a post begining with <row> and ending with />

Each post has four attributes
  Id: unique identifier of each post
  PostTypeId: 1=question, 2=answer, 3-8:others
  CreationDate: creation date & time of post (yyyy-mm-ddThh:mm:ss)
  Body: content of post
