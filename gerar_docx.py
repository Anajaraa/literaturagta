# -*- coding: utf-8 -*-
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

ACCENT = RGBColor(0x7C, 0x3A, 0xED)
GOOD = RGBColor(0x0E, 0x9F, 0x5F)
GOLD = RGBColor(0xB4, 0x69, 0x0E)
MUTED = RGBColor(0x5E, 0x52, 0x72)
DARK = RGBColor(0x24, 0x1C, 0x33)

doc = Document()

style = doc.styles["Normal"]
style.font.name = "Calibri"
style.font.size = Pt(11)
style.font.color.rgb = DARK


def set_cell_shading(cell, color_hex):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), color_hex)
    cell._tc.get_or_add_tcPr().append(shd)


def add_box(doc_, title, body_lines, color=ACCENT):
    p = doc_.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    run = p.add_run(title)
    run.bold = True
    run.font.color.rgb = color
    for line in body_lines:
        bp = doc_.add_paragraph(line)
        bp.paragraph_format.left_indent = Inches(0.15)
    doc_.add_paragraph()


def add_poem(doc_, lines, credit):
    for line in lines:
        p = doc_.add_paragraph(line)
        p.paragraph_format.left_indent = Inches(0.3)
        p.runs[0].italic = True
    cp = doc_.add_paragraph(credit)
    cp.paragraph_format.left_indent = Inches(0.3)
    cp.runs[0].italic = True
    cp.runs[0].font.size = Pt(9)
    cp.runs[0].font.color.rgb = MUTED
    doc_.add_paragraph()


def add_recall(doc_, text):
    p = doc_.add_paragraph()
    run = p.add_run("FIXOU: ")
    run.bold = True
    run.font.color.rgb = GOOD
    p.add_run(text)
    p.paragraph_format.space_after = Pt(16)


def add_table(doc_, rows):
    table = doc_.add_table(rows=1, cols=len(rows[0]))
    table.style = "Light Grid Accent 1"
    hdr = table.rows[0].cells
    for i, h_ in enumerate(rows[0]):
        hdr[i].text = h_
    for row in rows[1:]:
        cells = table.add_row().cells
        for i, val in enumerate(row):
            cells[i].text = val
    doc_.add_paragraph()


