# html-wrapper
wrappers for tags and document to write html in and upload to a json file for further use

# How to use:

The best feature of the html-wrapper library is that it is very flexible with unsupported html elements.

If there is an unsupported html element that is not listed below but you would like to use, then do the following:

    1) navigate to and open the file, references.py
    2) say the name of the new element you would like to use is called foo_element.
        Then put this line anywhere in the references.py file above line 3:
###

    lookup[foo_element] = {"attributes": [attr_1, attr_2, ..., attr_N],
                           "required": [req_1, req_2, ..., req_M]}

where

$\left(attr_i\right)_{i=1}^{N}$ are the attributes of the element and 

$\left(req_j\right)_{j=1}^{M}$ are the required attributes of the element.
Now simply run
    
    python3 references.py && python3 tags.py
        
in the terminal and you are good to go to use that new element!
    

## Tags supported

- html
- meta
- link
- script
- a
- img
- form
- input
- button
- label
- textarea
- select
- option
- iframe
- audio
- video
- div
- header
- nav
- main
- section
- article
- footer
- p
- span
- h1
- h2
- h3
- h4
- h5
- h6

Please refer to lookup.json for more details.
