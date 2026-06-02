# html-wrapper
wrappers for tags and document to write html in and upload to a json file for further use

# How to use:

The best feature of the html-wrapper library is that it is very flexible with unsupported html elements.

If there is an unsupported html element that is not listed below but you would like to use, then do the following:

    1) navigate to references.py and open the file
    2) say the name of the new element you would like to use is called foo_element.
        Then put this line anywhere in the references.py file above line 3:
            lookup[foo_element] = {"attributes": [$attr_1, attr_2, ..., attr_N$],
                                   "required": [$req_1, req_2, ..., req_M$]}
            
    

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
