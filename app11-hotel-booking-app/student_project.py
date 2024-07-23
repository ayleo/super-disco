import pandas as pd
from fpdf import FPDF


df = pd.read_csv('articles.csv', dtype='str')


class Article:
    def __init__(self, article_id):
        self.article_id = article_id
        self.article_name = df.loc[df['id'] == article_id, 'name'].squeeze()
        self.article_price = df.loc[df['id'] == article_id, 'price'].squeeze()

        
    def Receipt(self):
        self.pdf = FPDF(orientation="P", unit="mm", format="A4")
        self.pdf.add_page()

        self.pdf.set_font(family="Times", size=16, style="B")
        self.pdf.cell(w=50, h=8, txt=f"Receipt nr.{article_id}", ln=1)
        
        self.pdf.set_font(family="Times", size=16, style="B")
        self.pdf.cell(w=50, h=8, txt=f"Article: {self.article_name}", ln=1)

        self.pdf.set_font(family="Times", size=16, style="B")
        self.pdf.cell(w=50, h=8, txt=f"Price: {self.article_price}", ln=1)
    
        self.pdf.output("receipt.pdf")

    def Quantity(self):
        df.loc[df['id'] == article_id, 'in stock'] = str(int(df.loc[df['id'] == article_id, 'in stock'].squeeze()) - 1)
        df.to_csv('articles.csv', index=False)
        print("Quantity updated successfully")


print(df)
article_id = input("Choose an article to buy: ")


article = Article(article_id)
article.Receipt()
article.Quantity()