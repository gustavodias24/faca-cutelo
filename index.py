<!doctype html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Cutelo Chef Grande em aço inox, com cabo inteiriço e bainha. Compre hoje e pague somente na entrega por Pix ou maquininha.">
    <meta name="theme-color" content="#17130f">
    <meta property="og:title" content="Cutelo Chef Grande — força e precisão no preparo">
    <meta property="og:description" content="Compre hoje, receba no dia seguinte e pague somente na entrega por Pix ou maquininha.">
    <meta property="og:image" content="{{ url_for('static', filename='images/hero-cutelo.webp', _external=True) }}">
    <title>Cutelo Chef Grande | Aço Inox Forjado à Mão</title>
    <link rel="preload" href="{{ url_for('static', filename='images/hero-cutelo.webp') }}" as="image" fetchpriority="high">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <style>
        .pay-highlight {
            max-width: 600px;
            display: grid;
            grid-template-columns: auto 1fr;
            gap: 18px;
            align-items: center;
            margin: 0 0 28px;
            padding: 18px 20px;
            border: 1px solid rgba(229, 138, 59, 0.52);
            border-radius: 4px;
            background: rgba(18, 13, 9, 0.74);
            box-shadow: 0 16px 45px rgba(0, 0, 0, 0.22);
            backdrop-filter: blur(10px);
        }

        .pay-highlight-icon {
            width: 48px;
            height: 48px;
            display: grid;
            place-items: center;
            border-radius: 50%;
            background: var(--copper);
            color: var(--white);
            font-family: var(--font-display);
            font-size: 1.25rem;
            font-weight: 700;
        }

        .pay-highlight strong,
        .pay-highlight span {
            display: block;
        }

        .pay-highlight strong {
            color: var(--white);
            font-family: var(--font-display);
            font-size: 1.2rem;
            font-weight: 600;
            letter-spacing: 0.025em;
            line-height: 1.15;
            text-transform: uppercase;
        }

        .pay-highlight span {
            margin-top: 5px;
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.76rem;
            line-height: 1.45;
        }

        .pay-process {
            position: relative;
            overflow: hidden;
            padding: 82px 0;
            background: var(--copper);
            color: var(--white);
        }

        .pay-process::after {
            position: absolute;
            top: -190px;
            right: -130px;
            width: 430px;
            height: 430px;
            border: 1px solid rgba(255, 255, 255, 0.14);
            border-radius: 50%;
            content: "";
        }

        .pay-process-layout {
            position: relative;
            z-index: 1;
            display: grid;
            grid-template-columns: minmax(280px, 0.78fr) minmax(0, 1.22fr);
            gap: 76px;
            align-items: center;
        }

        .pay-process .eyebrow {
            color: rgba(255, 255, 255, 0.78);
        }

        .pay-process .eyebrow > span {
            background: var(--white);
        }

        .pay-process h2 {
            margin-bottom: 18px;
            font-size: clamp(2.75rem, 4.8vw, 4.7rem);
        }

        .pay-process-copy > p:not(.eyebrow) {
            max-width: 470px;
            margin-bottom: 0;
            color: rgba(255, 255, 255, 0.78);
        }

        .pay-steps {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            background: rgba(23, 19, 15, 0.18);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .pay-step {
            min-height: 230px;
            padding: 30px 24px;
            border-right: 1px solid rgba(255, 255, 255, 0.18);
        }

        .pay-step:last-child {
            border-right: 0;
        }

        .pay-step-number {
            width: 38px;
            height: 38px;
            display: grid;
            place-items: center;
            margin-bottom: 35px;
            border: 1px solid rgba(255, 255, 255, 0.5);
            border-radius: 50%;
            font-family: var(--font-display);
            font-size: 0.85rem;
        }

        .pay-step strong {
            display: block;
            margin-bottom: 10px;
            font-family: var(--font-display);
            font-size: 1.2rem;
            font-weight: 600;
            line-height: 1.2;
            text-transform: uppercase;
        }

        .pay-step p {
            margin: 0;
            color: rgba(255, 255, 255, 0.72);
            font-size: 0.77rem;
            line-height: 1.6;
        }

        .delivery-note {
            margin: 16px 0 0;
            color: rgba(255, 255, 255, 0.68);
            font-size: 0.68rem;
        }

        @media (max-width: 900px) {
            .pay-process-layout {
                grid-template-columns: 1fr;
                gap: 38px;
            }
        }

        @media (max-width: 760px) {
            .hero {
                min-height: 960px;
            }

            .pay-highlight {
                gap: 13px;
                margin-bottom: 22px;
                padding: 14px;
            }

            .pay-highlight-icon {
                width: 42px;
                height: 42px;
                font-size: 1rem;
            }

            .pay-highlight strong {
                font-size: 1rem;
            }

            .pay-highlight span {
                font-size: 0.68rem;
            }

            .pay-process {
                padding: 66px 0;
            }

            .pay-process h2 {
                font-size: 3rem;
            }

            .pay-steps {
                grid-template-columns: 1fr;
            }

            .pay-step {
                min-height: auto;
                padding: 25px 22px;
                border-right: 0;
                border-bottom: 1px solid rgba(255, 255, 255, 0.18);
            }

            .pay-step:last-child {
                border-bottom: 0;
            }

            .pay-step-number {
                margin-bottom: 18px;
            }
        }
    </style>
</head>
<body>
    <a class="skip-link" href="#conteudo">Pular para o conteúdo</a>

    <div class="announcement" role="note">
        <span>Compre hoje e pague só na entrega</span>
        <span class="announcement-divider" aria-hidden="true"></span>
        <span>Pix ou maquininha</span>
    </div>

    <header class="site-header" data-header>
        <div class="container header-inner">
            <a class="brand" href="#inicio" aria-label="Cutelo Chef, página inicial">
                <span class="brand-mark" aria-hidden="true">C</span>
                <span class="brand-copy">
                    <strong>CUTELO CHEF</strong>
                    <small>Forjado para performance</small>
                </span>
            </a>

            <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="main-nav" data-menu-toggle>
                <span></span><span></span><span></span>
                <span class="sr-only">Abrir menu</span>
            </button>

            <nav class="main-nav" id="main-nav" aria-label="Navegação principal" data-nav>
                <a href="#beneficios">Benefícios</a>
                <a href="#pagamento">Pagamento</a>
                <a href="#detalhes">Detalhes</a>
                <a href="#especificacoes">Especificações</a>
                <a href="#galeria">Galeria</a>
            </nav>

            <a class="button button-small header-cta" href="{{ checkout_url }}" target="_blank" rel="noopener noreferrer">
                Pedir agora
            </a>
        </div>
    </header>

    <main id="conteudo">
        <section class="hero" id="inicio">
            <div class="hero-media" aria-hidden="true">
                <img src="{{ url_for('static', filename='images/hero-cutelo.webp') }}" alt="" width="1600" height="1067" fetchpriority="high">
            </div>
            <div class="hero-overlay" aria-hidden="true"></div>
            <div class="container hero-layout">
                <div class="hero-copy reveal">
                    <p class="eyebrow"><span></span> Peça hoje • pague somente ao receber</p>
                    <h1>Força no corte.<br><em>Precisão no preparo.</em></h1>
                    <p class="hero-description">
                        O Cutelo Chef Grande combina lâmina larga em aço inox com cabo de madeira firme para acompanhar o preparo de carnes, peixes e receitas que exigem controle.
                    </p>
                    <div class="pay-highlight" role="note" aria-label="Pagamento somente na entrega">
                        <div class="pay-highlight-icon" aria-hidden="true">$</div>
                        <div>
                            <strong>Compre hoje e pague só na entrega</strong>
                            <span>Receba no dia seguinte e pague ao entregador por Pix ou maquininha.</span>
                        </div>
                    </div>
                    <div class="hero-actions">
                        <a class="button button-primary" href="{{ checkout_url }}" target="_blank" rel="noopener noreferrer">
                            Comprar hoje
                            <span aria-hidden="true">→</span>
                        </a>
                        <a class="text-link" href="#detalhes">Conhecer os detalhes <span aria-hidden="true">↓</span></a>
                    </div>
                    <ul class="hero-proof" aria-label="Destaques do produto">
                        <li><strong>31 cm</strong><span>comprimento</span></li>
                        <li><strong>480 g</strong><span>peso aprox.</span></li>
                        <li><strong>Pix / cartão</strong><span>somente na entrega</span></li>
                    </ul>
                </div>
            </div>
        </section>

        <section class="trust-strip" aria-label="Principais características">
            <div class="container trust-grid">
                <div><span class="trust-number">01</span><strong>Aço inox</strong><small>Resistente e fácil de higienizar</small></div>
                <div><span class="trust-number">02</span><strong>Pegada firme</strong><small>Cabo aderente em madeira</small></div>
                <div><span class="trust-number">03</span><strong>Uso versátil</strong><small>Para diferentes preparos</small></div>
                <div><span class="trust-number">04</span><strong>Pague na entrega</strong><small>Pix ou maquininha</small></div>
            </div>
        </section>

        <section class="pay-process" id="pagamento" aria-labelledby="pay-process-title">
            <div class="container pay-process-layout">
                <div class="pay-process-copy reveal">
                    <p class="eyebrow"><span></span> Sem pagamento antecipado</p>
                    <h2 id="pay-process-title">Compre hoje.<br>Receba amanhã.<br>Pague na entrega.</h2>
                    <p>Faça seu pedido pelo site e deixe para pagar somente quando o Cutelo Chef chegar até você.</p>
                    <p class="delivery-note">* Entrega no dia seguinte sujeita à disponibilidade da sua região.</p>
                </div>
                <div class="pay-steps reveal" aria-label="Como comprar e pagar na entrega">
                    <article class="pay-step">
                        <span class="pay-step-number">01</span>
                        <strong>Faça seu pedido</strong>
                        <p>Clique em comprar e preencha os dados necessários para a entrega.</p>
                    </article>
                    <article class="pay-step">
                        <span class="pay-step-number">02</span>
                        <strong>Receba no dia seguinte</strong>
                        <p>Seu pedido é preparado para chegar até você com rapidez.</p>
                    </article>
                    <article class="pay-step">
                        <span class="pay-step-number">03</span>
                        <strong>Pague ao receber</strong>
                        <p>Na entrega, escolha pagar por Pix ou diretamente na maquininha.</p>
                    </article>
                </div>
            </div>
        </section>

        <section class="section benefits" id="beneficios">
            <div class="container">
                <div class="section-heading reveal">
                    <div>
                        <p class="eyebrow eyebrow-dark"><span></span> Feito para o preparo de verdade</p>
                        <h2>Um cutelo robusto,<br>do fogo à cozinha.</h2>
                    </div>
                    <p>Formato amplo, materiais resistentes e construção pensada para dar mais firmeza aos movimentos em diferentes rotinas de preparo.</p>
                </div>

                <div class="benefit-grid">
                    <article class="benefit-card reveal">
                        <span class="card-index">01</span>
                        <div class="line-icon" aria-hidden="true"><span></span></div>
                        <h3>Lâmina ampla em inox</h3>
                        <p>Superfície larga para cortes firmes e apoio no manuseio dos alimentos.</p>
                    </article>
                    <article class="benefit-card reveal">
                        <span class="card-index">02</span>
                        <div class="line-icon icon-handle" aria-hidden="true"><span></span></div>
                        <h3>Cabo inteiriço de madeira</h3>
                        <p>Construção aderente, fixada com pinos de aço inoxidável, para uma pegada mais segura.</p>
                    </article>
                    <article class="benefit-card reveal">
                        <span class="card-index">03</span>
                        <div class="line-icon icon-clean" aria-hidden="true"><span></span></div>
                        <h3>Higienização simples</h3>
                        <p>Materiais e formato adequados para facilitar o cuidado após o uso.</p>
                    </article>
                </div>
            </div>
        </section>

        <section class="section story-section" id="detalhes">
            <div class="container story-grid">
                <div class="story-image reveal">
                    <img src="{{ url_for('static', filename='images/churrasco-acao.webp') }}" alt="Cutelo sendo usado para fatiar carne assada sobre uma tábua" width="1200" height="900" loading="lazy">
                    <div class="image-caption"><span>01</span> Controle no preparo</div>
                </div>
                <div class="story-copy reveal">
                    <p class="eyebrow eyebrow-light"><span></span> Versatilidade à mesa</p>
                    <h2>Do corte mais delicado ao preparo que pede firmeza.</h2>
                    <p>Use no preparo de carnes, peixes, carne com osso e nas tarefas do dia a dia na cozinha. O formato robusto também acompanha atividades de pesca e caça.</p>
                    <ul class="check-list">
                        <li><span aria-hidden="true">✓</span> Mais firmeza ao segurar</li>
                        <li><span aria-hidden="true">✓</span> Cabo de madeira aderente</li>
                        <li><span aria-hidden="true">✓</span> Pinos em aço inoxidável</li>
                    </ul>
                    <a class="button button-outline" href="{{ checkout_url }}" target="_blank" rel="noopener noreferrer">Ir para o checkout <span aria-hidden="true">→</span></a>
                </div>
            </div>
        </section>

        <section class="section craftsmanship">
            <div class="container craftsmanship-grid">
                <div class="craft-copy reveal">
                    <p class="eyebrow eyebrow-dark"><span></span> Pegada e acabamento</p>
                    <h2>Madeira, aço e presença.</h2>
                    <p>O cabo inteiriço de madeira foi pensado para manter o controle nas mãos, enquanto os pinos de aço inoxidável reforçam a construção.</p>
                    <div class="material-notes">
                        <div><strong>Madeira</strong><span>Pegada aderente</span></div>
                        <div><strong>Aço inox</strong><span>Lâmina e fixação</span></div>
                    </div>
                </div>
                <figure class="craft-image reveal">
                    <img src="{{ url_for('static', filename='images/detalhe-cabo.webp') }}" alt="Detalhe do cabo de madeira com três pinos e da lâmina em aço inox" width="1200" height="800" loading="lazy">
                </figure>
            </div>
        </section>

        <section class="section specifications" id="especificacoes">
            <div class="container specs-grid">
                <div class="spec-visual reveal">
                    <img src="{{ url_for('static', filename='images/flatlay-premium.webp') }}" alt="Cutelo Chef Grande apresentado sobre uma bancada de madeira" width="1200" height="1200" loading="lazy">
                    <span class="dimension dimension-length">31 cm</span>
                    <span class="dimension dimension-width">10 cm</span>
                </div>
                <div class="spec-copy reveal">
                    <p class="eyebrow eyebrow-light"><span></span> Ficha técnica</p>
                    <h2>Proporções que entregam presença e controle.</h2>
                    <dl class="spec-list">
                        <div><dt>Comprimento</dt><dd>31 cm</dd></div>
                        <div><dt>Largura</dt><dd>10 cm</dd></div>
                        <div><dt>Altura</dt><dd>2 cm</dd></div>
                        <div><dt>Peso aproximado</dt><dd>480 g</dd></div>
                        <div><dt>Lâmina</dt><dd>Aço inox</dd></div>
                        <div><dt>Cabo</dt><dd>Madeira inteiriça</dd></div>
                    </dl>
                </div>
            </div>
        </section>

        <section class="section gallery-section" id="galeria">
            <div class="container">
                <div class="section-heading gallery-heading reveal">
                    <div>
                        <p class="eyebrow eyebrow-dark"><span></span> Veja de perto</p>
                        <h2>Detalhes que falam<br>antes do primeiro corte.</h2>
                    </div>
                    <p>Uma visão completa do produto, do acabamento ao uso em diferentes preparos.</p>
                </div>

                <div class="gallery-grid" data-gallery>
                    <button class="gallery-item gallery-large reveal" type="button" data-gallery-src="{{ url_for('static', filename='images/cozinha-preparo.webp') }}" aria-label="Ampliar imagem do cutelo em uso na cozinha">
                        <img src="{{ url_for('static', filename='images/cozinha-preparo.webp') }}" alt="Cutelo em uma bancada de cozinha durante o preparo de alimentos" width="1200" height="1500" loading="lazy">
                    </button>
                    <button class="gallery-item reveal" type="button" data-gallery-src="{{ url_for('static', filename='images/kit-bainha.webp') }}" aria-label="Ampliar imagem do cutelo com bainha">
                        <img src="{{ url_for('static', filename='images/kit-bainha.webp') }}" alt="Conjunto com Cutelo Chef Grande e bainha" width="1200" height="900" loading="lazy">
                    </button>
                    <button class="gallery-item reveal" type="button" data-gallery-src="{{ url_for('static', filename='images/detalhe-cabo.webp') }}" aria-label="Ampliar detalhe do cabo">
                        <img src="{{ url_for('static', filename='images/detalhe-cabo.webp') }}" alt="Detalhe do cabo inteiriço de madeira" width="1200" height="800" loading="lazy">
                    </button>
                    <button class="gallery-item reveal" type="button" data-gallery-src="{{ url_for('static', filename='images/hero-cutelo.webp') }}" aria-label="Ampliar foto principal do cutelo">
                        <img src="{{ url_for('static', filename='images/hero-cutelo.webp') }}" alt="Cutelo Chef Grande sobre tábua de madeira escura" width="1600" height="1067" loading="lazy">
                    </button>
                    <button class="gallery-item gallery-wide reveal" type="button" data-gallery-src="{{ url_for('static', filename='images/churrasco-acao.webp') }}" aria-label="Ampliar imagem do cutelo no churrasco">
                        <img src="{{ url_for('static', filename='images/churrasco-acao.webp') }}" alt="Cutelo em uso durante um churrasco" width="1200" height="900" loading="lazy">
                    </button>
                </div>
                <p class="illustrative-note">* Imagens meramente ilustrativas.</p>
            </div>
        </section>

        <section class="section included-section">
            <div class="container included-grid">
                <div class="included-image reveal">
                    <img src="{{ url_for('static', filename='images/kit-bainha.webp') }}" alt="Cutelo Chef Grande acompanhado de bainha" width="1400" height="1000" loading="lazy">
                </div>
                <div class="included-copy reveal">
                    <p class="eyebrow eyebrow-dark"><span></span> Na sua compra</p>
                    <h2>O essencial para começar.</h2>
                    <div class="included-items">
                        <div><span>01</span><strong>Cutelo Chef Grande</strong></div>
                        <div><span>01</span><strong>Bainha</strong></div>
                    </div>
                    <p class="included-note">Guarde o cutelo limpo e seco. Mantenha fora do alcance de crianças.</p>
                </div>
            </div>
        </section>

        <section class="section faq-section" id="duvidas">
            <div class="container faq-grid">
                <div class="faq-title reveal">
                    <p class="eyebrow eyebrow-dark"><span></span> Dúvidas frequentes</p>
                    <h2>Antes de escolher<br>o seu cutelo.</h2>
                </div>
                <div class="faq-list reveal">
                    <details>
                        <summary>Preciso pagar agora para fazer o pedido?<span aria-hidden="true">+</span></summary>
                        <p>Não. Você faz o pedido hoje e paga somente no momento da entrega, por Pix ou maquininha.</p>
                    </details>
                    <details>
                        <summary>Quando o produto será entregue?<span aria-hidden="true">+</span></summary>
                        <p>A entrega é prevista para o dia seguinte à compra, conforme a disponibilidade de atendimento da sua região.</p>
                    </details>
                    <details>
                        <summary>Qual é o material da lâmina?<span aria-hidden="true">+</span></summary>
                        <p>A lâmina é produzida em aço inox, material resistente e de higienização simples.</p>
                    </details>
                    <details>
                        <summary>O cabo é inteiriço?<span aria-hidden="true">+</span></summary>
                        <p>Sim. O cabo inteiriço é revestido em madeira aderente e fixado com pinos de aço inoxidável.</p>
                    </details>
                    <details>
                        <summary>Em quais preparos posso utilizar?<span aria-hidden="true">+</span></summary>
                        <p>É indicado para cortar carnes, peixes, carne com osso e para uso geral na cozinha, além de atividades de pesca e caça.</p>
                    </details>
                    <details>
                        <summary>O que vem na embalagem?<span aria-hidden="true">+</span></summary>
                        <p>A compra inclui uma unidade do Cutelo Chef Grande e uma bainha.</p>
                    </details>
                </div>
            </div>
        </section>

        <section class="final-cta">
            <div class="final-cta-image" aria-hidden="true">
                <img src="{{ url_for('static', filename='images/churrasco-acao.webp') }}" alt="" width="1600" height="1000" loading="lazy">
            </div>
            <div class="final-cta-overlay" aria-hidden="true"></div>
            <div class="container final-cta-content reveal">
                <p class="eyebrow"><span></span> Peça sem pagar antecipado</p>
                <h2>Compre hoje e pague<br>somente na entrega.</h2>
                <p>Receba o Cutelo Chef no dia seguinte e escolha pagar por Pix ou maquininha no momento da entrega.</p>
                <a class="button button-primary button-large" href="{{ checkout_url }}" target="_blank" rel="noopener noreferrer">Fazer meu pedido <span aria-hidden="true">→</span></a>
                <small>Você não paga agora. O pagamento é realizado somente quando receber o produto.</small>
            </div>
        </section>
    </main>

    <footer class="site-footer">
        <div class="container footer-grid">
            <a class="brand brand-footer" href="#inicio" aria-label="Voltar ao início">
                <span class="brand-mark" aria-hidden="true">C</span>
                <span class="brand-copy"><strong>CUTELO CHEF</strong><small>Forjado para performance</small></span>
            </a>
            <p>Produto cortante. Use com responsabilidade, higienize após o uso e mantenha em local seguro.</p>
            <a href="{{ checkout_url }}" target="_blank" rel="noopener noreferrer">Fazer pedido <span aria-hidden="true">↗</span></a>
        </div>
        <div class="container footer-bottom">
            <span>© <span data-year></span> Cutelo Chef. Todos os direitos reservados.</span>
            <span>Imagens meramente ilustrativas.</span>
        </div>
    </footer>

    <a class="mobile-buy" href="{{ checkout_url }}" target="_blank" rel="noopener noreferrer" aria-label="Comprar Cutelo Chef Grande agora">
        <span><small>Pague só na entrega</small><strong>Comprar hoje</strong></span>
        <span aria-hidden="true">→</span>
    </a>

    <dialog class="lightbox" data-lightbox aria-label="Visualização ampliada da galeria">
        <button type="button" data-lightbox-close aria-label="Fechar imagem ampliada">×</button>
        <img src="" alt="Imagem ampliada do produto" data-lightbox-image>
    </dialog>

    <script src="{{ url_for('static', filename='js/main.js') }}" defer></script>
</body>
</html>
