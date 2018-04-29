import httplib2, re


def grabSiteTags(pageToSearch):
    grabHtmlTags = re.compile(
        '<title>(.{5,90})</title>|<summary>(.{5,300})</summary>|<link rel="alternate" type="text/html" href="(.{5,100})"/>',
        re.IGNORECASE)

    allTheTags = re.findall(grabHtmlTags, pageToSearch)

    for i in allTheTags:
        print(i[0].replace("\\'", "'") + i[1].replace("\\'", "'") + i[2].replace("\\'", "'") + "\n")

        getTheArticle(str(i[2]))


def getTheArticle(pageToSearch):
    if pageToSearch:

        i = httplib2.Http('.cache')
        content = i.request(pageToSearch)

        content = str(content)

        grabHtmlTags = re.compile('<div>.{1,40}<p>(.{1,800})', re.IGNORECASE)

        allTheArticle = re.findall(grabHtmlTags, content)

        allTheArticle = str(allTheArticle)

        if (len(allTheArticle) > 100):
            print("Article: " + allTheArticle.replace("\\\\'", "'").replace("\\n'", "").replace("\\'", "'").replace(
                "\\\\n", "").replace("\\\\t", ""))
        else:
            pass
        return


def main():
    urlToGet = "http://www.huffingtonpost.com/feeds/verticals/comedy/index.xml"

    h = httplib2.Http('.cache')
    content = h.request(urlToGet)

    grabSiteTags(str(content))


if __name__ == "__main__": main()
