const QUESTIONS = [
  {
    tag: "Módulo 1 · Contexto histórico",
    q: "Qual evento histórico marca o início da 2ª Fase do Modernismo brasileiro, por volta de 1930?",
    options: [
      "A Semana de Arte Moderna de 1922",
      "A Revolução de 1930, que encerra a República Velha e leva Getúlio Vargas ao poder",
      "O fim da Segunda Guerra Mundial",
      "A fundação da revista Noigandres",
    ],
    correct: 1,
    explain: "A 2ª Fase do Modernismo nasce no contexto da Revolução de 1930, que derruba a República Velha e inicia a era Vargas — um período de grandes transformações sociais, urbanização e industrialização que empurra a literatura para temas mais críticos e profundos.",
    example: "É o mesmo raciocínio do guia: a 1ª Fase (1922) foi a 'festa' de ruptura formal; a 2ª Fase (1930) é a 'ressaca pensativa' que usa essa liberdade para olhar a realidade brasileira com mais seriedade.",
  },
  {
    tag: "Módulo 1 · 1ª x 2ª Fase",
    q: "O que diferencia principalmente a 2ª Fase (1930–1945) da 1ª Fase (1922) do Modernismo?",
    options: [
      "A 2ª Fase abandona completamente a língua portuguesa coloquial",
      "A 2ª Fase aprofunda o conteúdo psicológico e social, enquanto a 1ª Fase focou em romper a forma",
      "A 2ª Fase não teve nenhum romancista importante",
      "A 2ª Fase é anterior à 1ª Fase",
    ],
    correct: 1,
    explain: "A 1ª Fase (1922) foi marcada pela ruptura com o passado e pela experimentação formal, com humor e irreverência. A 2ª Fase (1930-1945) aprofunda o conteúdo: visão crítica e analítica da sociedade, linguagem mais elaborada e temas existenciais e humanos.",
    example: "Pense na tabela do Módulo 1: a mesma liberdade de forma conquistada em 22 é usada, em 30, para contar histórias como a de Fabiano em Vidas Secas, bem mais sérias que os poemas-piada da Semana de 22.",
  },
  {
    tag: "Módulo 2 · Prosa Modernista",
    q: "Quais são características centrais da prosa da 2ª Fase do Modernismo?",
    options: [
      "Humor, irreverência e poemas-piada, sem nenhuma crítica social",
      "Aprofundamento psicológico das personagens, crítica social e narrativas não lineares (monólogo interior, fluxo de consciência)",
      "Uso exclusivo de versos livres sem nenhuma prosa",
      "Rejeição total de qualquer regionalismo",
    ],
    correct: 1,
    explain: "A prosa de 30 se caracteriza pelo aprofundamento psicológico, pela visão crítica da sociedade, pela denúncia das desigualdades sociais, pela linguagem mais elaborada e intimista, e pelo uso de narrativas não lineares, além do forte regionalismo.",
    example: "É o exemplo de Vidas Secas: a linguagem seca imita a vida seca dos personagens, e o narrador mergulha nos pensamentos confusos de Fabiano — psicologia e crítica social andando juntas.",
  },
  {
    tag: "Módulo 3 · Autores e obras",
    q: "Qual autor é conhecido pelo 'ciclo da cana-de-açúcar', retratando a vida nos engenhos e as relações de poder, começando pelo romance 'Menino de engenho'?",
    options: [
      "Graciliano Ramos",
      "Érico Veríssimo",
      "José Lins do Rego",
      "Mário de Andrade",
    ],
    correct: 2,
    explain: "José Lins do Rego é o criador do ciclo da cana-de-açúcar, composto por romances como Menino de engenho (1932), Doidinho (1933), Bangüê (1934) e Usina (1936), que acompanham a decadência da aristocracia rural dos engenhos.",
    example: "Lembre do 'mapa' do Módulo 3: cada romancista tem um território — Graciliano é o sertão seco, José Lins do Rego é o engenho de cana, Érico Veríssimo é o Rio Grande do Sul.",
  },
  {
    tag: "Módulo 3 · Autores e obras",
    q: "'Vidas Secas' e 'São Bernardo', romances marcados pelo retrato do sertão nordestino e da condição humana, são obras de:",
    options: [
      "Rachel de Queiroz",
      "Graciliano Ramos",
      "José Lins do Rego",
      "Érico Veríssimo",
    ],
    correct: 1,
    explain: "Graciliano Ramos retratou com profundidade o sertão nordestino e a condição humana em romances como Vidas secas (1938), São Bernardo (1934) e Angústia (1936).",
    example: "Rachel de Queiroz também escreve sobre o Nordeste, mas com um olhar crítico e feminino, em obras como O quinze (1930) — personagem e autor não devem ser confundidos.",
  },
  {
    tag: "Módulo 4 · Fases de Drummond",
    q: "O poema 'Quadrilha', de Carlos Drummond de Andrade, que narra uma corrente irônica de amores não correspondidos, pertence a qual fase do poeta?",
    options: [
      "Fase Social (poesia engajada)",
      "Fase Gauche (individualismo e ironia)",
      "Fase Reflexiva (temas metafísicos)",
      "Fase do Tempo e Memória (infância e terra natal)",
    ],
    correct: 1,
    explain: "'Quadrilha' pertence à fase Gauche de Drummond, marcada pelo individualismo e pela ironia — o poema trata o amor romântico quase como uma brincadeira de roda que termina sem nenhum final feliz de verdade.",
    example: "A fase Social seria algo como A Rosa do Povo (poesia como instrumento de luta); a fase do Tempo e Memória seria Boitempo (lembranças de Itabira e do pai).",
  },
  {
    tag: "Módulo 4 · Interpretação de poema",
    q: "Em 'Quadrilha', todos os personagens amam alguém que ama outra pessoa, formando uma corrente de amores não correspondidos. Quem rompe esse ciclo, e como?",
    options: [
      "João, ao ir para os Estados Unidos",
      "Raimundo, ao morrer de desastre",
      "Lili, que não amava ninguém e casa com J. Pinto Fernandes, que não tinha entrado na história",
      "Teresa, ao entrar para o convento",
    ],
    correct: 2,
    explain: "Lili é a única que 'não amava ninguém' dentro da corrente de amores do poema. Ironicamente, é ela quem 'quebra' o ciclo ao se casar com alguém completamente externo à história (J. Pinto Fernandes), enquanto todos os outros personagens terminam de forma trágica ou dispersa.",
    example: "É esse tipo de ironia — o amor tratado com um distanciamento quase cômico — que caracteriza a fase Gauche de Drummond.",
  },
  {
    tag: "Módulo 5 · Cecília Meireles",
    q: "Além de sua poesia lírica e simbólica, Cecília Meireles também escreveu uma obra de natureza histórica sobre a Inconfidência Mineira, intitulada:",
    options: [
      "Vaga Música",
      "Viagem",
      "Romanceiro da Inconfidência",
      "Cânticos",
    ],
    correct: 2,
    explain: "O Romanceiro da Inconfidência é a obra de Cecília Meireles de natureza histórica, que narra episódios da Inconfidência Mineira. Viagem, Vaga Música e Cânticos são obras da sua lírica intimista e simbólica.",
    example: "É um bom exemplo de como um mesmo autor pode transitar entre a poesia intimista (símbolos como o mar e o tempo) e um projeto histórico-narrativo mais amplo.",
  },
  {
    tag: "Módulo 5 · Interpretação de poema",
    q: "No fragmento de Cecília Meireles 'Encostei-me em ti, sabendo que eras somente onda... Fiquei sem poder chorar, quando caí', o tema central é:",
    options: [
      "O gosto pelas coisas antigas e a serenidade do amor",
      "A consciência da fugacidade e da fragilidade do amor",
      "A predileção pela cor branca e o elogio ao amor",
      "A sensação do vago e a consciência da perenidade do amor",
    ],
    correct: 1,
    explain: "O eu lírico já sabia, desde o início, que aquilo em que se apoiava era instável ('onda', 'nuvem') — por isso, quando a queda chega, não há nem espaço para choro, só a aceitação de algo que já se sabia passageiro e frágil.",
    example: "Note a diferença da última opção: o poema fala de fugacidade (o oposto de perenidade) — um erro comum é confundir 'consciência do vago' com 'consciência da duração eterna'.",
  },
  {
    tag: "Módulo 5 · Vinícius de Moraes",
    q: "Vinícius de Moraes escreveu, em parceria com Tom Jobim, uma composição símbolo da Bossa Nova, intitulada:",
    options: [
      "Tempo e Eternidade",
      "Forma e Exegese",
      "Garota de Ipanema",
      "O Amor Natural",
    ],
    correct: 2,
    explain: "'Garota de Ipanema' é a parceria mais famosa entre Vinícius de Moraes e Tom Jobim, e um dos maiores símbolos da Bossa Nova no mundo todo.",
    example: "Isso mostra a dupla identidade de Vinícius: poeta de sonetos clássicos rigorosos (como o Soneto de Fidelidade) e, ao mesmo tempo, letrista popular de canções.",
  },
  {
    tag: "Módulo 5 · Soneto de Fidelidade",
    q: "No verso final do 'Soneto de Fidelidade' — 'Que não seja imortal, posto que é chama, Mas que seja infinito enquanto dure' —, a ideia central é que o amor:",
    options: [
      "Precisa durar para sempre para ser considerado verdadeiro",
      "Não precisa ser eterno; a fidelidade está na intensidade vivida enquanto o sentimento existir",
      "É impossível de sustentar, por isso deve ser evitado",
      "Só tem valor se for correspondido imediatamente",
    ],
    correct: 1,
    explain: "A metáfora da 'chama' indica algo intenso mas não necessariamente permanente. O poeta resolve a aparente contradição dizendo que o amor não precisa ser imortal — basta ser vivido de forma plena e infinita enquanto durar.",
    example: "No poema, o eu lírico já havia dito que se dedicaria ao amor 'nos louvores' e 'nos risos' — ou seja, nos bons e nos maus momentos —, reforçando que a fidelidade é sobre intensidade, não sobre duração garantida.",
  },
  {
    tag: "Módulo 6 · Concretismo",
    q: "O Concretismo surge no Brasil em 1956, com a publicação de qual revista, e tendo quais nomes como seus principais idealizadores?",
    options: [
      "Revista Noigandres, com Haroldo de Campos, Augusto de Campos e Décio Pignatari",
      "Revista Klaxon, com Mário de Andrade e Oswald de Andrade",
      "Revista Noigandres, com Carlos Drummond de Andrade e Cecília Meireles",
      "Revista Klaxon, com Vinícius de Moraes e Tom Jobim",
    ],
    correct: 0,
    explain: "O Concretismo surgiu em 1956 com a revista Noigandres, representado e idealizado por Haroldo de Campos, Augusto de Campos e Décio Pignatari. A revista Klaxon, por outro lado, é associada à 1ª Fase do Modernismo, de 1922.",
    example: "Não confunda as revistas: Klaxon (1922) é da 1ª Fase modernista; Noigandres (1956) é do Concretismo, décadas depois.",
  },
  {
    tag: "Módulo 6 · Concretismo",
    q: "A principal radicalização proposta pelo Concretismo na poesia brasileira foi:",
    options: [
      "O retorno estrito às formas fixas, como o soneto clássico",
      "A valorização da forma visual e espacial do poema, tratando-o quase como um objeto",
      "A eliminação total de qualquer preocupação com a forma",
      "A substituição da poesia escrita por poesia apenas falada",
    ],
    correct: 1,
    explain: "O Concretismo radicaliza a proposta de valorização da forma na poesia moderna: o poema passa a ser tratado quase como um objeto visual, em que a disposição das palavras na página carrega parte do significado.",
    example: "É a ideia do 'poema-videoclipe' do guia: a mensagem não está só nas palavras, mas em como elas se organizam no espaço da página.",
  },
  {
    tag: "Módulo 7 · Terceiro Momento",
    q: "O chamado Terceiro Momento da literatura modernista brasileira, com início por volta de 1945 e autores como Clarice Lispector, Lygia Fagundes Telles e Raduan Nassar, é caracterizado principalmente por:",
    options: [
      "Narrativas lineares e sem nenhum aprofundamento psicológico",
      "Mergulho no universo psicológico das personagens, com fluxo de consciência e intimismo",
      "Exclusivamente poesia concretista, sem nenhuma prosa",
      "Retorno total às características da 1ª Fase de 1922",
    ],
    correct: 1,
    explain: "Apesar das diferenças estéticas entre os autores, o Terceiro Momento é marcado pelo mergulho no universo psicológico das personagens, revelando angústias, medos e frustrações em narrativas marcadas pelo fluxo de consciência e pelo intimismo.",
    example: "É um aprofundamento ainda maior do que já acontecia na prosa de 1930 (Módulo 2): a ação se desloca cada vez mais para dentro da mente das personagens.",
  },
  {
    tag: "Módulo 7 · Intertextualidade",
    q: "Uma cena de uma novela de 2025 reaproveita a estrutura do poema 'Quadrilha', de Drummond, criando uma corrente irônica de amores não correspondidos com nomes diferentes. Esse diálogo consciente entre os dois textos é chamado de:",
    options: [
      "Rima",
      "Intertextualidade",
      "Contexto",
      "Fluxo de consciência",
    ],
    correct: 1,
    explain: "Intertextualidade é o diálogo consciente entre dois textos, em que um se apropria da estrutura, do estilo ou do conteúdo do outro. Quando esse diálogo tem tom irônico ou crítico, como no caso da novela que recria 'Quadrilha', o recurso específico é chamado de paródia — um tipo de intertextualidade.",
    example: "É como um 'sample' numa música: o artista novo usa um trecho reconhecível de uma obra antiga, contando que o público identifique a referência e perceba o diálogo entre as duas.",
  },
  {
    tag: "Revisão geral",
    q: "Qual frase resume melhor a trajetória da literatura modernista brasileira do guia, da 1ª Fase ao Terceiro Momento?",
    options: [
      "Toda a literatura modernista é idêntica, sem nenhuma mudança ao longo do tempo",
      "Quebrou a forma em 1922, aprofundou o conteúdo em 1930, virou objeto visual em 1956, e foi morar dentro da mente das personagens depois disso",
      "O Modernismo terminou completamente em 1930 e não teve nenhum desdobramento posterior",
      "Apenas a poesia evoluiu; a prosa permaneceu sempre igual",
    ],
    correct: 1,
    explain: "Essa é a síntese do atalho mental do guia: ruptura formal (1922) → aprofundamento psicológico e social (1930–1945) → poema como objeto visual (Concretismo, 1956) → narrativas intimistas e de fluxo de consciência (Terceiro Momento, pós-1945).",
    example: "Volte à seção 'A Festa, a Ressaca e o Espelho' do guia de estudo sempre que precisar relembrar rápido essa linha do tempo antes de uma prova.",
  },
];

