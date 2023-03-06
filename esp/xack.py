import mechanicalsoup as ms

browser = ms.Browser()

url = "https://id.egov.uz"

page = browser.get(url)

soup = page.soup

form = soup.select("from")[0]

form.select("input")[2]["value"] = "m2220134@gmail.com"
form.select("input")[2]["value"] = "muhammad_1507"

profile = browser.submit(form, page.url)

print(profile.url)