# ---------- COVER ----------
title = doc.add_heading("Modernismo Brasileiro em 2 Horas", level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub = doc.add_paragraph(
    "Da Revolução de 30 ao Concretismo: guia de estudo com imagens mentais, "
    "exemplos concretos e um atalho mental"
)
sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub.runs[0].italic = True
sub.runs[0].font.color.rgb = MUTED
doc.add_paragraph()
info = doc.add_paragraph("7 módulos · ~15 min cada · 1 atalho mental · quiz online linkado ao final")
info.alignment = WD_ALIGN_PARAGRAPH.CENTER
info.runs[0].font.color.rgb = MUTED
doc.add_page_break()

# ---------- TOC ----------
doc.add_heading("Roteiro dos 120 minutos", level=1)
toc_items = [
    "1. Contexto histórico (1930-1945)",
    "2. Prosa Modernista: o que é",
    "3. Os cinco romancistas e suas obras",
    "4. Poesia: as quatro fases de Drummond",
    "5. Cecília Meireles e Vinícius de Moraes",
    "6. Concretismo: a poesia-objeto",
    "7. Terceiro Momento e intertextualidade",
    "8. Atalho mental: A Festa, a Ressaca e o Espelho",
    "9. Link do quiz online",
]
for it in toc_items:
    doc.add_paragraph(it, style="List Number")
doc.add_page_break()


def module(num, title_, tag, intro_paras, image_text, example_paras, compare_text, recall_text, compare_table=None):
    doc.add_heading(f"{num}. {title_}", level=1)
    tagp = doc.add_paragraph(tag)
    tagp.runs[0].italic = True
    tagp.runs[0].font.color.rgb = MUTED

    for para in intro_paras:
        doc.add_paragraph(para)

    add_box(doc, "Imagem mental", [image_text], ACCENT)
    add_box(doc, "Exemplo concreto", example_paras, GOOD)

    if compare_table:
        cp = doc.add_paragraph()
        cr = cp.add_run("Comparação simples")
        cr.bold = True
        cr.font.color.rgb = GOLD
        add_table(doc, compare_table)
    else:
        add_box(doc, "Comparação simples", [compare_text], GOLD)

    add_recall(doc, recall_text)
    doc.add_paragraph()


# Module 1
module(
    1, "Contexto histórico (1930-1945)",
    "Antes de decorar autores e obras, entenda por que a literatura brasileira muda de tom depois de 1930.",
    [
        "A 2ª Fase do Modernismo nasce junto com a Revolução de 1930, que derruba a República Velha e coloca "
        "Getúlio Vargas no poder. É uma década de grandes transformações: crescimento das cidades, "
        "industrialização, urbanização acelerada, e forte influência das ideias socialistas e marxistas, além do "
        "clima tenso das guerras mundiais. A literatura responde buscando um texto mais profundo, crítico e "
        "voltado para a realidade brasileira."
    ],
    "Pense na 1ª Fase (1922) como uma festa de estreia: todo mundo quebrando regras, rindo da tradição, testando "
    "formas novas só para provar que dava para fazer diferente. A 2ª Fase é a ressaca pensativa depois da festa: "
    "a euforia passa, e os escritores olham ao redor — o sertão com fome, o operário explorado, o indivíduo "
    "perdido — e decidem usar aquela liberdade de forma conquistada em 22 para contar essas histórias com "
    "profundidade.",
    [
        "Enquanto Mário de Andrade e Oswald de Andrade, em 1922, provocavam o público com manifestos e "
        "poemas-piada, autores da década de 1930 como Graciliano Ramos escreviam romances como Vidas Secas "
        "(1938): sem humor nenhum, só a seca, a fome e o silêncio de uma família de retirantes. É a mesma "
        "liberdade formal da Semana de 22, usada para um projeto completamente diferente.",
    ],
    None,
    "1ª Fase quebrou a forma; 2ª Fase usou a forma já quebrada para aprofundar o conteúdo — o ser humano e o "
    "Brasil real.",
    compare_table=[
        ["1ª Fase (1922)", "2ª Fase (1930-1945)"],
        ["Ruptura com o passado", "Aprofundamento psicológico e social"],
        ["Experimentação formal", "Visão crítica e analítica da sociedade"],
        ["Humor e irreverência", "Linguagem mais elaborada e, às vezes, intimista"],
        ["Linguagem livre e coloquial", "Temas existenciais e humanos"],
    ],
)

# Module 2
module(
    2, "Prosa Modernista: o que é e suas características",
    "O romance de 30 muda de foco: da experimentação para a psicologia e a crítica social.",
    [
        "A Prosa Modernista da 2ª Fase aprofunda a renovação iniciada na Semana de 22, com foco na exploração do "
        "ser humano, de seus conflitos internos e da realidade brasileira, usando linguagem mais complexa e "
        "experimental."
    ],
    "Imagine uma câmera que, na 1ª Fase, filmava só a superfície das coisas — rápida, engraçada, irreverente. Na "
    "2ª Fase, essa câmera entra dentro da cabeça dos personagens: mostra o monólogo interior, o fluxo de "
    "consciência, os flashbacks. Ao mesmo tempo, ela também aponta para fora, para a miséria e a desigualdade "
    "social, como um documentário crítico.",
    [
        "Em Vidas Secas, Graciliano Ramos narra a história de Fabiano e sua família, retirantes que fogem da "
        "seca no sertão nordestino. A linguagem seca imita a vida seca dos personagens, e o narrador mergulha nos "
        "pensamentos confusos e quase sem vocabulário de Fabiano, mostrando sua humanidade negada pela miséria.",
    ],
    "É a diferença entre uma foto de turista (bonita, rápida, de fora) e uma reportagem investigativa (que entra "
    "na vida das pessoas, mostra o contexto social, demora para contar a história toda). A prosa de 30 troca a "
    "foto de turista da 1ª Fase pela reportagem investigativa.",
    "características centrais — aprofundamento psicológico, crítica social, narrativas não lineares (monólogo "
    "interior, fluxo de consciência) e regionalismo voltado ao Brasil profundo.",
)

# Module 3
doc.add_heading("3. Os cinco grandes romancistas e suas obras", level=1)
tagp = doc.add_paragraph("Decore o \"mapa\" abaixo — é a parte que mais cai em prova de múltipla escolha.")
tagp.runs[0].italic = True
tagp.runs[0].font.color.rgb = MUTED
add_table(doc, [
    ["Autor", "Marca registrada", "Obras principais"],
    ["Mário de Andrade", "Explorou o Brasil urbano e suas contradições",
     "Macunaíma (1928), Amar, verbo intransitivo (1927), Contos novos (1947)"],
    ["Graciliano Ramos", "Sertão nordestino e condição humana",
     "Vidas secas (1938), São Bernardo (1934), Angústia (1936)"],
    ["Rachel de Queiroz", "Visão crítica e feminina da sociedade, foco no Nordeste",
     "O quinze (1930), João Miguel (1932), Caminho de pedras (1937)"],
    ["José Lins do Rego", "Ciclo da cana-de-açúcar: vida nos engenhos e relações de poder",
     "Menino de engenho (1932), Doidinho (1933), Bangüê (1934), Usina (1936)"],
    ["Érico Veríssimo", "Formação do Rio Grande do Sul e conflitos humanos",
     "Clarissa (1933), Caminhos cruzados (1935), O tempo e o vento (1949-1962)"],
])
add_box(doc, "Imagem mental", [
    "Pense em cada autor como dono de um \"território\" literário: Graciliano é dono do sertão seco, José Lins do "
    "Rego é dono do engenho de cana, Rachel de Queiroz é dona do Nordeste visto por uma mulher, Érico Veríssimo é "
    "dono do Rio Grande do Sul, e Mário de Andrade transita pelo Brasil urbano e mestiço de Macunaíma.",
], ACCENT)
add_box(doc, "Exemplo concreto", [
    "Se uma questão descrever \"romance que acompanha o ciclo de vida de um engenho de cana-de-açúcar, narrado "
    "por um menino que observa a decadência da aristocracia rural\", a resposta quase certamente é José Lins do "
    "Rego — provavelmente Menino de engenho, o primeiro do seu ciclo.",
], GOOD)
add_recall(doc, "associe autor → região/tema → título mais famoso. É o \"atalho\" mais usado em prova de "
                "múltipla escolha sobre esse período.")
doc.add_paragraph()

# Module 4
doc.add_heading("4. Poesia: as quatro fases de Carlos Drummond de Andrade", level=1)
tagp = doc.add_paragraph("Drummond é o nome mais citado da poesia modernista — sua obra se divide em quatro "
                          "momentos bem distintos.")
tagp.runs[0].italic = True
tagp.runs[0].font.color.rgb = MUTED
doc.add_paragraph(
    "Drummond atravessa décadas de poesia sem se repetir. Sua obra costuma ser dividida em quatro fases: Gauche "
    "(individualismo e ironia), Social (poesia como instrumento de luta), Reflexiva/Metafísica (análise de temas "
    "universais e existenciais) e do Tempo e Memória (infância, pai, terra natal)."
)
add_box(doc, "Imagem mental", [
    "Imagine quatro fotos da mesma pessoa em quatro décadas: jovem irônico e deslocado (\"gauche na vida\"), "
    "depois engajado gritando contra a injustiça ao lado do povo, depois um filósofo calado pensando sobre a "
    "existência, e por fim um senhor revisitando com carinho a infância em Itabira.",
], ACCENT)
p = doc.add_paragraph()
r = p.add_run("Exemplo concreto: \"Quadrilha\"")
r.bold = True
r.font.color.rgb = GOOD
add_poem(doc, [
    "João amava Teresa que amava Raimundo",
    "que amava Maria que amava Joaquim que amava Lili",
    "que não amava ninguém.",
    "João foi para os Estados Unidos, Teresa para o convento,",
    "Raimundo morreu de desastre, Maria ficou para tia,",
    "Joaquim suicidou-se e Lili casou com J. Pinto Fernandes,",
    "que não tinha entrado na história.",
], "Carlos Drummond de Andrade, \"Quadrilha\" (fase Gauche)")
doc.add_paragraph(
    "O poema monta uma corrente de amores não correspondidos — cada um ama quem ama outra pessoa — até que Lili, "
    "a única que \"não amava ninguém\", quebra o ciclo ao se casar com um estranho que nem fazia parte da "
    "história. É ironia pura, típica da fase Gauche."
)
doc.add_paragraph()
cp = doc.add_paragraph()
cr = cp.add_run("Comparação simples")
cr.bold = True
cr.font.color.rgb = GOLD
add_table(doc, [
    ["Fase", "Marca", "Obra-exemplo"],
    ["Gauche", "Individualismo, ironia, desajuste com o mundo", "Alguma Poesia (inclui \"Quadrilha\")"],
    ["Social", "Poesia engajada, instrumento de luta política", "A Rosa do Povo"],
    ["Reflexiva", "Temas universais, existenciais e filosóficos", "Claro Enigma"],
    ["Tempo e Memória", "Infância, pai, terra natal", "Boitempo"],
])
add_recall(doc, "se a questão citar \"luta/povo\" pense Fase Social; se citar \"infância/Itabira/pai\" pense "
                "Tempo e Memória; se for ironia sobre o indivíduo deslocado, é Fase Gauche.")
doc.add_paragraph()

# Module 5
doc.add_heading("5. Cecília Meireles e Vinícius de Moraes", level=1)
tagp = doc.add_paragraph("Duas vozes líricas e intimistas da mesma geração — uma mais simbólica, outra mais "
                          "musical.")
tagp.runs[0].italic = True
tagp.runs[0].font.color.rgb = MUTED
doc.add_paragraph(
    "Cecília Meireles é a grande voz da poesia intimista: trabalha símbolos como o mar, o tempo e a fugacidade "
    "das coisas, numa linguagem fluida e musical. Além da lírica pura (Viagem, Vaga Música, Cânticos), escreveu "
    "também uma obra de natureza histórica, o Romanceiro da Inconfidência, sobre a Inconfidência Mineira."
)
p = doc.add_paragraph()
r = p.add_run("Exemplo concreto: Cecília Meireles")
r.bold = True
r.font.color.rgb = GOOD
add_poem(doc, [
    "Encostei-me em ti, sabendo que eras somente onda.",
    "Sabendo bem que eras nuvem, depus a minha vida em ti.",
    "Como sabia bem tudo isso, e dei-me ao teu destino frágil,",
    "Fiquei sem poder chorar, quando caí.",
], "Cecília Meireles")
doc.add_paragraph(
    "O fragmento mostra consciência da fugacidade e da fragilidade do amor: o eu lírico sabia desde o início que "
    "aquilo em que se apoiava era instável (\"onda\", \"nuvem\"), e mesmo assim se entregou."
)
doc.add_paragraph(
    "Vinícius de Moraes transita entre a poesia clássica (sonetos rigorosos) e a popularidade da música: em "
    "parceria com Tom Jobim, compôs \"Garota de Ipanema\", um dos maiores símbolos da Bossa Nova. Mas também é "
    "autor de sonetos densos como o \"Soneto de Fidelidade\"."
)
p = doc.add_paragraph()
r = p.add_run("Exemplo concreto: \"Soneto de Fidelidade\"")
r.bold = True
r.font.color.rgb = GOOD
add_poem(doc, [
    "De tudo, ao meu amor serei atento",
    "Antes, e com tal zelo, e sempre, e tanto",
    "Que mesmo em face do maior encanto",
    "Dele se encante mais meu pensamento.",
    "(...)",
    "Eu possa me dizer do amor (que tive):",
    "Que não seja imortal, posto que é chama",
    "Mas que seja infinito enquanto dure.",
], "Vinícius de Moraes, \"Soneto de Fidelidade\"")
doc.add_paragraph(
    "O sentimento central é o amor, vivido com zelo nos \"louvores\" e nos \"risos\" — nos bons e nos maus "
    "momentos. O verso final resolve a aparente contradição: o amor não precisa durar para sempre para ser "
    "verdadeiro; a chama só precisa ser intensa enquanto existir — a fidelidade está na intensidade, não na "
    "duração."
)
doc.add_paragraph()
add_box(doc, "Comparação simples", [
    "Cecília Meireles é como observar o mar de longe, pensando sobre o tempo que passa — contemplativa e "
    "simbólica. Vinícius de Moraes é como alguém que ora escreve um poema clássico rigoroso, ora pega o violão e "
    "compõe uma canção que o Brasil inteiro canta — o mesmo lirismo, em dois formatos diferentes.",
], GOLD)
add_recall(doc, "Cecília = símbolos, fugacidade, Romanceiro da Inconfidência. Vinícius = soneto clássico + Bossa "
                "Nova (Garota de Ipanema, com Tom Jobim).")
doc.add_paragraph()
doc.add_page_break()

# Module 6
module(
    6, "Concretismo: a poesia-objeto",
    "Quando a forma visual do poema vira tão importante quanto (ou mais que) as palavras.",
    [
        "O Concretismo surge no Brasil em 1956, com a publicação da revista Noigandres. Foi representado e "
        "idealizado por Haroldo de Campos, Augusto de Campos e Décio Pignatari. O movimento radicaliza a proposta "
        "de valorização da forma na poesia, tratando o poema quase como um objeto visual e sonoro na sociedade "
        "moderna."
    ],
    "Pense num poema tradicional como uma carta: você lê linha por linha, em ordem, do começo ao fim. O poema "
    "concretista é mais como um cartaz publicitário ou um logotipo: o significado nasce também do espaço em "
    "branco, do tamanho da letra, da posição da palavra na página.",
    [
        "Um poema concretista famoso é \"Velocidade\", de Augusto de Campos: a própria disposição das letras na "
        "página imita visualmente a ideia de aceleração. A forma vira parte do conteúdo.",
    ],
    "É a diferença entre ouvir uma música no rádio (só o som) e assistir ao videoclipe (som + imagem + edição "
    "trabalhando juntos para o mesmo efeito). O Concretismo faz a poesia \"ganhar videoclipe\".",
    "Concretismo = 1956 + revista Noigandres + Haroldo de Campos, Augusto de Campos e Décio Pignatari + poema "
    "como objeto visual/espacial.",
)

# Module 7
module(
    7, "O Terceiro Momento e a intertextualidade",
    "A prosa depois de 1945 — e como textos antigos continuam \"conversando\" com a cultura pop de hoje.",
    [
        "O chamado Terceiro Momento tem início, aproximadamente, em 1945, atravessando várias décadas até os dias "
        "atuais — por isso costuma ser chamado de tendências contemporâneas. Autores como Clarice Lispector, "
        "Lygia Fagundes Telles, Nélida Piñon, Marina Colasanti e Raduan Nassar mergulham no universo psicológico "
        "das personagens, em narrativas marcadas pelo fluxo de consciência e pelo intimismo."
    ],
    "Se a prosa de 1930 já tinha \"entrado na cabeça\" dos personagens, o Terceiro Momento fecha a porta do "
    "quarto e apaga a luz do corredor: quase toda a ação acontece dentro da mente da personagem, em pensamentos "
    "fragmentados, epifanias súbitas e silêncios.",
    [
        "Em 2025, uma cena da novela Vale Tudo, com a personagem Odete Roitman, viralizou com a fala: \"Solange "
        "que amava Afonso, que amava Fátima, que amava Cesar, que agora me ama. Só a pobre da Celina que ficou de "
        "fora dessa história.\" A frase dialoga diretamente com \"Quadrilha\", de Drummond, repetindo sua "
        "estrutura de corrente de amores não correspondidos. Esse diálogo consciente entre dois textos é chamado "
        "de intertextualidade (aqui, no formato de paródia, por seu tom irônico).",
    ],
    "Intertextualidade é como um \"sample\" numa música: o artista novo usa um trecho reconhecível de uma música "
    "antiga para criar algo novo, contando com que o ouvinte identifique a referência.",
    "Terceiro Momento = contemporaneidade + intimismo + fluxo de consciência. Intertextualidade = diálogo "
    "consciente entre dois textos (paródia, quando o tom é irônico/crítico).",
)
doc.add_page_break()

# ---------- MNEMONIC ----------
doc.add_heading("8. Atalho mental: \"A Festa, a Ressaca e o Espelho\"", level=1)
doc.add_paragraph("Para lembrar de tudo acima em 10 segundos, imagine esta historinha sempre que ler uma questão "
                   "sobre esse período:")

story = [
    ("🎉 A festa (1922):", "a 1ª Fase quebra tudo, experimenta a forma, ri da tradição."),
    ("😔📖 A ressaca pensativa (1930-1945):", "a 2ª Fase usa essa liberdade para olhar pra dentro (psicologia) e "
     "pra fora (crítica social) — Graciliano no sertão, José Lins do Rego no engenho, Drummond passando da ironia "
     "Gauche ao engajamento Social, Cecília e Vinícius cantando o amor que passa."),
    ("🔲✨ O poema vira objeto (1956):", "o Concretismo transforma a própria página em imagem — a forma grita tão "
     "alto quanto as palavras."),
    ("🪞🤫 O espelho interior (depois de 1945):", "o Terceiro Momento fecha a porta do quarto e narra de dentro "
     "da mente — intimismo e fluxo de consciência, numa literatura tão contemporânea que ainda hoje \"conversa\" "
     "com novelas e redes sociais (intertextualidade)."),
]
for lead, rest in story:
    p = doc.add_paragraph()
    r1 = p.add_run(lead + " ")
    r1.bold = True
    r1.font.color.rgb = ACCENT
    p.add_run(rest)

doc.add_paragraph()
add_recall(doc, "\"Quebrou a forma em 22, aprofundou o conteúdo em 30, virou objeto em 56, e foi morar dentro da "
                "mente depois disso — e ainda hoje dialoga com o presente.\"")

doc.add_page_break()

# ---------- QUIZ LINK ----------
doc.add_heading("9. Quiz online", level=1)
doc.add_paragraph(
    "O quiz inteligente com 16 perguntas, correção automática, explicação dos erros e exemplos extras está "
    "disponível online:"
)
linkp = doc.add_paragraph()
lr1 = linkp.add_run("Guia de estudo: ")
lr1.bold = True
linkp.add_run("https://literaturagta.vercel.app/")
linkp2 = doc.add_paragraph()
lr2 = linkp2.add_run("Quiz: ")
lr2.bold = True
linkp2.add_run("https://literaturagta.vercel.app/quiz.html")
doc.add_paragraph()
p = doc.add_paragraph()
r = p.add_run("Dica: ")
r.bold = True
p.add_run("faça o quiz logo após terminar de ler este guia, enquanto o conteúdo ainda está fresco. Erros no quiz "
          "indicam exatamente qual módulo deste documento você deve reler.")

doc.save("Literatura_Guia_de_Estudo.docx")
print("OK: Literatura_Guia_de_Estudo.docx gerado")
