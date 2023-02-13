import googlesearch
import newspaper
import pyttsx3

engine = pyttsx3.init()

while True:
    query = input("Enter your query: ")

    search_results = list(googlesearch.search(query, num_results=5000))
    
    # Skip Wikipedia search results and pick the second result instead
    search_results = [r for r in search_results if not r.startswith('https://en.wikipedia.org/')]
    if len(search_results) > 1:
        top_result = search_results[1]
        article = newspaper.Article(top_result)
        try:
            article.download()
            article.parse()
            print(article.text)
            engine.say(article.text)
            engine.runAndWait()
        except newspaper.ArticleException:
            print(f"Skipping '{top_result}' due to ArticleException")
    else:
        print(f"No article found for '{query}' in top 5 search results, excluding Wikipedia results.")
    
    # check if user wants to continue with another search
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != "y":
        break
