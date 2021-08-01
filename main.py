from reportlab.pdfgen import canvas as cv
from reportlab.lib.pagesizes import A4


nomeArquivo = ('primeiro-teste.pdf')
tituloPdf = ('Titulo do PDF')
titulo = ('Primeiro Titulo')
primeiraLinha = ('Primeira linha: ')
baseMilimetrosParaPontos = 0.352777
logo = ('tux.png')

def mp(mm):
    return mm/baseMilimetrosParaPontos

def criaPDF():
    try:
        file = cv.Canvas(nomeArquivo,pagesize=A4)
        file.setTitle(tituloPdf)
        file.drawCentredString(mp(100), mp(290), titulo)
        file.drawImage(logo, mp(190),mp(275), width=50, height=50)
        file.drawString(mp(5), mp(260), primeiraLinha)
        file.save()
    except Exception as e:
        print(e)
        return
    print('PDF criado com sucesso')

criaPDF()
