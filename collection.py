# name: masihullah wardak
# date 4/28/2025
# description: in this code we have people's names and death time. and by running the code it shows their name and the year they died.

# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = {
    "Charles Dickens": 1870,
    "William Thackeray": 1863,
    "Anthony Trollope": 1882,
    "Gerard Manley Hopkins": 1889
    }

for author, date in authors.items():
    
    print ("%s died in %d." % (author, date))