let current = 0;
let answers = new Array(QUESTIONS.length).fill(null);

const root = document.getElementById("quiz-root");
const progressBar = document.getElementById("progress-bar");
const resultsEl = document.getElementById("results");

function renderQuestion(index) {
  const item = QUESTIONS[index];
  const card = document.createElement("div");
  card.className = "module quiz-card active";
  card.innerHTML = `
    <span class="qtag">${item.tag} · Pergunta ${index + 1} de ${QUESTIONS.length}</span>
    <h3>${item.q}</h3>
    <div class="options">
      ${item.options.map((opt, i) => `<button class="option" data-i="${i}">${opt}</button>`).join("")}
    </div>
    <div class="feedback" id="feedback-${index}"></div>
    <div class="quiz-nav">
      <button class="btn ghost" id="prev-btn" type="button" ${index === 0 ? "disabled style='opacity:.4;cursor:default;'" : ""}>← Anterior</button>
      <button class="btn primary" id="next-btn" type="button" disabled style="opacity:.4;cursor:default;">${index === QUESTIONS.length - 1 ? "Ver resultado" : "Próxima →"}</button>
    </div>
  `;
  root.innerHTML = "";
  root.appendChild(card);

  const optionButtons = card.querySelectorAll(".option");
  const feedbackEl = card.querySelector(`#feedback-${index}`);
  const nextBtn = card.querySelector("#next-btn");
  const prevBtn = card.querySelector("#prev-btn");

  if (answers[index] !== null) {
    lockAnswer(optionButtons, feedbackEl, item, answers[index]);
    nextBtn.disabled = false;
    nextBtn.style.opacity = 1;
    nextBtn.style.cursor = "pointer";
  }

  optionButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      if (answers[index] !== null) return;
      const chosen = parseInt(btn.dataset.i, 10);
      answers[index] = chosen;
      lockAnswer(optionButtons, feedbackEl, item, chosen);
      nextBtn.disabled = false;
      nextBtn.style.opacity = 1;
      nextBtn.style.cursor = "pointer";
      updateProgress();
    });
  });

  nextBtn.addEventListener("click", () => {
    if (index === QUESTIONS.length - 1) {
      showResults();
    } else {
      current = index + 1;
      renderQuestion(current);
    }
  });

  if (prevBtn) {
    prevBtn.addEventListener("click", () => {
      current = index - 1;
      renderQuestion(current);
    });
  }

  updateProgress();
}

