###################################################################################
#################################### Wikipedia Searcher ###########################
###################################################################################

import wikipediaapi as Wiki

# set Wikipedia and language 
wiki = Wiki.Wikipedia('en')

# Get Single Page
p = wiki.page('Python')

# Get Title of Page
print("Page title:" , p.title)

# Get Page Summary
print("Summary: ", p.summary)

# Get URL of Page
print("Page_Url: ", p.fullurl)

# Get Full Text of Page
print("Full Text: ", p.text)

# change language of Page
p = wiki.page('Python', language='de')

# Get Page Categories
print("Categories: ", p.categories)