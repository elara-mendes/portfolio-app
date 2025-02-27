I can use Pandas too, to iterate the items from data like csv.

Example:

df = pandas.read_csv("data.csv", sep=";")

for index, row in df[:10].iterrows():
    print(row["title"])

form_message = f"Subject: (Topic)Teste\r\n\r\nMessage: {message}\r\nEmail: {sender}"
