import wikipedia

user_search = input("Wikipedia page title or search phrase: ")
while user_search != "":
    wiki_page = wikipedia.page(user_search)
    print(wiki_page.title)
    print(wikipedia.summary(user_search))
    print(wiki_page.url)
    user_search = input("Wikipedia page title or search phrase: ")


    # Could not get expection clause operational
    # try:
    #     wiki_page = wikipedia.page(user_search))
    # except wikipedia.exceptions.DisambiguationError as e:
    #     print(e.options)