function lockAnswer(optionButtons, feedbackEl, item, chosen) {
  optionButtons.forEach((b) => (b.disabled = true));
  const correctBtn = optionButtons[item.correct];
  const chosenBtn = optionButtons[chosen];
  correctBtn.classList.add("correct");
  const isRight = chosen === item.correct;
  if (!isRight) chosenBtn.classList.add("incorrect");

  feedbackEl.classList.add("show", isRight ? "ok" : "no");
  feedbackEl.innerHTML = `
    <div class="verdict ${isRight ? "ok-text" : "no-text"}">${isRight ? "✅ Certo!" : "❌ Não é essa — vamos entender por quê."}</div>
    <div>${item.explain}</div>
    <div class="example"><b>Exemplo para fixar:</b> ${item.example}</div>
  `;
}

function updateProgress() {
  const answered = answers.filter((a) => a !== null).length;
  const pct = Math.round((answered / QUESTIONS.length) * 100);
  progressBar.style.width = pct + "%";
}

function showResults() {
  root.innerHTML = "";
  const score = answers.reduce((acc, a, i) => acc + (a === QUESTIONS[i].correct ? 1 : 0), 0);
  const pct = Math.round((score / QUESTIONS.length) * 100);

  resultsEl.classList.add("show");
  document.getElementById("score-ring").style.setProperty("--pct", pct);
  document.getElementById("score-text").textContent = `${score}/${QUESTIONS.length}`;

  let msg;
  if (score === QUESTIONS.length) msg = "Perfeito! Você dominou a 2ª Fase do Modernismo, o Concretismo e o Terceiro Momento. Releia só o atalho mental de vez em quando para manter fresco.";
  else if (score >= 12) msg = "Muito bom! Reveja no guia os módulos das perguntas erradas abaixo — são pontos pequenos de ajustar.";
  else if (score >= 7) msg = "Bom começo. Volte ao guia de estudo e releia com calma os módulos indicados abaixo antes de repetir o quiz.";
  else msg = "Sem problema — é bastante conteúdo novo. Releia o guia do início, focando nas imagens mentais e nos exemplos, e tente de novo.";
  document.getElementById("score-msg").textContent = msg;

  const reviewList = document.getElementById("review-list");
  reviewList.innerHTML = QUESTIONS.map((item, i) => {
    const isRight = answers[i] === item.correct;
    return `
      <div class="review-item ${isRight ? "right" : "wrong"}">
        <div style="font-weight:700; margin-bottom:4px;">${isRight ? "✅" : "❌"} ${item.tag}</div>
        <div style="margin-bottom:6px;">${item.q}</div>
        ${isRight ? "" : `<div style="color:var(--muted); font-size:0.92rem;"><b>Sua resposta:</b> ${item.options[answers[i]]}<br><b>Correta:</b> ${item.options[item.correct]}<br>${item.explain}</div>`}
      </div>
    `;
  }).join("");

  progressBar.style.width = "100%";
}

document.getElementById("retry-btn").addEventListener("click", () => {
  current = 0;
  answers = new Array(QUESTIONS.length).fill(null);
  resultsEl.classList.remove("show");
  renderQuestion(0);
  window.scrollTo({ top: 0, behavior: "smooth" });
});

renderQuestion(0);
